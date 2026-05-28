A full stack finance management application buit with pyrhon streamlit and MongoDB

**Project Title**
**Expense Tracking System**
> _"Track every rupee. Control every decision."_

---

## 📖 About the Project

The **Expense Tracking System** is a web-based personal finance application that enables users to record, monitor, analyze, and manage their daily expenses and income. Built using **Python Streamlit** for the front-end and **MongoDB** as the back-end database, this application provides a seamless, real-time financial dashboard.

The system allows users to:
- Add and categorize income and expenses
- View monthly/weekly spending summaries
- Analyze spending trends through interactive charts
- Set budgets and receive overspending alerts
- Filter, search, and export transaction history

This project was developed as a full-stack solution demonstrating the integration of a reactive Python UI framework with a NoSQL document database, making it both scalable and easy to maintain.

---

## 🎯 Purpose / Advantages / Applications

### 🔵 Purpose
Managing personal finances is a challenge for millions of people. This system provides a **simple, intuitive interface** to help individuals:
- Keep track of where their money is going
- Identify unnecessary spending habits
- Plan budgets effectively
- Make informed financial decisions

### ✅ Advantages

| Advantage | Description |
|-----------|-------------|
| 📊 **Visual Analytics** | Interactive charts and graphs for spending insights |
| 🗂️ **Category Management** | Organize expenses into Food, Transport, Bills, Health, etc. |
| ⚡ **Real-time Updates** | Streamlit re-renders UI instantly on data changes |
| 🔒 **Secure Storage** | MongoDB stores data persistently and securely |
| 🌐 **Web-based** | Accessible from any browser, no installation needed by end users |
| 📱 **Responsive UI** | Works on desktop and mobile browsers |
| 📤 **Data Export** | Download expense reports as CSV |
| 🔔 **Budget Alerts** | Notifies when spending exceeds set limits |

### 🏭 Applications

- **Personal Finance Management** — Track daily household expenses
- **Student Budget Planner** — Monitor hostel and college expenses
- **Small Business Bookkeeping** — Record petty cash and daily transactions
- **Family Expense Manager** — Shared family financial tracking
- **Freelancer Income/Expense Tracker** — Track project earnings and deductions

---

## 🛠️ Tech Stack

### 🎨 Front-End Technologies

#### i) Python Streamlit

| Component | Details |
|-----------|---------|
| **Framework** | Streamlit 1.x |
| **Language** | Python 3.9+ |
| **UI Components** | st.sidebar, st.columns, st.metric, st.dataframe, st.plotly_chart |
| **Charts** | Plotly Express (bar, pie, line charts) |
| **Forms** | st.form, st.selectbox, st.date_input, st.number_input |
| **State Management** | st.session_state |

**Why Streamlit?**
- Zero HTML/CSS/JS needed — pure Python
- Rapid prototyping and deployment
- Built-in widgets (sliders, date pickers, file uploaders)
- Auto-reloading on code changes
- Easy integration with data science libraries (Pandas, Plotly)

---

### 🗄️ Back-End Technologies

#### i) MongoDB

| Component | Details |
|-----------|---------|
| **Database** | MongoDB (NoSQL, Document-based) |
| **Driver** | PyMongo 4.x |
| **Hosting** | MongoDB Atlas (Cloud) or Local MongoDB |
| **Collections** | `users`, `transactions`, `categories`, `budgets` |
| **Query Language** | MongoDB Query Language (MQL) |
| **Indexing** | Indexed on `user_id`, `date`, `category` |

**Why MongoDB?**
- Flexible schema — easy to add fields without migration
- JSON-like documents match Python dictionaries perfectly
- Horizontal scalability for large datasets
- Rich query capabilities with aggregation pipelines
- Free tier available on MongoDB Atlas

---

