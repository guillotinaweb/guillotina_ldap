from guillotina.auth.users import GuillotinaUser
from guillotina.component import get_utility
from guillotina_ldap.interfaces import ILDAPUsers


class LDAPGuillotinaUser(GuillotinaUser):

    async def set_password(self, password, old_password=None, oldpassword=None):
        # Guillotina calls old_password=; keep oldpassword for backwards compatibility.
        previous = old_password if old_password is not None else oldpassword
        util = get_utility(ILDAPUsers)
        set_password = False
        if previous is not None and await util.validate_user(self.id, previous):
            set_password = True
        elif previous is None:
            set_password = True

        if set_password:
            await util.set_password(self.id, password)
