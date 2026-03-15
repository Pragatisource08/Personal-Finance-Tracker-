from flask import render_template, Blueprint,request,redirect,url_for,make_response
from app import db
from datetime import datetime
from app.models import Transaction
import csv
import io
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")


@main.route('/add_transaction',methods=['POST'])
def add_transaction():
    date=datetime.now()
    day=datetime.now().strftime("%A")
    expense_purpose=request.form['expense_purpose']
    amount=request.form['amount']
    category=request.form['category']
    user_id=1
    new_transaction = Transaction(
        amount=amount,
        expense_purpose=expense_purpose,
        date=date,
        day=day,
        user_id=user_id,
        category=category
        )    
    db.session.add(new_transaction)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/transaction/delete/<id>', methods=['POST'])
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/transaction')
def get_transaction():
    transactions=Transaction.query.all() 
    return render_template('transactions.html',transactions=transactions)     


@main.route('/expense/<int:month>/<int:year>')
def get_expense(month, year):
     transactions = Transaction.query.filter( 
     db.extract('month', Transaction.date) == month, 
     db.extract('year', Transaction.date) == year 
     ).all() 
     total = sum(t.amount for t in transactions)
     return render_template("expense.html", month=month, year=year,total=total)


@main.route('/export')
def export_csv():
    transactions=Transaction.query.all()
    output=io.StringIO()
    writer=csv.writer(output)
    writer.writerow(['id','amount','expense_purpose','category','day','date'])
    for t in transactions:
        writer.writerow([t.id,t.amount,t.expense_purpose,t.category,t.date,t.day])

    response=make_response(output.getvalue())
    response.headers['Content-Disposition']='attachment; filename=transactions.csv'
    response.headers['Content-Type']='text/csv'
    return response

@main.route('/summary')
def summary():
    return render_template('summary.html')
