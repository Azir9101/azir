import requests


class RiotApiError(Exception):
    pass

class RiotApi(object):
    def __init__(self, key, region='kr'):
        self.key = key
        self.region = region

    def _request(self, url, **kwargs):
        pass
