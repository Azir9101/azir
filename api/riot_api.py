import os
import requests
import config_riot

URLS = config_riot.URLS
VERSIONS = config_riot.VERSIONS

class RiotApiError(Exception):
    pass

class RiotApi(object):
    def __init__(self, key=None, region='kr'):
        if key is None:
            self.key = os.getenv('RIOT_API_KEY')
        else:
            self.key = key
        self.region = region

    def _request(self, url, static=False, **kwargs):
        if self.key is None:
            raise RiotApiError('api key is none')
        params = kwargs
        if params is None:
            params = {}
        params.update({'api_key':self.key})
        if not static:
            base_url = 'https://{region}.api.pvp.net'.format(region=self.region)
            url = base_url+url
        else:
            base_url = 'https://global.api.pvp.net'
            url = base_url+url
        resp = requests.get(url, params=params)
        return resp.json()
        
    def get_summoner_id(self, username):
        sub_url = URLS['summoner_byname'].format(region=self.region,
                                   version=VERSIONS['summoner'], summonerNames=username)
        return self._request(sub_url)
