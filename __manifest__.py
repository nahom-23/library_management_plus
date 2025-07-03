{
    "name": "Library Management",
    "version": "2.0",
    "category": "Productivity",
    "summary": "Enhanced Library Management System",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
        "views/library_member_views.xml",
        "views/library_loan_views.xml",
        "views/library_menus.xml",
        "wizard/library_book_confirm_wizard.xml"
    ],
    "installable": True,
    "application": True
}
