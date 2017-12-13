# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Variation"]


class Variation(Resource):
    def create(self, variation_data):
        """
        To add a new variation to a product you can create a product variation.
        For example, a product has sizes “Large” and “Extra-Large” and you wanted to add size “Medium”,
        you would create a new product variation with this API.
        :param variation_data:
        :return:
        """
        return self.client.execute("variant/add", "POST", variation_data)

    def retrieve(self, **kwargs):
        """
        Retrieve a Product Variation
        Retrieves the details of an existing product variation.
        Provide the SKU of the product variation and Joom will return details about the corresponding product variation.
        GET https://api-merchant.joom.com/api/v2/variant
        :param kwargs:
        :return:
        """
        return self.client.execute("variant", "GET", kwargs)

    def update(self, update_data):
        """
        Update a Product Variation
        Updates the specified variation by updating the attributes of the parameters passed in the request.
        Any attribute not provided will be left unchanged.
        This request can only update attributes specific to variations and cannot be used to update any attribute of a Product.
        POST https://api-merchant.joom.com/api/v2/variant/update
        :param update_data:
        :return:
        """
        return self.client.execute("variant/update", "POST", update_data)

    def change_sku(self, **kwargs):
        """
        Change a Product Variation’s SKU
        Change a variantion’s unique identifier, the new identifier must also be unique within all SKUs of the merchant.
        POST https://api-merchant.joom.com/api/v2/variant/change-sku
        :param kwargs:
        :return:
        """
        return self.client.execute("/variant/change-sku", "POST", kwargs)

    def enable(self, **kwargs):
        """
        Enable a Product Variation
        Enable a product variation. This marks the product variation available for sale.
        POST https://api-merchant.joom.com/api/v2/variant/enable
        :param kwargs:
        :return:
        """
        return self.client.execute("/variant/enable", "POST", kwargs)

    def disable(self, **kwargs):
        """
        Disable a Product Variation
        Disable a product variation. This marks the product variation unavailable for sale.
        POST https://api-merchant.joom.com/api/v2/variant/disable
        :param kwargs:
        :return:
        """
        return self.client.execute("/variant/disable", "POST", kwargs)

    def update_inventory(self, **kwargs):
        """
        Update Inventory
        Update inventory for a product variation.
        POST https://api-merchant.joom.com/api/v2/variant/update-inventory
        :param kwargs:
        :return:
        """
        return self.client.execute("/variant/update-inventory", "POST", kwargs)

    def list(self, **kwargs):
        """
        List All Product Variations
        Returns a list of all your product variations currently on the Joom platform.
        This API is useful to paginate through all the SKUs that you have uploaded to Joom.
        If the number of results is too large the full result set may require pagination.
        GET https://api-merchant.joom.com/api/v2/variant/multi-get
        :param kwargs:
        :return:
        """
        return self.client.execute("/variant/multi-get", "GET", kwargs)
