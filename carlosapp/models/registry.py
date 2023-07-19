from odoo import api, fields, models

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
        for vals in vals_list:
            if vals.get('name',('MRN0000')) == ('MRN0000'):
                vals['name'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

