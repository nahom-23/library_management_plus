from odoo import models, fields

class LibraryBookConfirm(models.TransientModel):
    _name = 'library.book.confirm'
    _description = 'Confirm Book Details'

    confirm_note = fields.Text(string="Confirmation Note")

    def confirm_book_action(self):
        return {'type': 'ir.actions.act_window_close'}
