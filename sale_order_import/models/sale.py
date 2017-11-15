# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ErrorLog(models.Model):
    _inherit = 'error.log'

    sale_order_ids = fields.One2many(
        'sale.order',
        'error_log_id',
        string='Related Sale Orders'
    )


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    imported_order = fields.Boolean(
        'Is Imported',
        readonly=True,
    )
    order_ref = fields.Char(
        'Order Reference',
        readonly=True
    )
    error_log_id = fields.Many2one(
        relation='error.log',
        string='Import Log',
        readonly=True
    )
