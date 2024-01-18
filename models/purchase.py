# -*- coding: utf-8 -*-

from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    sales_per_year = fields.Float(
        related="product_id.sales_count", string="Sales (Last 365 days)"
    )
    color = fields.Integer(default=2, compute="_compute_color", readonly=True)
    order_line = fields.One2many(
        "purchase.order.line", "order_id", string="Order Lines"
    )
    product_need_count = fields.Float(
        string="Qty Needed",
        digits="Product Unit of Measure",
        compute="_compute_product_need_count",
    )
    sale_order_lines = fields.One2many(
        "sale.order.line", "order_id", string="Sale Order Lines"
    )

    @api.depends("order_line")
    def _compute_product_need_count(self):
        for product in self:
            domain = [
                ("order_id.state", "=", "draft"),
                ("name", "=", product.name),
            ]
            total_quantity = sum(
                product.sale_order_lines.search(domain).mapped("product_uom_qty")
            )
            product.product_need_count = total_quantity

    @api.depends("quantity_available_gse", "product_need_count", "sales_per_year")
    def _compute_color(self):
        for product in self:
            if product.quantity_available_gse <= product.product_need_count:
                product.color = 10  # Green color
            elif (
                product.quantity_available_gse > product.product_need_count
                or product.sales_per_year <= product.quantity_available_gse
            ):
                product.color = 9  # Red color
