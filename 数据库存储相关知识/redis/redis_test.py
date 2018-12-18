#!/usr/bin/env python
# -*- coding: utf-8 -*-


import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('name', 'huangxiang')
print(r['name'])
print(r.get('name'))
print(type(r.get('name')))


