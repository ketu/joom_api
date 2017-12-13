# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource
__all__ = ["Product"]

class Product(Resource):
    def create(self, product_data):
        """
        The /product/add endpoint creates a new product.
        It also createы the first variant of that product, so if a product has a single variant,
        both the product and variant can be created with this endpoint.
        If you have further variant, you can create them using the /variant/add endpoint.
        For clarity, we describe parameters related to product and variant in separate tables.
        When you make a request, parameters from both tables should be provided in a single form body.
        POST https://api-merchant.joom.com/api/v2/product/add
        :param product_data:
        :return:
        """
        return self.client.execute("product/add", "POST", product_data)

    def disable(self, **kwargs):
        """
        Disable a Product
        The /product/disable endpoint disables a product and all its variants, making them unavailable for sale.
        :param kwargs:
        :return:
        """
        return self.client.execute("product/disable", "POST", kwargs)

    def enable(self, **kwargs):
        """
        Enable a Product
        The /product/enable endpoint enables a product and all its variants, making them available for sale. You only need to enable a product if you previously disabled it.
        POST https://api-merchant.joom.com/api/v2/product/enable
        :param kwargs:
        :return:
        """
        return self.client.execute("product/enable", "POST", kwargs)

    def list(self, **kwargs):
        """
        List All Products
        Returns a list of all your products currently on the Joom platform. If you have a high number of products the response will be paginated.
        The response contains the URL for fetching the next page of products.
        GET https://api-merchant.joom.com/api/v2/product/multi-get
        :param kwargs:
        :return:
        """
        return self.client.execute("product/multi-get", "GET", kwargs)

    def retrieve(self, **kwargs):
        """
        Retrieve a Product
        The /product endpoint retrives a product given either parent SKU you have specified, or the Joom product ID that was returned upon product creation.
        GET https://api-merchant.joom.com/api/v2/product
        :param kwargs:
        :return:
        """
        return self.client.execute("product", "GET", kwargs)

    def update(self, product_data):
        """
        Update a Product

        Updates the specified product with the parameters passed in the request. Any attribute not provided will be left unchanged.
        For example, if you pass the name parameter the name of the product is updated, while other fields are left unchanged.
        This request can only update product attributes; even for products with a single variant, variant attributes cannot be modified.
        POST https://api-merchant.joom.com/api/v2/product/update
        :param product_data:
        :return:
        """
        return self.client.execute("product", "GET", product_data)

    def remove_extra_images(self, **kwargs):
        """
        Remove Extra Images from a Product

        This removes all the extra images from the product. The main product image and variation images will not be affected.

        POST
        https://api-merchant.joom.com/api/v2/product/remove-extra-images

        :param kwargs:
        :return:
        """
        return self.client.execute("product/remove-extra-images", "GET", kwargs)
