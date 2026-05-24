# 💸 Xpense Tracker

A clean, aesthetic expense tracking web app built with **Flask** and **JSON file storage** — no database setup required.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
expense-tracker/
├── app.py              ← Flask routes + JSON file I/O
├── data.json           ← Your expense database (auto-created)
├── requirements.txt
├── static/
│   └── style.css       ← Warm terracotta aesthetic styles
└── templates/
    ├── base.html        ← Shared layout (navbar, alerts)
    ├── index.html       ← Dashboard with summary cards + table
    ├── add_expense.html ← Add new expense form
    └── edit_expense.html← Edit existing expense form
```

---

## ✨ Features

- ➕ Add, edit, and delete expenses
- 🗂️ Categorise expenses (Food, Transport, Shopping, Bills, Health, etc.)
- 📅 Filter by category and month
- 💰 Summary cards showing total and per-category spending
- 💾 All data saved to `data.json` — no database needed
- 🎨 Elegant warm aesthetic with Cormorant Garamond + DM Sans fonts

---

## 🗃️ How Data is Stored

All expenses are stored in `data.json` as a list of objects:

```json
[
    {
        "id": 1,
        "title": "Lunch",
        "amount": 120.0,
        "category": "Food",
        "date": "2026-05-24",
        "note": "Biryani from canteen"
    }
]
```

The app reads and writes this file directly using Python's built-in `json` module — no SQL, no ORM, no setup.

---

## 🛠️ How the JSON I/O Works

```python
# Read all expenses
def read_data():
    with open("data.json", "r") as f:
        return json.load(f)

# Write all expenses back
def write_data(expenses):
    with open("data.json", "w") as f:
        json.dump(expenses, f, indent=4)
```

Every add, edit, or delete reads the file, modifies the list in memory, then writes it back.

---

## 📦 Dependencies

| Package | Purpose        |
|---------|----------------|
| Flask   | Web framework  |

---

## 🔮 Possible Enhancements

- [ ] Monthly spending chart (Chart.js)
- [ ] Export to CSV
- [ ] Budget limit alerts
- [ ] Recurring expenses
- [ ] Multi-currency support
