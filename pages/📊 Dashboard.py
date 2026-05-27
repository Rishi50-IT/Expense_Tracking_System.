import streamlit as st
import pandas as pd




st.title("📊 Expense Dashboard")

st.markdown("Welcome to your AI Powered Expense Tracker")

    # ---------------- TOP METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
        "💰 Total Balance",
        "₹75,000",
        "+12%"
    )

col2.metric(
        "📈 Income",
        "₹50,000",
        "+8%"
    )

col3.metric(
        "📉 Expense",
        "₹18,500",
        "-5%"
    )

col4.metric(
        "💵 Savings",
        "₹31,500",
        "+20%"
    )

st.markdown("---")

    # ---------------- CHART SECTION ----------------
chart1, chart2 = st.columns(2)

with chart1:

        st.subheader("📈 Monthly Expense Trend")

        expense_chart = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
            "Expense": [12000, 18000, 10000, 22000, 15000]
        })

        st.line_chart(
            expense_chart.set_index("Month")
        )

with chart2:

        st.subheader("📊 Category Wise Expense")

        category_chart = pd.DataFrame({
            "Category": [
                "Food",
                "Travel",
                "Shopping",
                "Bills"
            ],
            "Amount": [4000, 2500, 5000, 7000]
        })

        st.bar_chart(
            category_chart.set_index("Category")
        )

st.markdown("---")

    # ---------------- RECENT TRANSACTIONS ----------------
st.subheader("🧾 Recent Transactions")

transaction_data = pd.DataFrame({
        "Date": [
            "10 May",
            "12 May",
            "14 May",
            "16 May"
        ],
        "Category": [
            "Food",
            "Shopping",
            "Bills",
            "Travel"
        ],
        "Amount": [
            500,
            2500,
            4000,
            1200
        ],
        "Payment": [
            "UPI",
            "Card",
            "Cash",
            "UPI"
        ]
    })
st.dataframe(
        transaction_data,
        use_container_width=True
    )

st.markdown("---")
