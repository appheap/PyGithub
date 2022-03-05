from github.scaffold import Scaffold


class AuthenticateUser(Scaffold):
    def authenticate_user(self) -> bool:
        success, res = self.get_authenticated_user_info()
        if success:
            self.user = res[0]
            self.headers = res[1]
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = False
            # todo: raise error
            pass
        return False
