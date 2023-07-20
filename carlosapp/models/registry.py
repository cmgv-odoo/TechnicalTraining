from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
    _name = 'carlosapp.registry'
    _description = 'Info about carlos app'

    name  = fields.Char(string="Registry Number",required=True,
                        default="MRN0000", copy=False, readonly=True)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model_create_multi
    def create(self, vals_list):
        print("here")
        for vals in vals_list:
            if vals.get('name',('MRN0000')) == ('MRN0000'):
                vals['name'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        for registry in self:
            if re.match(r'^[A-Z]{4}[0-9]{2}[0-9A-Z]{2}[0-9]{6}$', registry.vin) is None:
                raise ValidationError("It must follow the next pattern Make - 2 Capital Letters \nModel - 2 Capital Letters \nYear - 2 Digits \nBattery Capacity - 2 Capital Letters or Numbers \nSerial Number - 6 Digits")


    @api.constrains('license_plate')
    def _check_license(self):
        for registry in self:
            if (re.match(r'[A-Z][A-Z]?[A-Z]?[A-Z]?[0-9][0-9]?[0-9]?[A-Z]?[A-Z]?', registry.license_plate) is None):
                raise ValidationError("1 - 4 Capital Letters \n1 - 3 Digits \nOptional 2 Capital Letters")