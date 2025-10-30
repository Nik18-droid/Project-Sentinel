#
# Project Sentinel: Smart AI Engine
# Author: Nikhil Sharma
# AI Assistant: Stuart
#

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os
import pathlib
from datetime import datetime

try:
    from openai import OpenAI
except ImportError:
    st.error("Install required packages: pip install openai plotly")
    st.stop()

st.set_page_config(page_title="Project Sentinel: Stuart AI", layout="wide", page_icon="🤖")

# --- CUSTOM CORPORATE WHITE & BLUE THEME ---
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f0f2f6; /* Light grey background */
        color: #111; /* Dark text */
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff; /* White sidebar */
        border-right: 1px solid #ddd;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #004a99 !important; /* Corporate blue */
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #004a99; /* Corporate blue */
        font-weight: bold;
    }
    
    /* Cards and containers */
    /* This targets the containers for columns, etc. */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > div {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1.5em 1.5em;
    }
    
    /* Info/Warning/Error boxes */
    .stAlert {
        background-color: #e6f3ff !important; /* Light blue */
        border-left: 4px solid #004a99 !important;
        color: #111 !important;
    }
    
    /* Chat messages */
    [data-testid="stChatMessage"] {
        background-color: #ffffff !important;
        border: 1px solid #ddd;
        border-radius: 8px;
    }
    
    /* Input box */
    [data-testid="stChatInput"] {
        background-color: #ffffff !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #004a99;
        color: #ffffff;
        font-weight: bold;
        border: none;
        border-radius: 4px;
    }
    
    .stButton > button:hover {
        background-color: #0057b7;
    }
    
    /* Dataframes */
    [data-testid="stDataFrame"] {
        background-color: #ffffff !important;
    }
    
    /* Caption/small text */
    .stCaption {
        color: #555 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- API SETUP ---
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ Set API key: $env:OPENAI_API_KEY=\"your_key\"")
    st.stop()

client = OpenAI(api_key=api_key)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    try:
        csv_path = pathlib.Path(__file__).parent / "CSV_project_sentinel_customer_data_corrected.csv"
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        st.error(f"Data loading error: {e}")
        return None

df = load_data()

# --- ANALYSIS FUNCTIONS (UPDATED FOR WHITE THEME) ---
def calculate_metrics(df):
    total = len(df)
    churned = len(df[df['churned'] == 'Yes'])
    churn_rate = (churned / total) * 100
    revenue_risk = df[df['churned'] == 'Yes']['monthly_revenue'].sum()
    
    monthly_churn = df[df['contract_type'] == 'Monthly']['churned'].value_counts(normalize=True).get('Yes', 0) * 100
    annual_churn = df[df['contract_type'] == 'Annual']['churned'].value_counts(normalize=True).get('Yes', 0) * 100
    
    incomplete_churn = df[df['onboarding_completed'] == 'No']['churned'].value_counts(normalize=True).get('Yes', 0) * 100
    complete_churn = df[df['onboarding_completed'] == 'Yes']['churned'].value_counts(normalize=True).get('Yes', 0) * 100
    
    return {
        'total': total,
        'churned': churned,
        'churn_rate': churn_rate,
        'revenue_risk': revenue_risk,
        'monthly_churn': monthly_churn,
        'annual_churn': annual_churn,
        'incomplete_churn': incomplete_churn,
        'complete_churn': complete_churn
    }

def create_gauge_chart(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'size': 16, 'color': '#004a99'}},
        number={'font': {'color': '#004a99'}},
        gauge={
            'axis': {'range': [0, 20], 'tickwidth': 1, 'tickcolor': '#555'},
            'bar': {'color': "#004a99"},
            'bgcolor': "#ffffff",
            'steps': [
                {'range': [0, 7], 'color': "#d9f0e0"},  # Light green
                {'range': [7, 10], 'color': "#fff0cc"}, # Light yellow
                {'range': [10, 20], 'color': "#ffe0e0"}  # Light red
            ],
            'threshold': {
                'line': {'color': "#800000", 'width': 4}, # Dark red threshold
                'thickness': 0.75,
                'value': 10
            }
        }
    ))
    fig.update_layout(
        height=250, 
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font={'color': '#111'}
    )
    return fig