## 📐 E-R Diagram (Entity-Relationship Diagram)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        E-R DIAGRAM — EXPENSE TRACKING SYSTEM                │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐          ┌───────────────────┐          ┌────────────────┐
  │    USERS     │          │   TRANSACTIONS    │          │   CATEGORIES   │
  ├──────────────┤          ├───────────────────┤          ├────────────────┤
  │ _id (PK)     │──────┐   │ _id (PK)          │   ┌──────│ _id (PK)       │
  │ username     │      └──▶│ user_id (FK)      │   │      │ name           │
  │ email        │          │ category_id (FK)  │◀──┘      │ type           │
  │ password     │          │ amount            │          │ icon           │
  │ created_at   │          │ type (income/exp) │          │ color          │
  │ profile_pic  │          │ description       │          └────────────────┘
  └──────────────┘          │ date              │
          │                 │ payment_method    │          ┌────────────────┐
          │                 │ receipt_img       │          │    BUDGETS     │
          │                 └───────────────────┘          ├────────────────┤
          └────────────────────────────────────────────────│ _id (PK)       │
                                                          │ user_id (FK)   │
                                                          │ category_id    │
                                                          │ limit_amount   │
                                                          │ month          │
                                                          │ year           │
                                                          │ spent_amount   │
                                                          └────────────────┘

  RELATIONSHIPS:
  ┌─────────────────────────────────────────────────────────┐
  │  USER         ──< TRANSACTIONS  (One-to-Many)           │
  │  USER         ──< BUDGETS       (One-to-Many)           │
  │  CATEGORY     ──< TRANSACTIONS  (One-to-Many)           │
  │  CATEGORY     ──< BUDGETS       (One-to-Many)           │
  └─────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram (DFD)

### Level 0 — Context Diagram
```
                        ┌───────────────────────────────┐
                        │                               │
   User Input ─────────▶│   EXPENSE TRACKING SYSTEM    │─────────▶ Reports/Dashboard
                        │                               │
   Login/Register ─────▶│                               │─────────▶ Alerts/Notifications
                        └───────────────────────────────┘
```

### Level 1 — DFD
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LEVEL 1 DATA FLOW DIAGRAM                          │
└─────────────────────────────────────────────────────────────────────────────┘

         ┌──────────┐
         │  USER    │
         └────┬─────┘
              │
    ┌─────────▼──────────┐        ┌──────────────────┐
    │  1.0 AUTHENTICATE  │◀──────▶│   USERS Collection│
    │  (Login/Register)  │        │   (MongoDB)       │
    └─────────┬──────────┘        └──────────────────┘
              │ Valid Session
              │
    ┌─────────▼──────────────────────────────────────────┐
    │                  STREAMLIT DASHBOARD                 │
    │  ┌───────────────┐    ┌────────────────────────┐   │
    │  │ 2.0 ADD       │    │ 3.0 VIEW TRANSACTIONS  │   │
    │  │ TRANSACTION   │    │ (Filter, Search, Sort) │   │
    │  └──────┬────────┘    └──────────┬─────────────┘   │
    │         │                        │                  │
    │  ┌──────▼────────┐    ┌──────────▼─────────────┐   │
    │  │ 4.0 BUDGET    │    │ 5.0 ANALYTICS          │   │
    │  │ MANAGEMENT    │    │ (Charts & Reports)     │   │
    │  └──────┬────────┘    └──────────┬─────────────┘   │
    └─────────┼────────────────────────┼─────────────────┘
              │                        │
              ▼                        ▼
    ┌──────────────────────────────────────────────┐
    │            MONGODB DATABASE                  │
    │  ┌──────────────┐  ┌────────────────────┐   │
    │  │ transactions │  │     budgets        │   │
    │  │ collection   │  │     collection     │   │
    │  └──────────────┘  └────────────────────┘   │
    │  ┌──────────────┐  ┌────────────────────┐   │
    │  │  categories  │  │       users        │   │
    │  │  collection  │  │     collection     │   │
    │  └──────────────┘  └────────────────────┘   │
    └──────────────────────────────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ 6.0 EXPORT / REPORT │──▶  CSV Download / PDF
    └─────────────────────┘

  DATA FLOWS:
  ──────────────────────────────────────────────────
  User ──▶ 1.0: credentials (username, password)
  1.0 ──▶ DB: query user record
  DB  ──▶ 1.0: user data / auth token
  User ──▶ 2.0: transaction (amount, category, date, type)
  2.0 ──▶ DB: INSERT transaction document
  DB  ──▶ 3.0: READ all transactions for user
  3.0 ──▶ 5.0: filtered data for charts
  5.0 ──▶ User: visual charts (pie, bar, line)
  User ──▶ 4.0: budget limit per category
  4.0 ──▶ DB: UPSERT budget document
  DB  ──▶ 4.0: current spent vs limit
  4.0 ──▶ User: alert if overspent
