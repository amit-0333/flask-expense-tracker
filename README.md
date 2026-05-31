<div align="center">

```text
██╗  ██╗██████╗ ███████╗███╗   ██╗███████╗███████╗
╚██╗██╔╝██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝
 ╚███╔╝ ██████╔╝█████╗  ██╔██╗ ██║███████╗█████╗
 ██╔██╗ ██╔═══╝ ██╔══╝  ██║╚██╗██║╚════██║██╔══╝
██╔╝ ██╗██║     ███████╗██║ ╚████║███████║███████╗
╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝

████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

### 💸 Xpense Tracker

> A clean and aesthetic expense tracking web application built using Flask and JSON storage. Manage expenses, track spending habits, and organize finances without requiring a database setup.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge\&logo=flask)
![JSON](https://img.shields.io/badge/Database-JSON-lightgrey?style=for-the-badge)
![HTML](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

# 📌 About

Xpense Tracker is a full-stack expense management application built using Flask and file-based JSON storage.

The application helps users:

* 💸 Track daily expenses
* 📊 Monitor spending patterns
* 🗂️ Categorize transactions
* 📅 Filter expenses by month and category
* 💾 Store data locally without a database

The project demonstrates CRUD operations, server-side rendering, file handling, and responsive UI design using Flask.

---

# ✨ Features

| Feature                 | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| ➕ Add Expense           | Record a new expense with title, amount, category, and notes |
| ✏️ Edit Expense         | Modify existing expense records                              |
| 🗑️ Delete Expense      | Remove unwanted transactions                                 |
| 🗂️ Category Management | Organize expenses into categories                            |
| 📅 Monthly Filtering    | View expenses for specific months                            |
| 💰 Spending Summary     | Dashboard cards showing total expenditure                    |
| 💾 JSON Storage         | Lightweight database-free persistence                        |
| 🎨 Modern UI            | Elegant warm-themed interface                                |

---

# 🛠️ Tech Stack

| Technology      | Usage               |
| --------------- | ------------------- |
| 🐍 Python       | Backend Development |
| 🌶️ Flask       | Web Framework       |
| 📄 JSON         | Local Data Storage  |
| 🎨 HTML/CSS     | Frontend Interface  |
| 🔧 Git & GitHub | Version Control     |

---

# 📚 Concepts Implemented

| Concept             | Status  |
| ------------------- | ------- |
| Flask Routing       | 🟢 Done |
| CRUD Operations     | 🟢 Done |
| File Handling       | 🟢 Done |
| JSON Storage        | 🟢 Done |
| Form Processing     | 🟢 Done |
| Template Rendering  | 🟢 Done |
| Expense Filtering   | 🟢 Done |
| Dashboard Analytics | 🟢 Done |

---

# 🗂️ Project Structure

```bash
Xpense-Tracker/
│
├── 📄 app.py
│   └── Flask Routes & Business Logic
│
├── 📄 data.json
│   └── Expense Database
│
├── 📄 requirements.txt
│
├── 📂 static/
│   └── style.css
│
├── 📂 templates/
│   ├── base.html
│   ├── index.html
│   ├── add_expense.html
│   └── edit_expense.html
│
└── 📄 README.md
```

---

# ⚙️ How to Run

```bash
# Clone Repository
git clone https://github.com/amit-0333/Xpense-Tracker.git

# Navigate into project
cd Xpense-Tracker

# Install dependencies
pip install -r requirements.txt

# Run Flask application
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🎯 Application Workflow

```text
User Action
     │
     ▼
Flask Routes
     │
     ▼
Read data.json
     │
     ▼
Add / Edit / Delete
     │
     ▼
Update Expense List
     │
     ▼
Write Back to JSON
     │
     ▼
Render Updated Dashboard
```

---

# 💰 Expense Data Format

Each expense is stored as a JSON object:

```json
{
    "id": 1,
    "title": "Lunch",
    "amount": 120.0,
    "category": "Food",
    "date": "2026-05-24",
    "note": "Biryani from canteen"
}
```

---

# 🎯 Learning Outcomes

* [x] Build complete Flask applications
* [x] Implement CRUD functionality
* [x] Work with JSON as a lightweight database
* [x] Handle forms and user input
* [x] Design responsive web interfaces
* [x] Structure Flask projects professionally
* [x] Implement filtering and summary analytics
* [ ] Add authentication system
* [ ] Deploy to cloud platform

---

# 🔮 Future Improvements

* [ ] Interactive Charts using Chart.js
* [ ] Export Expenses to CSV
* [ ] Budget Limit Notifications
* [ ] Recurring Expense Tracking
* [ ] User Authentication
* [ ] Multi-Currency Support
* [ ] Expense Search Functionality
* [ ] Dark Mode Support

---

# 🙏 Acknowledgements

This project was built to strengthen practical knowledge of:

* Flask Development
* CRUD Operations
* JSON File Handling
* Web Application Architecture
* Expense Management Systems

---

# 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat\&logo=github)](https://github.com/amit-0333)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat\&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)

[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat\&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

<div align="center">

### ⭐ Star this repository if you found it useful!

💸 Track smarter. Spend better. Save more.

</div>
