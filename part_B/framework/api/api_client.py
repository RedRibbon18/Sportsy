import requests
from framework.config import get_environment_config


class ApiClient:
    def __init__(self, base_url: str | None = None, env: str | None = None):
        config = get_environment_config(env)
        self.base_url = (base_url or config.api_base_url).rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, params=None, headers=None):
        return self.session.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            params=params,
            headers=headers
        )

    def post(self, endpoint: str, json=None, data=None, headers=None):
        return self.session.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            json=json,
            data=data,
            headers=headers,
        )

    def put(self, endpoint: str, json=None, data=None, headers=None):
        return self.session.put(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            json=json,
            data=data,
            headers=headers,
        )

    def delete(self, endpoint: str, params=None, headers=None):
        return self.session.delete(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            params=params,
            headers=headers
        )
