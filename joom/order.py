# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource


class Order(Resource):

    def query(self, **kwargs):
        resp = self.client.execute("order/get-fulfill", "GET", kwargs)

        print(resp)
        print(resp.text)

    def retrieve_recently_changed_orders(self, **kwargs):
        resp = self.client.execute("order/multi-get", "GET", kwargs)

        print(resp)
        print(resp.text)


