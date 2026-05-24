from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

DATA_FILE = "data.json"

# ─── JSON File Helpers ────────────────────────────────────────────────────────

def read_data():
    if not os.path.exists(DATA_FILE):
        write_data([])
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def get_next_id(expenses):
    return max((e["id"] for e in expenses), default=0) + 1

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    expenses = read_data()

    # Filters
    category_filter = request.args.get("category", "")
    month_filter = request.args.get("month", "")

    filtered = expenses
    if category_filter:
        filtered = [e for e in filtered if e["category"] == category_filter]
    if month_filter:
        filtered = [e for e in filtered if e["date"].startswith(month_filter)]

    # Summary
    total = sum(e["amount"] for e in filtered)
    by_category = {}
    for e in filtered:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]

    categories = sorted(set(e["category"] for e in expenses))

    return render_template(
        "index.html",
        expenses=sorted(filtered, key=lambda x: x["date"], reverse=True),
        total=total,
        by_category=by_category,
        categories=categories,
        category_filter=category_filter,
        month_filter=month_filter,
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        title    = request.form.get("title", "").strip()
        amount   = request.form.get("amount", "").strip()
        category = request.form.get("category", "").strip()
        date     = request.form.get("date", "").strip()
        note     = request.form.get("note", "").strip()

        if not title or not amount or not category or not date:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("add_expense"))

        try:
            amount = float(amount)
        except ValueError:
            flash("Amount must be a number.", "error")
            return redirect(url_for("add_expense"))

        expenses = read_data()
        expenses.append({
            "id":       get_next_id(expenses),
            "title":    title,
            "amount":   amount,
            "category": category,
            "date":     date,
            "note":     note,
        })
        write_data(expenses)
        flash("Expense added!", "success")
        return redirect(url_for("index"))

    return render_template("add_expense.html", today=datetime.today().strftime("%Y-%m-%d"))


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expenses = read_data()
    expense = next((e for e in expenses if e["id"] == expense_id), None)

    if not expense:
        flash("Expense not found.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        expense["title"]    = request.form.get("title", "").strip()
        expense["category"] = request.form.get("category", "").strip()
        expense["date"]     = request.form.get("date", "").strip()
        expense["note"]     = request.form.get("note", "").strip()
        try:
            expense["amount"] = float(request.form.get("amount", 0))
        except ValueError:
            flash("Amount must be a number.", "error")
            return redirect(url_for("edit_expense", expense_id=expense_id))

        write_data(expenses)
        flash("Expense updated!", "success")
        return redirect(url_for("index"))

    return render_template("edit_expense.html", expense=expense)


@app.route("/delete/<int:expense_id>")
def delete_expense(expense_id):
    expenses = read_data()
    expenses = [e for e in expenses if e["id"] != expense_id]
    write_data(expenses)
    flash("Expense deleted.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
