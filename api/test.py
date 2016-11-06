#-*- coding: utf-8 -*-

import riot_api

a = riot_api.RiotApi()
result = a.get_summoner_id('트린다먹어')

print result
