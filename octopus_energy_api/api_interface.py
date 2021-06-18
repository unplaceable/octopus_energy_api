import requests

class api:

    def __init__(self, api_key):
        self._api_key = api_key

    def create_session(self):
        
        session = requests.session()

        session.auth = (self._api_key, "")

        return session

    def run(self, url):

        session = self.create_session()
        
        response = session.request(method="GET", url=url)

        parsed = response.json()

        return( parsed )