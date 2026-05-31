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

## 🌐 Live Demo

[![Open Website](https://img.shields.io/badge/🚀_Live_Demo-Visit_Now-blue?style=for-the-badge)](https://expense-tracking-system-website.streamlit.app/)


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
  │ username     │      └──▶│ user_id (FK)           │ name          │
  │ email        │           │ category_id (FK)      │◀──┘      │ type           │
  │ password     │           │ amount            │     │ icon         │
  │ created_at   │           │ type (income/exp) │     │ color        │
  │ profile_pic  │           │ description        │          └────────────────┘
  └──────────────┘        │ date               │
          │                  │ payment_method     │          ┌────────────────┐
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
│  [    SignIn  ]   [   SignUP   ]                │
└─────────────────────────────────────────────────┘
```

### Screen 2 — Dashboard (Home)
```
┌─────────────────────────────────────────────────────────────────┐
│ 💸 Expense Tracker         |  👤 John Doe     [Logout]         │
│─────────────────────────────────────────────────────────────────│
│ 📊 May 2026 Summary                                             │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│ │ Total Income │  │Total Expense │  │   Balance    │            │
│ │  ₹45,000     │  │  ₹28,500     │  │  ₹16,500     │            │
│ └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                 │
│  [Pie Chart: Expense by Category]  [Bar Chart: Monthly Trend]   │
│                                                                 │
│  Recent Transactions                                            │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ 26 May  │ 🍕 Food        │ -₹450   │ Zomato Order      │    │
│  │ 25 May  │ 🚌 Transport   │ -₹120   │ Auto Rickshaw     │    │
│  │ 25 May  │ 💰 Salary      │ +₹45000 │ Monthly Salary    │    │
│  └────────────────────────────────────────────────────────┘     │
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
│                                             │
│            [ ✅ Add Transaction ]           │
└─────────────────────────────────────────────┘
```

### Screen 4 — Budget Manager
```
┌──────────────────────────────────────────────────────┐
│  🎯 Budget Manager — May 2026                        │ 
│  ──────────────────────────────────────────────────  │
│  Food & Dining                                       │
│  ████████████░░░░░░  ₹4,200 / ₹6,000  (70%)          │
│                                                      │
│  Transport                                           │
│  ██████████████████  ₹3,500 / ₹3,000  ⚠️ OVERSPENT   │
│                                                      │
│  Entertainment                                       │
│  ████░░░░░░░░░░░░░░  ₹800 / ₹2,000   (40%)           │
└──────────────────────────────────────────────────────┘
```

### Screen 5 — Analytics
```
┌──────────────────────────────────────────────────────────┐
│  📈 Analytics & Reports                                  │
│  ──────────────────────────────────────────────────────  │
│                                                          │
│  Filter: [Jan ▼] to [May ▼] [2026 ▼]  [Apply]            │
│                                                          │
│  ┌──────────────────────────────────────────────────┐    │
│  │         Monthly Income vs Expense (Bar Chart)    │    │
│  │  ██ Income  ██ Expense                           │    │
│  │  Jan  Feb  Mar  Apr  May                        │     │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
│  ┌──────────────────────────────────────────────────┐    │
│  │         Spending by Category (Pie Chart)         │    │
│  │  🟢 Food 35%  🔵 Transport 20%  🟡 Bills 25%    │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
│  [ 📥 Download CSV Report ]                              │
└──────────────────────────────────────────────────────────┘
```

---

## 💻 All Source Code

### 📁 Project Structure
```
expense-tracking-system/
│
├── Home.py                  # Main Streamlit application entry point and Project Details
│
├── pages/
│   ├── Login.py        #In this page Sigin and Signup form available
│   ├── Profile.py      # change password and see profile details are available
│   ├── Add Transactions.py     Add income/expense form# View/filter all transactions
│   ├── Reports.py           # Data Visulisation
│   
│
├── .streamlit
│   ├── config.toml             # work as CSS and Provide my website Color 
│          
```

---

### 📄 `requirements.txt`
```txt
streamlit==1.32.0
pymongo==4.6.1
python-dotenv==1.0.0
plotly==5.19.0
pandas==2.2.0
Pillow==10.2.0
matplotlib==3.10.8
streamlit-lottie==0.0.5
```
1.The Main Page of my  Python Streamlit website is Home.py .
 in this page I describe my project

![Home](images/home1.png)       ![Home](images/home2.png)
```python
import streamlit as st
import time
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie


st.set_page_config(page_title="💰 Expense Tracker")
st.header(" 💰 Expense Tracking System")

st.logo("logo.png")
st.write("Welcome to the expense tracking webpage. You can Track Income & Expenses Easily ")
com.iframe("https://lottie.host/embed/872ed4cc-0112-4b2b-a488-d3ec21fa9632/FY2sesenYh.lottie")
st.toast("welcome to Expense Tracke")
with st.spinner("Loading..."):
    time.sleep(3)
st.subheader("Project Description:")
st.image("expense _tracker_image.png")
st.markdown('''Expense Tracker is a smart web application that helps users to  monitor, analyze, manage and improve their financial activities
expenses efficiently.
The system uses AI/ML techniques to provide:

- Expense prediction
- Spending analysis
- Smart recommendations
- Budget alerts

The project is developed using Python and Streamlit.
We use MongoDB as a Backend DataBase.


''')
with st.expander("See  More Details About Project"):
    st.write("""About Us:Begginer Python Developer | Passionate about AI/ML | Building Innovative Projects | Open to Collaborations | Always Learning and Growing
               
             Contact Us:93xxxxxx67

             """)

st.markdown("[👔](https://www.linkedin.com/in/rishi-munda-a88b80224) |"
" [Github](https://github.com/Rishi50-IT)|""[✖️](https://twitter.com/@340Rishi)")
st.caption("@2026 Expense Tracking System website | Made with love ")

```

2. In my main folder one more subfolder whith name is pages . In pages folder my login page is available
   
![Login](images/login1.png)  ![Login](images/login2.png)

'''Python
import streamlit as st
import pymongo
import random
import time
from datetime import date
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

#live server connection
#conn= pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0")


conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
my=mydb["expenseinfo"]





progress = st.progress(0)
for i in range(100):
     progress.progress(i + 1)
     time.sleep(0.02)
     progress.empty() 
tab1,tab2=st.tabs(["SIGNIN" , "SIGNUP"])
with tab1:
     with st.form("tab1"):

           st.subheader("🔐Login Your Account")
           com.iframe("https://lottie.host/embed/55bc33c7-9ba7-4d9b-9716-219960a85fbd/dYVC0xsrbu.lottie")
           em=st.text_input("📧Email:")
           pa=st.text_input("🔑Password:" , type="password")
           st.checkbox("Terms &Conditions")
           if st.form_submit_button("SIGNIN"):
                if not em or not pa  :
                     st.error("Fill all fields")
                else :
                     user=my.find({"email":em,"password":pa})
                     v=0
                     for data in user:
                          v=v+1
                          st.session_state["Email"]=data['email']
                          st.session_state["password"]=data["password"]
                          st.session_state["image"]=data['photo']
                          st.success(f"🤝𝐖𝐄𝐋𝐂𝐎𝐌𝐄:{data['email']}")
                          st.switch_page("pages/👤 Profile.py")

                     if v==0 :
                              st.error("Invalid Login Details")
                
              

with tab2:
    with st.form("tab2"):
          
          st.subheader("👤 ➕Create New Account")
          com.iframe("https://lottie.host/embed/7467ad87-9159-4b91-9408-315468cde80d/sEHVpSU2at.lottie")
          us=st.text_input("Username")
          mn=st.text_input("Mobile no")
          dob=st.date_input("DOB" ,min_value=date(1975,1,1),max_value=date.today())
          ad=st.text_area("Address")
          e=st.text_input("Email")
          p=st.text_input("🗝️Password:", type="password")
          cp=st.text_input("🈴Conform Password:" , type="password")
          lp=st.camera_input("⋆.📷˚Click your Picture")
          count=random.randrange(1,100000)
          str1="img"
          str1=str1+str(count)+".jpg"
          if lp:
              with open(str1,"wb") as f:
                    f.write(lp.getvalue())
      
          st.checkbox("Terms &Conditions")
          if st.form_submit_button("SIGNUP"):
               my.insert_one({"Username":us ,"Mobileno":mn,"Address":ad,"email":e,"password":p,"photo":str1})
               if p==cp :
                 st.success("Thank you for SIGNUP")
                 #my.insert_one({"Username":us ,"Mobileno":mn,"Address":ad,"email":e,"password":p,"photo":lp})
                 st.balloons()
               else:
                 st.error(" Your password is not same")
st.markdown("---")
st.caption("@2026 Expense Tracking Systm Login Form")
'''

3.In pages folder one more file name Profile.py
in thispage all the information of user can see profile  details and they can also change their password and logout.

![Profile](images/profile1.png)       ![Profile](images/profile2.png)


'''import streamlit as st
import pymongo
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

#for live server data base connection
#conn= pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0")

#for local db
conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
my=mydb["expenseinfo"]

    
st.title("User Profile")

com.iframe("https://lottie.host/embed/cc5b0694-3397-4044-8a59-e72ab8a47e5f/9aZ5nLcu0V.lottie")

@st.dialog("CHANGE PASSWORD")
def cp():
      op=st.text_input("Enter the old Password :")
      np=st.text_input("Enter the New Password :")
      if st.button("Change Password "):
            reset=my.update_one({"password":op},{'$set':{"password":np}})
            st.success("password change successfully")


em=st.session_state["Email"]
imag=st.session_state["image"]
user=my.find({"email":em})

for data in user:
      e=data['email']
      st.write(f"Welcome {e} 👋")
      p=data['photo']
      u=data['Username']
      m=data['Mobileno']
      a=data['Address']
      
      
  
    
c1,c2,c3, c4=st.columns(4)
if c1.button("🪪 see profile",use_container_width=True):
             str1=data["email"]
             str2=st.session_state["password"]
             str3=st.session_state["image"]
             user=my.find({"email":str1,"password":str2,"image":str3})
             st.success("user profile")
             st.image(p)
             st.logo(p)
             st.text_input("Username",u)  
             st.text_input("Mobile No",m)  
             st.text_input("Address",a)                             
             st.text_input("Email",e)                             
                           

if c2.button("🔑change password ",use_container_width=True):
      cp()
if c3.button("➜]Logout",use_container_width=True):
         st.session_state.data = False
         st.session_state.email = ""
         st.session_state.image = ""
         st.success("You have been logged out")
         st.switch_page("login.py")
if c4.button("➕Add Transactions",use_container_width=True):
         st.switch_page("pages/➕💸 Add Transations.py")'''

4. In pages folder One is transaction page name Add Transaction.py
   In this page you can add their income and expense you get all expenses and income details in table formate you also download this in json formate.
    
![Transactions](images/t1.png)                    ![Transactions](images/t2.png)
![Transactions](images/t3.pngz)                   ![Transactions](images/t4.png)
![Transactions](images/t5.png)

'''import streamlit as st
import pandas as pd
import pymongo
from datetime import date
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

#live server connection
#Aconn= pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0")


#for local db
conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["expensedb"]
transactions=mydb["transactions"]

st.set_page_config(page_title="Transaction")
if "transactions" not in st.session_state:
    st.session_state.transactions = []
st.header("➕ Add New Transaction")
c1,c2=st.columns(2)
with c1:
    com.iframe("https://lottie.host/embed/135ca7d0-9a8e-41e2-9a8b-3985fd3a4530/0FWKtPLPAv.lottie")
with c2:
    com.iframe("https://lottie.host/embed/5aed7e16-d179-449b-80c1-d8ef118f27f0/z7O82KECUH.lottie")
    
t1,t2=st.tabs(["💵Add Income","Add Expense"])
with t1:
    st.title("Add Income ")
    
    
    with st.form("Add Income"):
        st.subheader("Add Your  Source of Income")
        com.iframe("https://lottie.host/embed/bfc96117-3415-4682-8141-5a62ce022119/q2M3kpnaAK.lottie")
        category= st.selectbox("Select Category" ,["Salary","Business","Invetsment", "Other Source of Income"] )
        amount = st.number_input("Enter Amount",min_value=0,step=50)
        month = st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September", "October","November","December"])
        income_date = st.date_input("Select Date",value=date.today())
        payment_method= st.radio("Payment Method" ,[ "Cash","Upi","Debit Card","Credit Card"])
        description = st.text_area("Description / Notes")     

    
        if st.form_submit_button("Add Income"):          
           income = {"email":st.session_state["Email"],
               "Type":"Income","Category": category,"Amount": amount,"Month": month,"Date":str( income_date),"Payment": payment_method,"Description": description}

           transactions.insert_one(income)
           st.success("Income Added Successfully ✅ ")

        st.markdown("---")




with t2:

    st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered")

    st.title("💰 Add Expense")

    with st.form("expense_form"):
        com.iframe("https://lottie.host/embed/cf361bf1-f911-43d0-9d81-7aac48e58483/P85yY7w2Kn.lottie")
        category = st.selectbox( "Expense  Category",["Food","Travel","Shopping",
                                "Bills","Entertainment","E-commerce",
                                "Education","Health","Other"])

        amount = st.number_input(
        "💵 Enter Amount",
        min_value=0,
        step=50,
        key="expense_amount")

        month = st.selectbox("Select Expense Month",["January","February",
                                                 "March","April","May",
                                                 "June","July","August",
                                                 "September", "October",
                                                 "November","December"],key="expense_month")
        expense_date = st.date_input("Expense Date",value=date.today(),key="expense_date")
        payment_method = st.radio("Payment Method",["Cash","UPI","Debit Card","Credit Card"],key="expense_payment")
        description = st.text_area("Expense Description / Notes",key="expense_descriptionn")  


        if st.form_submit_button("Add Expense"):
            expense={"email":st.session_state["Email"],
                "Type": "Expense",
                "Category": category,
                "Amount": amount,
                "Month": month,
                "Date":str( expense_date),
                "Payment": payment_method,
                "Description": description}
            transactions.insert_one(expense)
            st.success("Expense Added Successfully ✅")
        else:
            st.info("No Expense  added yet.")
        




st.markdown("---")

st.subheader("📋 All Transactions")
data=list(transactions.find( { "email": st.session_state["Email"] }, {"_id": 0} ))

if data:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)




else:
    st.info("No Transactions Added Yet")

st.subheader("📑Income Records")
if st.button("📊 Data Visulization"):
    st.switch_page("pages/📋📊Reports.py")'''


5.last page of the pages folder is Reports.py.in this page you visualize you transaction in the form of piecharst bargraph line grap etc 

![Reports](images/r1.png)    ![Reports](images/r2.png)
![Reports](images/r3.png)     ![Reports](images/r4.png)
![Reports](images/r5.png)      ![Reports](images/r6.png)
'''
import streamlit as st
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie 


#live server connection
#conn= pymongo.MongoClient("mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0")

conn= pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")

mydb = conn["expensedb"]
transactions = mydb["transactions"]

st.title("📊 Reports & Analytics")
com.iframe("https://lottie.host/embed/a48fea96-bcae-4f62-aee8-e1c07e4f1e59/A5QzK0qPFf.json")

if "Email" not in st.session_state:
    st.error("Please login to view your reports.")
    st.stop()


records=list(transactions.find({"email":st.session_state["Email"]},{"_id": 0}))



if not records:
    st.warning("No Transactions Available")

else:
    data=pd.DataFrame(records)

    st.subheader("📋 Transaction Table")

    st.dataframe(data, use_container_width=True)

    income = data[data["Type"] == "Income"]["Amount"].sum()
    expense = data[data["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense

    c1, c2, c3 = st.columns(3)

    c1.metric("💵 Total Income", f"₹{income}","100%")
    c2.metric("💸 Total Expense", f"₹{expense}","-9%")
    c3.metric("💰 Balance", f"₹{balance}","91%")

    st.markdown("---")
    expense_data = data[data["Type"] == "Expense"]
if not expense_data.empty:
        
        st.subheader("📊 Category Wise Expenses")

        category_data = expense_data.groupby("Category")["Amount"].sum()
 
        fig, ax = plt.subplots()

        ax.bar(category_data.index, category_data.values)

        plt.xticks(rotation=45)

        st.pyplot(fig)

    
   

st.subheader("🥧 Expense Distribution")

fig2, ax2 = plt.subplots()

ax2.pie(
        category_data.values,
        labels=category_data.index,
        autopct="%1.1f%%"
    )

st.pyplot(fig2)


st.subheader("📈 Monthly Transactions")

monthly = data.groupby("Month")["Amount"].sum()

st.line_chart(monthly)


st.subheader("💹 Income vs Expense")

compare = data.groupby("Type")["Amount"].sum()

st.bar_chart(compare)
'''


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

**  Rishi Munda**
- GitHub: [GitHub](https://github.com/Rishi50-IT)
- Email: rishimunda50@gmail.com
- LinkedIn: [ LinkedIn](https://linkedin.com/in/rishi-munda-a88b80224)

---

## 🙏 Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io)
- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [PyMongo Documentation](https://pymongo.readthedocs.io)

---


LIVE URL OF MY WEBSITE : https://expense-tracking-system-website.streamlit.app/


<div align="center">
  <p>Made with ❤️ using Python Streamlit & MongoDB</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>

