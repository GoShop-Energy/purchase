# -*- coding: utf-8 -*-

from odoo.addons.account.tests.common import AccountTestInvoicingCommon
from odoo.tests import tagged


@tagged("-at_install", "post_install")
class TestPurchase(AccountTestInvoicingCommon):
    def setUp(self):
        super(TestPurchase, self).setUp()
        partner = self.env["res.partner"].create(
            {
                "name": "Test Partner",
                "email": "test.partner@example.com",
            }
        )

        product = self.env["product.product"].create(
            {
                "name": "Test Product",
                "type": "product",
                "list_price": 100.0,
            }
        )

        self.product = self.env["purchase.order"].create(
            {
                "name": "Test Product",
                "partner_id": partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": product.id,
                            "name": product.name,
                            "product_qty": 1.0,
                            "product_uom": product.uom_id.id,
                            "price_unit": product.list_price,
                        },
                    )
                ],
            }
        )

    def test_compute_color_green(self):
        self.product.order_line.quantity_available_gse = 5.0
        self.product.order_line.product_need_count = 10.0
        self.product.order_line.sales_per_year = 10.0

        self.product.order_line._compute_color()

        # Check if the color is set to 10 (Green)
        self.assertEqual(self.product.order_line.color, 10)

    def test_compute_color_red_1(self):
        self.product.order_line.quantity_available_gse = 15.0
        self.product.order_line.product_need_count = 10.0
        self.product.order_line.sales_per_year = 5.0

        self.product.order_line._compute_color()

        # Check if the color is set to 9 (Red)
        self.assertEqual(self.product.order_line.color, 9)
