from src.metrisapi.base import json_response, MetrisClient


class AccountClient(MetrisClient):
    @json_response
    def authenticate(self, username, password):
        uri = f'{self.base_uri}/api/account/authenticate'
        data = {'username': username, 'password': password}
        return self.session.post(uri, json=data)  # apply with 2020.R3
        # return self.session.post(uri, data=data)  # outdated after 2020.R2.SP4

    @json_response
    def validate_token(self, token):
        uri = f'{self.base_uri}/api/account/validatetoken'
        return self.session.post(uri, json=token)