```

---

## 🖥️ Running Project Screenshots

> The following describes the screens of the running application:

### Screen 1 — Login / Register Page
```
┌─────────────────────────────────────────────────┐
│  💸 Expense Tracker                             │
│  ─────────────────────────────────────────────  │
│  Welcome Back!                                  │
│                                                 │
│  Username:  [_________________________]         │
│  Password:  [_________________________]         │
│                                                 │
│  [    LOGIN    ]   [   REGISTER   ]             │
└─────────────────────────────────────────────────┘
```

### Screen 2 — Dashboard (Home)
```
┌─────────────────────────────────────────────────────────────────┐
│ 💸 Expense Tracker         |  👤 John Doe     [Logout]          │
│─────────────────────────────────────────────────────────────────│
│ 📊 May 2026 Summary                                             │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│ │ Total Income │  │Total Expense │  │   Balance    │           │
│ │  ₹45,000     │  │  ₹28,500     │  │  ₹16,500     │           │
│ └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                  │
│  [Pie Chart: Expense by Category]  [Bar Chart: Monthly Trend]   │
│                                                                  │
│  Recent Transactions                                            │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ 26 May  │ 🍕 Food        │ -₹450   │ Zomato Order      │    │
│  │ 25 May  │ 🚌 Transport   │ -₹120   │ Auto Rickshaw     │    │
│  │ 25 May  │ 💰 Salary      │ +₹45000 │ Monthly Salary    │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### Screen 3 — Add Transaction
```
┌─────────────────────────────────────────────┐
│  ➕ Add New Transaction                      │
│  ──────────────────────────────────────────  │
│  Type:      [● Expense  ○ Income]            │
│  Amount:    [  1200  ] ₹                    │
│  Category:  [ Food & Dining  ▼ ]            │
│  Date:      [ 27/05/2026     ]              │
│  Payment:   [ UPI            ▼ ]            │
│  Note:      [ Dinner at restaurant ]        │
│                                              │
│            [ ✅ Add Transaction ]            │
└─────────────────────────────────────────────┘
```

### Screen 4 — Budget Manager
```
┌──────────────────────────────────────────────────────┐
│  🎯 Budget Manager — May 2026                        │
│  ────────────────────────────────────────────────── │
│  Food & Dining                                       │
│  ████████████░░░░░░  ₹4,200 / ₹6,000  (70%)         │
│                                                      │
│  Transport                                           │
│  ██████████████████  ₹3,500 / ₹3,000  ⚠️ OVERSPENT  │
│                                                      │
│  Entertainment                                       │
│  ████░░░░░░░░░░░░░░  ₹800 / ₹2,000   (40%)          │
└──────────────────────────────────────────────────────┘
```

### Screen 5 — Analytics
```
┌──────────────────────────────────────────────────────────┐
│  📈 Analytics & Reports                                  │
│  ──────────────────────────────────────────────────────  │
│                                                          │
│  Filter: [Jan ▼] to [May ▼] [2026 ▼]  [Apply]          │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Monthly Income vs Expense (Bar Chart)    │   │
│  │  ██ Income  ██ Expense                           │   │
│  │  Jan  Feb  Mar  Apr  May                        │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Spending by Category (Pie Chart)         │   │
│  │  🟢 Food 35%  🔵 Transport 20%  🟡 Bills 25%    │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  [ 📥 Download CSV Report ]                             │
└──────────────────────────────────────────────────────────┘
```

---

## 💻 All Source Code

