# 📚 Library Management Plus - Odoo 17 Custom Module

A fully functional Odoo 17 custom module to manage library books, members, and book loans.

---

## 🚀 Features

- 📖 **Books Management**  
  Create, update, and track books with price, author, published date, and total cost with tax.

- 👤 **Member Management**  
  Manage library members with contact details.

- 🔄 **Book Loan Tracking**  
  Record loans between books and members, with return tracking.

- 🧠 **Computed Fields**  
  Automatically calculates price + tax (15%) for each book.

- 🧩 **Wizards**  
  Modal confirmation dialog with `library.book.confirm` transient model.

- 🛡️ **Access Rights & Menus**  
  Group-level permissions and hierarchical menu structure for ease of use.

---

## 🧱 Technical Stack

- Odoo 17
- Python 3.10+
- PostgreSQL
- XML (for views, actions, menus)
- ORM API: `@api.depends`, One2many/Many2one
- Security: `ir.model.access.csv`

---

## 📂 Module Structure

```
library_management_plus/
├── models/
│   ├── __init__.py
│   ├── library_book.py
│   ├── library_member.py
│   └── library_loan.py
├── views/
│   ├── library_book_views.xml
│   ├── library_member_views.xml
│   ├── library_loan_views.xml
│   └── library_menus.xml
├── wizard/
│   ├── __init__.py
│   └── library_book_confirm.py
├── security/
│   └── ir.model.access.csv
├── __init__.py
├── __manifest__.py
```

---

## 🛠️ Installation Guide

1. Clone or download this repository.

   ```bash
   git clone [https://github.com/nahom-23/library_management_plus.git]
   ```

2. Copy the folder to your Odoo `addons` directory:

   ```
   /odoo/custom/addons/library_management_plus
   ```

3. Restart Odoo and activate Developer Mode.

4. Go to **Apps** and click **Update Apps List**.

5. Search for **Library Management Plus** and install the module.

---

## 🧪 Demo Data

This module does not include demo data. Create records from the UI via the Library > Books / Members / Loans menus.

---

## 🙋‍♂️ Author

**Nahom Birhanu**  


---

⭐️ _Feel free to fork, star, and customize this repo for your own learning or job interview portfolio!_