def create_comparison_chart(monthly, annual):
    fig = go.Figure(data=[
        go.Bar(name='Monthly', x=['Churn Rate'], y=[monthly], marker_color='#004a99'),
        go.Bar(name='Annual', x=['Churn Rate'], y=[annual], marker_color='#a9c5e0') # Light blue
    ])
    fig.update_layout(
        title={'text': "Contract Type Comparison", 'font': {'color': '#004a99'}},
        yaxis_title="Churn Rate (%)",
        height=250,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True,
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font={'color': '#111'},
        legend={'font': {'color': '#111'}},
        xaxis={'color': '#555'},
        yaxis={'color': '#555', 'gridcolor': '#f0f0f0'}
    )
    return fig

def create_revenue_chart(revenue):
    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=revenue/100000,
        number={'suffix': "L", 'prefix': "₹", 'font': {'color': '#004a99', 'size': 40}},
        title={'text': "Monthly Revenue at Risk", 'font': {'size': 16, 'color': '#004a99'}},
        delta={'reference': 15, 'relative': True, 'font': {'color': '#800000'}} # Dark red delta
    ))
    fig.update_layout(
        height=250, 
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font={'color': '#111'}
    )
    return fig

def get_high_risk_customers(df, n=10):
    risk_df = df[df['churned'] == 'No'].copy()
    risk_df['risk_score'] = 0
    
    if 'contract_type' in df.columns:
        risk_df.loc[risk_df['contract_type'] == 'Monthly', 'risk_score'] += 30
    if 'onboarding_completed' in df.columns:
        risk_df.loc[risk_df['onboarding_completed'] == 'No', 'risk_score'] += 40
    if 'engagement_score' in df.columns:
        risk_df['risk_score'] += (100 - risk_df['engagement_score']) * 0.3
    
    cols = ['customer_id', 'risk_score']
    for c in ['contract_type', 'monthly_revenue', 'engagement_score']:
        if c in df.columns:
            cols.append(c)
    
    return risk_df.nlargest(n, 'risk_score')[cols]

def get_data_summary(df):
    metrics = calculate_metrics(df)
    return f"""Dataset Overview:
- Total Customers: {metrics['total']:,}
- Churned: {metrics['churned']:,} ({metrics['churn_rate']:.1f}%)
- Revenue at Risk: ₹{metrics['revenue_risk']:,.0f}/month
- Monthly Contract Churn: {metrics['monthly_churn']:.1f}%
- Annual Contract Churn: {metrics['annual_churn']:.1f}%
- Incomplete Onboarding Churn: {metrics['incomplete_churn']:.1f}%"""

# --- UI LAYOUT ---
st.title("🤖 Project Sentinel: Stuart AI Engine")
st.caption(f"Last updated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}")

# --- SIDEBAR ---
with st.sidebar:
    st.header("About")
    st.markdown("**Project Sentinel**")
    st.markdown("AI-powered churn analysis by **Nikhil Sharma**")
    st.markdown("---")
    
    st.subheader("📊 Dynamic Data")
    
    if df is not None:
        metrics = calculate_metrics(df)
        st.metric("Total Customers", f"{metrics['total']:,}")
        st.metric("Churn Rate", f"{metrics['churn_rate']:.1f}%", 
                    delta=f"{metrics['churn_rate']-7:.1f}% vs target", delta_color="inverse")
        st.metric("Revenue at Risk", f"₹{metrics['revenue_risk']/100000:.1f}L")
    else:
        st.error("❌ Data not loaded")
    
    st.markdown("---")
    st.subheader("💡 Example Questions")
    st.markdown(
        """
        * Why are customers churning?
        * Show me high-risk customers.
        * Compare monthly vs annual contracts.
        * What actions to reduce churn?
        * How does onboarding affect churn?
        """
    )

