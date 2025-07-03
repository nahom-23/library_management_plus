from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    loan_ids = fields.One2many('library.loan', 'member_id', string='Loans')
