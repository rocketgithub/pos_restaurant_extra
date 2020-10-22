# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _get_fields_for_order_line(self):
        res = super(PosOrder, self)._get_fields_for_order_line()
        res.append('price_manually_set')
        return res

class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    price_manually_set = fields.Boolean('Precio Puesto Manualmente')
