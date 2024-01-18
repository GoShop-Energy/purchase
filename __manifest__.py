# -*- coding: utf-8 -*-
{
    "name": "purchase_custo quality check",
    "summary": """
        Customizations pour Goshop Energy""",
    "description": """
        Add quality check on purchase order line
    """,
    "author": "Benjamin Kisenge",
    "website": "https://dev--glowing-faun-e9789d.netlify.app/",
    "category": "Customizations",
    "version": "0.1.8.7",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": [
        "account",
        "base",
        "base_automation",
        "crm",
        "hr",
        "industry_fsm_report",
        "mrp",
        "partner_commission",
        "project",  # recurrence
        "sale_project",
        "stock",  # qty_available
        "website_sale",  # public_categ_ids
        "purchase",
    ],
    "data": [
        "views/purchase_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "gse_custo/static/scss/gse_custo.scss",
        ]
    },
}