### 📁 Project Structure
```
expense-tracking-system/
│
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (MongoDB URI)
├── .gitignore
│
├── database/
│   └── db.py               # MongoDB connection and helper functions
│
├── pages/
│   ├── dashboard.py        # Dashboard/home page
│   ├── add_transaction.py  # Add income/expense form
│   ├── transactions.py     # View/filter all transactions
│   ├── budget.py           # Budget setting and tracking
│   └── analytics.py        # Charts and reports
│
├── models/
│   ├── user.py             # User model
│   ├── transaction.py      # Transaction model
│   └── budget.py           # Budget model
│
└── utils/
    ├── auth.py             # Login/register logic
    ├── charts.py           # Plotly chart helpers
    └── helpers.py          # Date, formatting utilities
```

---

### 📄 `requirements.txt`
```txt
streamlit==1.32.0
pymongo==4.6.1
python-dotenv==1.0.0
plotly==5.19.0
pandas==2.2.0
bcrypt==4.1.2
Pillow==10.2.0
```

---

### 📄 `.env`
```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/expense_tracker
DB_NAME=expense_tracker
SECRET_KEY=your_secret_key_here
```

---

### 📄 `database/db.py` — MongoDB Connection
```python
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "expense_tracker")

client = None

def get_db():
    global client
    if client is None:
        client = MongoClient(MONGO_URI)
    return client[DB_NAME]

def get_collection(collection_name: str):
    db = get_db()
    return db[collection_name]
```

---

### 📄 `utils/auth.py` — Authentication
```python
import bcrypt
import streamlit as st
from database.db import get_collection
from datetime import datetime

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(username: str, email: str, password: str) -> dict:
    users = get_collection("users")
    if users.find_one({"email": email}):
        return {"success": False, "message": "Email already registered."}
    
    user = {
        "username": username,
        "email": email,
        "password": hash_password(password),
        "created_at": datetime.utcnow()
    }
    result = users.insert_one(user)
    return {"success": True, "user_id": str(result.inserted_id)}

def login_user(email: str, password: str) -> dict:
    users = get_collection("users")
    user = users.find_one({"email": email})
    if not user:
        return {"success": False, "message": "User not found."}
    if not verify_password(password, user["password"]):
        return {"success": False, "message": "Invalid password."}
    return {"success": True, "user": user}

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
```

---

### 📄 `models/transaction.py` — Transaction Model
```python
from database.db import get_collection
from bson import ObjectId
from datetime import datetime

def add_transaction(user_id: str, data: dict) -> dict:
    transactions = get_collection("transactions")
    doc = {
        "user_id": user_id,
        "type": data["type"],           # "income" or "expense"
        "amount": float(data["amount"]),
        "category": data["category"],
        "description": data.get("description", ""),
        "payment_method": data.get("payment_method", "Cash"),
        "date": data["date"],
        "created_at": datetime.utcnow()
    }
    result = transactions.insert_one(doc)
    return {"success": True, "id": str(result.inserted_id)}

def get_transactions(user_id: str, filters: dict = {}) -> list:
    transactions = get_collection("transactions")
    query = {"user_id": user_id}
    if filters.get("type"):
        query["type"] = filters["type"]
    if filters.get("category"):
        query["category"] = filters["category"]
    if filters.get("start_date") and filters.get("end_date"):
        query["date"] = {
            "$gte": filters["start_date"],
            "$lte": filters["end_date"]
        }
    return list(transactions.find(query).sort("date", -1))

def delete_transaction(transaction_id: str) -> bool:
    transactions = get_collection("transactions")
    result = transactions.delete_one({"_id": ObjectId(transaction_id)})
    return result.deleted_count > 0

def get_monthly_summary(user_id: str, month: int, year: int) -> dict:
    transactions = get_collection("transactions")
    pipeline = [
        {"$match": {
            "user_id": user_id,
            "$expr": {
                "$and": [
                    {"$eq": [{"$month": "$date"}, month]},
                    {"$eq": [{"$year": "$date"}, year]}
                ]
            }
        }},
        {"$group": {
            "_id": "$type",
            "total": {"$sum": "$amount"}
        }}
    ]
    results = list(transactions.aggregate(pipeline))
    summary = {"income": 0, "expense": 0}
    for r in results:
        summary[r["_id"]] = r["total"]
    summary["balance"] = summary["income"] - summary["expense"]
    return summary
```

