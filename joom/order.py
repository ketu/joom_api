# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Order"]
class Order(Resource):
    def retrieve(self, **kwargs):
        """
        Retrieve an Order
        Retrieves the details of an existing order.
        Supply the unique identifier for the order and if one exists this API will return the corresponding order.
        Each order will have all the information you need to fulfill it.
        GET https://api-merchant.joom.com/api/v2/order
        :param kwargs:
        :return:
        """
        return self.client.execute("order", "GET", kwargs)

    def retrieve_recently_changed_orders(self, **kwargs):
        """
        Retrieve Recently Changed Orders
        Returns all orders that have changed state since the date and time requested.
        Use this API to keep your orders processing system in sync with Joom.
        This API takes a parameter since and returns all orders that were updated since this time.
        GET https://api-merchant.joom.com/api/v2/order/multi-get
        :param kwargs:
        :return:
        """
        return self.client.execute("order/multi-get", "GET", kwargs)

    def retrieve_unfulfilled_orders(self, **kwargs):
        """
        Retrieve Unfulfilled Orders
        Returns all orders that currently require fulfillment. This API takes no parameters but may require pagination if the number of orders is too large.
        GET https://api-merchant.joom.com/api/v2/order/get-fulfill
        :param kwargs:
        :return:
        """
        return self.client.execute("order/get-fulfill", "GET", kwargs)

    def fulfill_order(self, **kwargs):
        """
        Fulfills an order in the Joom system.
        Call this API once you have shipped the item to the recipient.
        Joom will notify the user their order has been shipped upon completion of this request.
        POST https://api-merchant.joom.com/api/v2/order/fulfill-one
        :param kwargs:
        :return:
        """
        return self.client.execute("order/fulfill-one", "POST", kwargs)

    def cancel_order(self, **kwargs):
        """
        Refund/Cancel an order in the Joom system.
        Call this API if you cannot fulfill the order for any reason.
        Joom will notify the user their order has been cancelled shipped and refund them upon completion of this request.
        POST https://api-merchant.joom.com/api/v2/order/refund
        :param kwargs:
        :return:
        """
        return self.client.execute("order/refund", "POST", kwargs)

    def modify_tracking(self, **kwargs):
        """
        Update tracking information about an order. Call this to change the tracking number or provider for an order that has already been marked shipped.
        POST https://api-merchant.joom.com/api/v2/order/modify-tracking

        :param kwargs:
        :return:
        """
        return self.client.execute("order/modify-tracking", "POST", kwargs)

    def fulfill_order_online(self, **kwargs):
        """
        Call this API via Joom when you are ready to request shipment of an order, using one of our accepted shipping providers that offer online shipping.
        Joom will automatically transfer the order information, such as package weight, to your shipping carrier of choice.
        Once the carrier confirms the request, Joom will assign a tracking number to that order.
        POST https://api-merchant.joom.com/api/v2/order/fulfill-online
        :param kwargs:
        :return:
        """
        return self.client.execute("order/fulfill-online", "POST", kwargs)

    def get_shipping_label(self, **kwargs):
        """
        Get a Printable Label
        Get a printable PDF label for the order fulfilled with the Online Shipping method.
        You should print and attach the PDF label to the package.
        Call this API once you have packed the order and are ready to print the label for the package. 
        POST https://api-merchant.joom.com/api/v2/order/shipping-label
        :param kwargs:
        :return:
        """
        return self.client.execute("order/shipping-label", "POST", kwargs)
