import inspect
import json

import jwt
import pytest

from guillotina.testing import TESTING_SETTINGS
from guillotina_ldap.model import LDAPGuillotinaUser


@pytest.mark.asyncio
async def test_ldap_login(ldap, container_requester):
    async with container_requester as requester:
        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "anna", "password": "newsecret"}),
        )
        assert status_code == 200

        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "Anna", "password": "newsecret"}),
        )
        assert status_code == 200
        payload = jwt.decode(
            resp["token"], TESTING_SETTINGS["jwt"]["secret"], algorithms=["HS256"]
        )
        assert payload["id"] == "anna"


def test_set_password_accepts_guillotina_old_password_keyword():
    params = inspect.signature(LDAPGuillotinaUser.set_password).parameters
    assert "old_password" in params


@pytest.mark.asyncio
async def test_ldap_reset_password_with_old_password_keyword(ldap, container_requester):
    async with container_requester as requester:
        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "anna", "password": "newsecret"}),
        )
        assert status_code == 200
        token = resp["token"]

        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@users/anna/reset-password",
            token=token,
            auth_type="Bearer",
            data=json.dumps(
                {"old_password": "newsecret", "new_password": "newersecret"}
            ),
        )
        assert status_code == 200

        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "anna", "password": "newersecret"}),
        )
        assert status_code == 200
