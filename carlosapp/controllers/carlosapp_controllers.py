from odoo import http

class Carlosapp(http.Controller):

    @http.route('/motorcycles/',auth="public", website=True)
    def index(self, **kw):
        return"Hello world"
    
    @http.route('/motorcycles/compare/', auth='public', website=True)
    def motorcycles (self,**kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        return http.request.render('carlosapp.motorcycle_website',{
            'motorcycles': motorcycles,
        })
    