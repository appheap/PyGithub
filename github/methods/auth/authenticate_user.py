from github.scaffold import Scaffold


class AuthenticateUser(Scaffold):
    def authenticate_user(self) -> bool:
        response = self.get_authenticated_user_info()
        if response.success:
            self.user = response.result[0]
            self.headers = response.result[1]
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = False
            # todo: raise error
            pass
        return False
