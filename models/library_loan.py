from odoo import models, fields
from datetime import date

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Book Loan'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('library.member', string='Member', required=True)
    loan_date = fields.Date(string='Loan Date', default=fields.Date.context_today)
    return_date = fields.Date(string='Return Date')
    is_returned = fields.Boolean(string='Returned', default=False)
