from github import GithubClient
from decouple import config

if __name__ == '__main__':
    client = GithubClient(
        login=config('LOGIN'),
        token=config('API_KEY'),
        auto_auth=True,
    )

    # not needed when `auto_auth` is set to True
    # client.authenticate_user()

    info = client.get_my_info()
