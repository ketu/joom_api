# /usr/bin/env python
# -*- coding:utf8 -*-

import json
from urllib.parse import urljoin
from requests import Request, Session
from .settings import BASE_URL
from .order import Order
from .product import Product


installed_module = {
    "order": Order,
    "product": Product
}




class ClientMeta(type):
    def __new__(mcs, name, bases, dct):
        klass = super(ClientMeta, mcs).__new__(mcs, name, bases, dct)
        setattr(
            klass, "installed_module",
            installed_module
        )
        return klass


class Client(object, metaclass=ClientMeta):
    __metaclass__ = ClientMeta
    cached_module = {}

    def __init__(self, access_token):
        self.access_token = access_token


    def __getattr__(self, name):
        try:
            value = super(Client, self).__getattribute__(name)
        except AttributeError as e:
            value = self.get_cached_module(name)
            if not value:
                raise e
        return value


    def build_request(self, uri, method, body):

        url = urljoin(BASE_URL, uri)

        headers = {
            "Authorization": "Bearer "+ self.access_token
        }

        req = Request(method, url, headers=headers)

        if body:
            if req.method in ["POST", "PUT", "PATH"]:
                req.data = body
            else:
                req.params = body
        return req

    def execute(self, uri, method, body):
        method = method.upper()
        req = self.build_request(uri, method, body)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped)
        return resp

    def get_cached_module(self, key):
        cached_module = self.cached_module.get(key)
        if not cached_module:
            installed = self.installed_module.get(key)
            if not installed:
                return None
            cached_module = installed(self)
            self.cached_module.setdefault(key, cached_module)
        return cached_module

