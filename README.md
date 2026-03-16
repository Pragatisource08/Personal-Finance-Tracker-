💰 Track Your Finances

A simple personal finance tracker web app that helps you log and monitor your daily expenses — cleaner and simpler than Excel.

## Features
- Add and delete expense transactions
- Categorize expenses (Food, Travel, Rent, Shopping, etc.)
- View monthly expense summary
- Visual spending breakdown by category (Chart.js)
- Export transactions to CSV

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Jinja2, Chart.js |
| Backend | Python, Flask |
| Database | SQLite + SQLAlchemy |

## How to Run Locally

1. Clone the repository

   git clone https://github.com/Pragatisource08/Personal-Finance-Tracker.git
   cd Personal-Finance-Tracker

2. Create and activate virtual environment

   python -m venv venv
   venv\Scripts\activate

3. Install dependencies

   pip install -r requirements.txt

4. Create a `.env` file

   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///finance.db

5. Run the app

   python run.py

6. Visit `http://127.0.0.1:5000`

## Project Structure

app/
├── __init__.py
├── models.py
├── routes.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── transactions.html
    ├── expense.html
    └── summary.html
config.py
run.py