---

### 📄 `models/budget.py` — Budget Model
```python
from database.db import get_collection
from datetime import datetime

def set_budget(user_id: str, category: str, limit: float, month: int, year: int):
    budgets = get_collection("budgets")
    budgets.update_one(
        {"user_id": user_id, "category": category, "month": month, "year": year},
        {"$set": {"limit_amount": limit, "updated_at": datetime.utcnow()}},
        upsert=True
    )

def get_budgets(user_id: str, month: int, year: int) -> list:
    budgets = get_collection("budgets")
    transactions = get_collection("transactions")
    budget_list = list(budgets.find({"user_id": user_id, "month": month, "year": year}))
    
    for budget in budget_list:
        # Calculate spent amount for this category/month
        pipeline = [
            {"$match": {
                "user_id": user_id,
                "category": budget["category"],
                "type": "expense",
                "$expr": {
                    "$and": [
                        {"$eq": [{"$month": "$date"}, month]},
                        {"$eq": [{"$year": "$date"}, year]}
                    ]
                }
            }},
            {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
        ]
        result = list(transactions.aggregate(pipeline))
        budget["spent"] = result[0]["total"] if result else 0
        budget["remaining"] = budget["limit_amount"] - budget["spent"]
        budget["percent"] = (budget["spent"] / budget["limit_amount"] * 100) if budget["limit_amount"] > 0 else 0
    
    return budget_list
```

---

### 📄 `utils/charts.py` — Chart Helpers
```python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def pie_chart_by_category(transactions: list) -> go.Figure:
    if not transactions:
        return go.Figure()
    df = pd.DataFrame(transactions)
    df = df[df["type"] == "expense"]
    category_totals = df.groupby("category")["amount"].sum().reset_index()
    fig = px.pie(
        category_totals,
        names="category",
        values="amount",
        title="Spending by Category",
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig

def monthly_bar_chart(transactions: list) -> go.Figure:
    if not transactions:
        return go.Figure()
    df = pd.DataFrame(transactions)
    df["month"] = pd.to_datetime(df["date"]).dt.strftime("%b %Y")
    monthly = df.groupby(["month", "type"])["amount"].sum().reset_index()
    fig = px.bar(
        monthly, x="month", y="amount", color="type",
        barmode="group",
        title="Monthly Income vs Expense",
        color_discrete_map={"income": "#4CAF50", "expense": "#F44336"}
    )
    return fig

def line_chart_trend(transactions: list) -> go.Figure:
    if not transactions:
        return go.Figure()
    df = pd.DataFrame(transactions)
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["type"] == "expense"].sort_values("date")
    df["cumulative"] = df["amount"].cumsum()
    fig = px.line(df, x="date", y="cumulative", title="Cumulative Spending Trend")
    fig.update_traces(line_color="#FF6B35", line_width=2)
    return fig
```

---

### 📄 `app.py` — Main Entry Point
```python
import streamlit as st
from utils.auth import login_user, register_user, logout
from pages import dashboard, add_transaction, transactions, budget, analytics

st.set_page_config(
    page_title="💸 Expense Tracker",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-card {
        background: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def show_login():
    st.markdown('<div class="main-header">💸 Expense Tracking System</div>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
    
    with tab1:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                result = login_user(email, password)
                if result["success"]:
                    st.session_state["user"] = result["user"]
                    st.session_state["user_id"] = str(result["user"]["_id"])
                    st.rerun()
                else:
                    st.error(result["message"])
    
    with tab2:
        with st.form("register_form"):
            username = st.text_input("Full Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Register")
            if submitted:
                if password != confirm:
                    st.error("Passwords do not match!")
                else:
                    result = register_user(username, email, password)
                    if result["success"]:
                        st.success("Registration successful! Please login.")
                    else:
                        st.error(result["message"])

def show_main_app():
    user = st.session_state["user"]
    
    with st.sidebar:
        st.markdown(f"### 👤 {user['username']}")
        st.divider()
        page = st.radio(
            "Navigation",
            ["📊 Dashboard", "➕ Add Transaction", "📋 All Transactions",
             "🎯 Budget Manager", "📈 Analytics"],
            label_visibility="collapsed"
        )
        st.divider()
        if st.button("🚪 Logout"):
            logout()
    
    if page == "📊 Dashboard":
        dashboard.show()
    elif page == "➕ Add Transaction":
        add_transaction.show()
    elif page == "📋 All Transactions":
        transactions.show()
    elif page == "🎯 Budget Manager":
        budget.show()
    elif page == "📈 Analytics":
        analytics.show()

# Main router
if "user" not in st.session_state:
    show_login()
else:
    show_main_app()
```