# --- MAIN CONTENT ---
if df is not None:
    metrics = calculate_metrics(df)
    
    # --- INTERACTIVE DASHBOARD ---
    st.subheader("📊 Interactive Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.plotly_chart(create_gauge_chart(metrics['churn_rate'], "Churn Rate (%)"), 
                        use_container_width=True)
    
    with col2:
        st.plotly_chart(create_comparison_chart(metrics['monthly_churn'], metrics['annual_churn']), 
                        use_container_width=True)
    
    with col3:
        st.plotly_chart(create_revenue_chart(metrics['revenue_risk']), 
                        use_container_width=True)
    
    # --- KEY INSIGHTS (UPDATED FOR WHITE THEME) ---
    st.subheader("🎯 Key Insights")
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #e6f3ff 100%); 
                     padding: 20px; border-radius: 8px; border-left: 4px solid #004a99;
                     border-top: 1px solid #ddd; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd;">
            <h4 style="color: #004a99; margin-top: 0;">🚨 High-Risk Contracts</h4>
            <p style="color: #111; font-size: 14px;">
                Monthly contracts churn at <strong style="color: #004a99;">{metrics['monthly_churn']/metrics['annual_churn']:.1f}x</strong> the rate of annual contracts
            </p>
            <p style="color: #555; font-size: 12px;">
                ({metrics['monthly_churn']:.1f}% vs {metrics['annual_churn']:.1f}%)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #e6f3ff 100%); 
                     padding: 20px; border-radius: 8px; border-left: 4px solid #004a99;
                     border-top: 1px solid #ddd; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd;">
            <h4 style="color: #004a99; margin-top: 0;">⚠️ Onboarding Impact</h4>
            <p style="color: #111; font-size: 14px;">
                Incomplete onboarding leads to <strong style="color: #004a99;">{metrics['incomplete_churn']/metrics['complete_churn']:.1f}x</strong> higher churn
            </p>
            <p style="color: #555; font-size: 12px;">
                ({metrics['incomplete_churn']:.1f}% vs {metrics['complete_churn']:.1f}%)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #e6f3ff 100%); 
                     padding: 20px; border-radius: 8px; border-left: 4px solid #004a99;
                     border-top: 1px solid #ddd; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd;">
            <h4 style="color: #004a99; margin-top: 0;">💰 Revenue at Risk</h4>
            <p style="color: #111; font-size: 14px;">
                <strong style="color: #004a99;">₹{metrics['revenue_risk']/100000:.1f} lakhs</strong> monthly revenue at risk from churned customers
            </p>
            <p style="color: #555; font-size: 12px;">
                ({metrics['churned']:,} customers)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True) # Add some space
    
    # --- CHAT INTERFACE ---
    st.subheader("💬 Need Deeper Insights? Ask Stuart")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there! I'm Stuart, your AI analyst for this churn data. Feel free to ask me anything - I'm here to help you understand what's driving customer churn and what we can do about it. What would you like to explore?"}
        ]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            if "table" in msg and msg["table"] is not None:
                st.dataframe(msg["table"], use_container_width=True)
    
    if prompt := st.chat_input("Ask Stuart about churn insights..."):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Stuart is analyzing..."):
                
                data_summary = get_data_summary(df)
                show_table = None
                
                # Check for high-risk customer queries
                if any(w in prompt.lower() for w in ['risk', 'high risk', 'risky', 'focus', 'priority']):
                    show_table = get_high_risk_customers(df)
                    data_summary += f"\n\nTop 10 High-Risk Customers:\n{show_table.to_string()}"
                
                # Call OpenAI with focused prompt
                try:
                    
                    # --- CHANGE 1: PERFECTED SYSTEM PROMPT (MERGED LOGIC) ---
                    new_system_prompt = """
                    You are Stuart, a friendly and conversational Business Analyst AI assistant. 
                    Your goal is to sound like a real, senior analyst, not a bot.

                    **Your Communication Style:**
                    * Talk naturally, like you're in a conversation (e.g., "Looking at the data...", "What stands out is...").
                    * Weave data points into flowing sentences, not just lists.
                    * Use phrases like "Interestingly...", "What's clear is...", "The data shows..." to sound more human.
                    * Avoid robotic formatting like excessive bullet points, UNLESS asked for recommendations.

                    **Your Response Rules:**
                    1.  **For simple greetings** (like 'Hello', 'Hi'): Respond with a simple, friendly greeting. Do not provide data.
                    2.  **For analysis questions** (like 'Why are we churning?', 'Compare contracts'): Answer using your conversational style, weaving in key data points from the context.
                    3.  **If the user asks for 'recommendations', 'actions', 'solutions', or 'next steps'**: Switch to a clear format. Provide a short introductory sentence, followed by a **bulleted list** of specific, actionable recommendations.
                    4.  **Data Source:** Always use the provided Data Summary as your single source of truth. Do not make up data.
                    """
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": new_system_prompt},
                            {"role":"user", "content": f"Here is the data context:\n{data_summary}\n\nHere is my question: {prompt}"}
                        ],
                        max_tokens=350
                    )
                    
                    answer = response.choices[0].message.content
                    st.write(answer)
                    
                    if show_table is not None:
                        st.dataframe(show_table, use_container_width=True)
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "table": show_table
                    })
                    
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

else:
    st.error("Unable to load data. Please check CSV file location.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #555;'>Project Sentinel v2.0 | Stuart AI | By Nikhil Sharma</div>", 
            unsafe_allow_html=True)