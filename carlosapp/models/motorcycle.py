from odoo import models, fields, api

class Motorcycle(models.Model):
    _inherit = "product.template"

    name = fields.Char()
    horsepower = fields.Char()
    top_speed = fields.Char()
    torque = fields.Char()
    battery_capacity = fields.Char()
    charge_time = fields.Char()
    range = fields.Char()
    curb_weight = fields.Char()
    make = fields.Char()
    model = fields.Char()

    detailed_type = fields.Selection(selection_add=[
    ('motorcycle', 'Motorcycle'),
    ], ondelete={'motorcycle': 'set product'})
    
    type = fields.Selection(selection_add=[
    ('motorcycle', 'Motorcycle'),
    ], ondelete={'motorcycle': 'set product'})

    
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping