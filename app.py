from tracker import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.markdown("""
    <style>
        .app-title { text-align: center; color: #5B2C6F; margin-bottom: 0; font-size: 3rem; }
        .app-subtitle { text-align: center; color: #5B2C6F; margin-top: 0.1rem; margin-bottom: 1.5rem; font-size: 1.1rem; }
        .section-header { color: #5B2C6F; margin-top: 1.5rem; }
        .home-title { color: #0F4D4D; }
        .add-title { color: #2D8A55; }
        .view-title { color: #4A5568; }
        .summary-title { color: #2A52BE; }
        .stButton>button {
            border-radius: 0.85rem;
            padding: 0.85rem 1rem;
            font-weight: 600;
            transition: transform 0.2s ease;
        }
        .stButton>button:hover {
            transform: translateY(-1px);
        }
        .stButton>button:focus {
            box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.08);
        }
        .stButton>button:active {
            transform: translateY(0);
        }
        div[role="row"]:first-of-type > div:first-of-type .stButton > button {
            background-color: #0F4D4D !important;
            color: #FFFFFF !important;
            border-color: #0F4D4D !important;
        }
        div[role="row"]:first-of-type > div:first-of-type .stButton > button:hover {
            background-color: #0A3939 !important;
        }
    </style>
    <h1 class="app-title">💰 Expense Tracker</h1>
    <p class="app-subtitle">Monitor spending, streamline budgeting, and gain clean financial visibility.</p>
""", unsafe_allow_html=True)

# Initialize transaction storage
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Button navigation
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"

with col2:
    if st.button("➕ Add Transaction", use_container_width=True):
        st.session_state.page = "Add Transaction"

with col3:
    if st.button("📋 View Transactions", use_container_width=True):
        st.session_state.page = "View Transaction"

with col4:
    if st.button("📊 Summary", use_container_width=True):
        st.session_state.page = "Summary"

st.divider()

page = st.session_state.page

if page == "Home":
    st.markdown("<h2 class='home-title'>Welcome to Expense Tracker</h2>", unsafe_allow_html=True)
    
    # App Features Section
    st.markdown("<h3 style='color: #2A52BE; margin-top: 2rem;'>Key Features</h3>", unsafe_allow_html=True)
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.markdown("""
        <div style='background-color: #F0F4FF; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
        <h4 style='color: #2A52BE; margin-top: 0;'>📊 Real-time Dashboard</h4>
        <p style='font-size: 0.95rem; color: #4A5568;'>Monitor your income, expenses, and balance in real-time with comprehensive analytics and insights.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background-color: #F0FFF4; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
        <h4 style='color: #2D8A55; margin-top: 0;'>✅ Transaction Management</h4>
        <p style='font-size: 0.95rem; color: #4A5568;'>Easily add, track, and manage all your income and expense transactions with detailed categories.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col2:
        st.markdown("""
        <div style='background-color: #FFF5F0; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
        <h4 style='color: #C05621; margin-top: 0;'>📈 Smart Analytics</h4>
        <p style='font-size: 0.95rem; color: #4A5568;'>Get instant visibility into your spending patterns and financial metrics with visual reports.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background-color: #F5E6FF; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
        <h4 style='color: #6B46C1; margin-top: 0;'>💾 Secure Storage</h4>
        <p style='font-size: 0.95rem; color: #4A5568;'>All your financial data is securely stored and easily accessible whenever you need it.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Financial Summary
    total_transactions = len(st.session_state.transactions)
    total_income = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Income")
    total_expense = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Expense")
    balance = total_income - total_expense
    
    st.markdown("<h3 style='color: #2A52BE;'>Financial Summary</h3>", unsafe_allow_html=True)
    
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 12px; color: white;'>
        <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Total Income</p>
        <h2 style='margin: 10px 0 0 0; font-size: 2.2rem;'>₹{:.2f}</h2>
        </div>
        """.format(total_income), unsafe_allow_html=True)
    
    with summary_col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 12px; color: white;'>
        <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Total Expenses</p>
        <h2 style='margin: 10px 0 0 0; font-size: 2.2rem;'>₹{:.2f}</h2>
        </div>
        """.format(total_expense), unsafe_allow_html=True)
    
    st.markdown("")
    
    # Income vs Expense Chart
    if total_transactions > 0:
        chart_data = pd.DataFrame({
            'Category': ['Income', 'Expenses'],
            'Amount': [total_income, total_expense]
        })
        st.bar_chart(chart_data.set_index('Category'), use_container_width=True)
    
    st.divider()
    
    # Professional Insights
    st.markdown("<h3 style='color: #2A52BE;'>Key Insights</h3>", unsafe_allow_html=True)
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        save_rate = ((balance / total_income * 100) if total_income > 0 else 0)
        st.metric("Savings Rate", f"{save_rate:.1f}%")
    
    with insight_col2:
        expense_ratio = ((total_expense / total_income * 100) if total_income > 0 else 0)
        st.metric("Expense Ratio", f"{expense_ratio:.1f}%")
    
    with insight_col3:
        avg_transaction = (total_income + total_expense) / total_transactions if total_transactions > 0 else 0
        st.metric("Average Transaction", f"₹{avg_transaction:.2f}")

elif page == "Add Transaction":
    st.markdown("<h2 class='add-title'>Add New Transaction</h2>", unsafe_allow_html=True)
    
    with st.form("transaction_form"):
        form_left, form_right = st.columns(2)
        with form_left:
            t_type = st.selectbox("Transaction Type", ["Income", "Expense"])
            category = st.text_input("Category / Source")
            amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        with form_right:
            date = st.date_input("Date")
            description = st.text_area("Description", height=140)
        submitted = st.form_submit_button("Save Transaction")

    if submitted:
        transaction = {
            "type": t_type,
            "category": category,
            "amount": amount,
            "date": str(date),
            "description": description,
        }
        st.session_state.transactions.append(transaction)
        st.success("Transaction added successfully.")

elif page == "View Transaction":
    st.markdown("<h2 class='view-title'>View Transactions</h2>", unsafe_allow_html=True)
    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions)
        df = df.rename(columns={"type": "Type", "category": "Category", "amount": "Amount", "date": "Date", "description": "Description"})
        st.dataframe(df.style.format({"Amount": "₹{:.2f}"}))
    else:
        st.info("No transactions have been added yet. Use Add Transaction to begin tracking.")

elif page == "Summary":
    st.markdown("<h2 class='summary-title'>Summary</h2>", unsafe_allow_html=True)
    total_transactions = len(st.session_state.transactions)
    total_income = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Income")
    total_expense = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Expense")
    balance = total_income - total_expense
    
    summary_col1, summary_col2, summary_col3 = st.columns(3)
    summary_col1.metric("Transactions", total_transactions)
    summary_col2.metric("Income", f"₹{total_income:.2f}")
    summary_col3.metric("Expenses", f"₹{total_expense:.2f}")
    
    st.markdown(f"### Net Balance: ₹{balance:.2f}")
    
    st.divider()
    
    # Expense Breakdown by Category - Pie Chart
    st.write("#### Expense Breakdown by Category")
    category_expenses = {}
    for t in st.session_state.transactions:
        if t["type"] == "Expense":
            category = t.get("category", "Uncategorized").lower()
            # Map to standard categories
            if "food" in category or "restaurant" in category or "meal" in category:
                category = "Food"
            elif "shopping" in category or "clothes" in category or "grocery" in category:
                category = "Shopping"
            elif "travel" in category or "transport" in category or "bus" in category or "train" in category:
                category = "Travel"
            elif "bill" in category or "utility" in category or "electricity" in category or "water" in category:
                category = "Bills"
            else:
                category = t.get("category", "Uncategorized")
            category_expenses[category] = category_expenses.get(category, 0) + t["amount"]
    
    if category_expenses:
        # Pie Chart
        fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=80)
        ax.pie(category_expenses.values(), labels=category_expenses.keys(), autopct='%1.1f%%', startangle=90,pctdistance=3.2, labeldistance=1.3)
        ax.axis('equal')
        st.pyplot(fig)
        
        # Data table
        df_expenses = pd.DataFrame(list(category_expenses.items()), columns=["Category", "Total Amount"])
        st.dataframe(df_expenses.style.format({"Total Amount": "₹{:.2f}"}))
    else:
        st.info("No expense data available yet. Add expenses to generate a summary.")
    
    st.divider()
    
    # Monthly Expenses Bar Chart
    st.write("#### Monthly Expenses")
    monthly_expenses = {}
    for t in st.session_state.transactions:
        if t["type"] == "Expense":
            date = pd.to_datetime(t["date"])
            month_year = date.strftime("%Y-%m")
            monthly_expenses[month_year] = monthly_expenses.get(month_year, 0) + t["amount"]
    
    if monthly_expenses:
        df_monthly = pd.DataFrame(list(monthly_expenses.items()), columns=["Month", "Total Expenses"])
        df_monthly = df_monthly.sort_values("Month")
        st.bar_chart(df_monthly.set_index("Month"))
    else:
        st.info("No monthly expense data available.")
    
    st.divider()
    
    # Spending Over Time Line Chart
    st.write("#### Spending Over Time")
    spending_over_time = {}
    for t in st.session_state.transactions:
        if t["type"] == "Expense":
            date = pd.to_datetime(t["date"])
            date_str = date.strftime("%Y-%m-%d")
            spending_over_time[date_str] = spending_over_time.get(date_str, 0) + t["amount"]
    
    if spending_over_time:
        df_time = pd.DataFrame(list(spending_over_time.items()), columns=["Date", "Amount"])
        df_time["Date"] = pd.to_datetime(df_time["Date"])
        df_time = df_time.sort_values("Date")
        st.line_chart(df_time.set_index("Date"))
    else:
        st.info("No spending data over time available.")
    
    st.divider()
    
    # Recent Transactions
    st.write("#### Recent Transactions")
    if st.session_state.transactions:
        recent = st.session_state.transactions[-5:]  # Last 5 transactions
        for i, t in enumerate(reversed(recent), 1):
            emoji = "💰" if t["type"] == "Income" else "💸"
            st.write(f"{i}. {emoji} {t['type']} | {t.get('category', 'N/A')} | ₹{t['amount']:.2f} ({t['date']})")
    else:
        st.info("No transactions available.")
    
    st.divider()
    
    # Professional Budget Tracker
    st.write("#### Budget Tracker")
    budget_col1, budget_col2 = st.columns(2)
    
    with budget_col1:
        monthly_budget = st.number_input("Set Monthly Budget (₹)", min_value=0.0, value=35000.0, step=500.0)
    
    with budget_col2:
        current_month = pd.Timestamp.now().strftime("%Y-%m")
        monthly_spent = sum(t["amount"] for t in st.session_state.transactions 
                           if t["type"] == "Expense" and pd.to_datetime(t["date"]).strftime("%Y-%m") == current_month)
        
        remaining_budget = monthly_budget - monthly_spent
        budget_percentage = (monthly_spent / monthly_budget * 100) if monthly_budget > 0 else 0
        
        st.metric("Budget Used", f"{budget_percentage:.1f}%")
        st.metric("Remaining Budget", f"₹{remaining_budget:.2f}")
        
        # Budget progress bar
        st.progress(min(budget_percentage / 100, 1.0))
        
        if budget_percentage > 90:
            st.error("⚠️ You're close to exceeding your budget!")
        elif budget_percentage > 75:
            st.warning("⚠️ You've used more than 75% of your budget.")
        else:
            st.success("✅ You're within budget limits.")
    