---

### 📄 `pages/dashboard.py` — Dashboard Page
```python
import streamlit as st
from datetime import datetime
from models.transaction import get_transactions, get_monthly_summary
from utils.charts import pie_chart_by_category, monthly_bar_chart

def show():
    st.title("📊 Dashboard")
    user_id = st.session_state["user_id"]
    now = datetime.now()
    
    # Monthly Summary Cards
    summary = get_monthly_summary(user_id, now.month, now.year)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💰 Total Income", f"₹{summary['income']:,.2f}", delta=None)
    with col2:
        st.metric("💸 Total Expense", f"₹{summary['expense']:,.2f}", delta=None)
    with col3:
        balance = summary['balance']
        st.metric("🏦 Balance", f"₹{balance:,.2f}",
                  delta="Surplus" if balance >= 0 else "Deficit",
                  delta_color="normal" if balance >= 0 else "inverse")
    
    st.divider()
    
    # Charts
    transactions = get_transactions(user_id)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(pie_chart_by_category(transactions), use_container_width=True)
    with col2:
        st.plotly_chart(monthly_bar_chart(transactions), use_container_width=True)
    
    st.divider()
    
    # Recent Transactions
    st.subheader("🕒 Recent Transactions")
    recent = get_transactions(user_id)[:10]
    if recent:
        for t in recent:
            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write(str(t["date"])[:10])
            with col2:
                st.write(f"{'🏷️'} {t['category']} — {t.get('description', '')}")
            with col3:
                color = "🟢" if t["type"] == "income" else "🔴"
                sign = "+" if t["type"] == "income" else "-"
                st.write(f"{color} {sign}₹{t['amount']:,.0f}")
    else:
        st.info("No transactions yet. Add your first transaction!")
```

---

### 📄 `pages/add_transaction.py` — Add Transaction Page
```python
import streamlit as st
from datetime import date
from models.transaction import add_transaction

CATEGORIES = {
    "expense": ["Food & Dining", "Transport", "Shopping", "Bills & Utilities",
                "Health & Medical", "Entertainment", "Education", "Other"],
    "income": ["Salary", "Freelance", "Business", "Investment", "Gift", "Other"]
}

PAYMENT_METHODS = ["Cash", "UPI", "Credit Card", "Debit Card", "Net Banking", "Cheque"]

def show():
    st.title("➕ Add New Transaction")
    user_id = st.session_state["user_id"]
    
    with st.form("transaction_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            t_type = st.radio("Transaction Type", ["expense", "income"],
                              format_func=lambda x: "💸 Expense" if x == "expense" else "💰 Income",
                              horizontal=True)
        with col2:
            amount = st.number_input("Amount (₹)", min_value=0.01, step=0.01, format="%.2f")
        
        col3, col4 = st.columns(2)
        with col3:
            category = st.selectbox("Category", CATEGORIES[t_type])
        with col4:
            payment = st.selectbox("Payment Method", PAYMENT_METHODS)
        
        t_date = st.date_input("Date", value=date.today())
        description = st.text_input("Description / Note (optional)")
        
        submitted = st.form_submit_button("✅ Add Transaction", use_container_width=True)
        
        if submitted:
            if amount <= 0:
                st.error("Amount must be greater than 0.")
            else:
                data = {
                    "type": t_type,
                    "amount": amount,
                    "category": category,
                    "payment_method": payment,
                    "date": t_date,
                    "description": description
                }
                result = add_transaction(user_id, data)
                if result["success"]:
                    st.success(f"✅ Transaction added successfully!")
                    st.balloons()
                else:
                    st.error("Failed to add transaction. Please try again.")
```

