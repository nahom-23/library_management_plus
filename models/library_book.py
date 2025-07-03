from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    published_date = fields.Date(string='Published Date')
    price = fields.Float(string='Price')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price_total = fields.Monetary(string='Price + Tax', compute='_compute_price_total')
    loan_ids = fields.One2many('library.loan', 'book_id', string='Loans')

    @api.depends('price')
    def _compute_price_total(self):
        for book in self:
            book.price_total = book.price * 1.15
