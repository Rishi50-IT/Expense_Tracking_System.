import streamlit as st
import pandas as pd
import numpy as np
import pymongo
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🤖 AI Expense Prediction",
    page_icon="🤖",
    layout="wide"
)

# ---------------- LOGIN CHECK ---------------- #

if "Email" not in st.session_state:
    st.error("Please Login First")
    st.stop()

# ---------------- DATABASE ---------------- #

conn = pymongo.MongoClient(
    "mongodb+srv://Rishi_Munda:Rahul124@@cluster0.dod06ln.mongodb.net/?appName=Cluster0"
)

mydb = conn["expensedb"]
transactions = mydb["transactions"]

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='text-align:center;color:#ff4b4b'>
🤖 AI Financial Prediction Dashboard
</h1>
""", unsafe_allow_html=True)




com.iframe("https://lottie.host/embed/a48fea96-bcae-4f62-aee8-e1c07e4f1e59/A5QzK0qPFf.json")


st.markdown("""
- Powered by Machine Learning
- Expense Forecasting 
- Smart Financial Insights
            """)

st.markdown("---")

# ---------------- FETCH DATA ---------------- #

records = list(
    transactions.find(
        {
            "email": st.session_state["Email"],
            "Type": "Expense"
        },
        {"_id": 0}
    )
)

if len(records) == 0:
    st.error("No Expense Records Found")
    st.stop()

df = pd.DataFrame(records)

# ---------------- MONTH MAP ---------------- #

month_map = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

df["MonthNum"] = df["Month"].map(month_map)

monthly_expense = (
    df.groupby("MonthNum")["Amount"]
    .sum()
    .reset_index()
)

if len(monthly_expense) < 2:
    st.warning(
        "Add expenses in at least 2 different months to generate predictions."
    )
    st.stop()

# ---------------- MACHINE LEARNING ---------------- #

X = monthly_expense[["MonthNum"]]
y = monthly_expense["Amount"]

model = LinearRegression()
model.fit(X, y)

next_month = monthly_expense["MonthNum"].max() + 1

if next_month > 12:
    next_month = 1

prediction = model.predict([[next_month]])

current_expense = y.iloc[-1]

change = prediction[0] - current_expense

# ---------------- METRICS ---------------- #

st.subheader("📈 AI Prediction Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💸 Current Expense",
        f"₹{current_expense:,.0f}"
    )

with c2:
    st.metric(
        "🤖 Predicted Expense",
        f"₹{prediction[0]:,.0f}"
    )

with c3:
    st.metric(
        "📊 Difference",
        f"₹{change:,.0f}"
    )

with c4:
    st.metric(
        "📅 Next Month",
        next_month
    )

st.markdown("---")

# ---------------- CONFIDENCE ---------------- #

confidence = min(
    95,
    50 + (len(monthly_expense) * 5)
)

st.subheader("🎯 AI Confidence Score")

st.progress(confidence)

st.success(
    f"Prediction Confidence : {confidence}%"
)

st.markdown("---")

# ---------------- GRAPH ---------------- #

st.subheader("📊 Monthly Expense Trend")

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(
    monthly_expense["MonthNum"],
    monthly_expense["Amount"],
    marker="o",
    linewidth=3
)

ax.set_xlabel("Month Number")
ax.set_ylabel("Expense Amount")
ax.set_title("Monthly Expense Trend")

st.pyplot(fig)

# ---------------- INSIGHTS ---------------- #

st.subheader("🧠 AI Insights")

highest = monthly_expense["Amount"].max()

lowest = monthly_expense["Amount"].min()

average = monthly_expense["Amount"].mean()

st.info(
f"""
📌 Highest Expense : ₹{highest:,.0f}

📌 Lowest Expense : ₹{lowest:,.0f}

📌 Average Expense : ₹{average:,.0f}

📌 Predicted Expense : ₹{prediction[0]:,.0f}
"""
)

# ---------------- ALERT ---------------- #

if prediction[0] > current_expense:

    st.warning(
        f"""
🚨 Overspending Alert

Your expenses may increase by ₹{change:,.0f}
next month.

Consider reducing unnecessary spending.
"""
    )

else:

    st.success(
        """
✅ Positive Financial Trend

Your spending appears stable or decreasing.

Keep following your current budget plan.
"""
    )

# ---------------- RECOMMENDATION ---------------- #

st.subheader("💡 AI Budget Recommendation")

recommended_budget = prediction[0] * 0.9

st.success(
    f"""
Suggested Monthly Budget

₹ {recommended_budget:,.0f}

(10% lower than predicted expense)
"""
)

# ---------------- TABLE ---------------- #

st.subheader("📋 Training Data Used By AI")

st.dataframe(
    monthly_expense,
    use_container_width=True
)

# ---------------- SUMMARY ---------------- #

st.markdown("---")

st.subheader("🤖 Final AI Summary")

st.success(
f"""
Based on your historical spending pattern:

• Current Expense : ₹{current_expense:,.0f}

• Expected Next Month Expense : ₹{prediction[0]:,.0f}

• Suggested Budget : ₹{recommended_budget:,.0f}

• Confidence Score : {confidence}%

Keep monitoring your monthly expenses for more accurate predictions.
"""
)

st.balloons()