---

### 📄 `pages/analytics.py` — Analytics Page
```python
import streamlit as st
import pandas as pd
from models.transaction import get_transactions
from utils.charts import pie_chart_by_category, monthly_bar_chart, line_chart_trend
from datetime import datetime

def show():
    st.title("📈 Analytics & Reports")
    user_id = st.session_state["user_id"]
    
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("From Date", value=datetime(datetime.now().year, 1, 1))
    with col2:
        end_date = st.date_input("To Date", value=datetime.now())
    
    filters = {"start_date": start_date, "end_date": end_date}
    transactions = get_transactions(user_id, filters)
    
    if not transactions:
        st.warning("No transactions found for the selected period.")
        return
    
    df = pd.DataFrame(transactions)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(pie_chart_by_category(transactions), use_container_width=True)
    with col2:
        st.plotly_chart(monthly_bar_chart(transactions), use_container_width=True)
    
    st.plotly_chart(line_chart_trend(transactions), use_container_width=True)
    
    # Category-wise breakdown table
    st.subheader("📋 Category-wise Breakdown")
    expense_df = df[df["type"] == "expense"].groupby("category")["amount"].agg(["sum", "count"]).reset_index()
    expense_df.columns = ["Category", "Total Spent (₹)", "No. of Transactions"]
    expense_df = expense_df.sort_values("Total Spent (₹)", ascending=False)
    st.dataframe(expense_df, use_container_width=True)
    
    # Download CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Report as CSV",
        data=csv,
        file_name=f"expense_report_{start_date}_to_{end_date}.csv",
        mime="text/csv",
        use_container_width=True
    )
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- MongoDB Atlas account (free) or local MongoDB installation
- Git

### Installation

**Step 1: Clone the repository**
```bash
git clone https://github.com/your-username/expense-tracking-system.git
cd expense-tracking-system
```

**Step 2: Create a virtual environment**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure MongoDB**
1. Create a free account at [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a new cluster
3. Get your connection string
4. Create `.env` file:
```env
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/expense_tracker
DB_NAME=expense_tracker
```

**Step 5: Run the application**
```bash
streamlit run app.py
```

**Step 6: Open in browser**
```
http://localhost:8501
```

---

## 🌐 URL / Deployment

### Local URL
```
http://localhost:8501
```

### Deploy to Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file as `app.py`
5. Add your environment secrets (MongoDB URI)
6. Click **Deploy**

Your app will be live at:
```
https://your-app-name.streamlit.app
```

### Alternative Deployment Options
| Platform | URL Pattern |
|----------|------------|
| Streamlit Cloud | `https://your-app.streamlit.app` |
| Railway | `https://your-app.railway.app` |
| Render | `https://your-app.onrender.com` |
| Heroku | `https://your-app.herokuapp.com` |

---

## 📊 MongoDB Collections Schema

### `users` Collection
```json
{
  "_id": "ObjectId",
  "username": "John Doe",
  "email": "john@example.com",
  "password": "$2b$12$hashed_password",
  "created_at": "2026-01-01T00:00:00Z"
}
```

### `transactions` Collection
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "type": "expense",
  "amount": 450.00,
  "category": "Food & Dining",
  "description": "Dinner at restaurant",
  "payment_method": "UPI",
  "date": "2026-05-27",
  "created_at": "2026-05-27T19:30:00Z"
}
```

### `budgets` Collection
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "category": "Food & Dining",
  "limit_amount": 6000.00,
  "month": 5,
  "year": 2026,
  "updated_at": "2026-05-01T00:00:00Z"
}
```

### `categories` Collection
```json
{
  "_id": "ObjectId",
  "name": "Food & Dining",
  "type": "expense",
  "icon": "🍕",
  "color": "#FF6B6B"
}
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your-email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)

---

## 🙏 Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io)
- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [PyMongo Documentation](https://pymongo.readthedocs.io)

---

<div align="center">
  <p>Made with ❤️ using Python Streamlit & MongoDB</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>

