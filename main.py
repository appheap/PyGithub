from github import GithubClient
from decouple import config

if __name__ == '__main__':
    client = GithubClient(
        login=config('LOGIN'),
        token=config('API_KEY')
    )

    info = client.get_my_info()
