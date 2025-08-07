import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_hotel_data.csv', parse_dates=['reservation_status_date'])

df = load_data()

# Title
st.title("🏨 Hotel Booking Dashboard")

# Sidebar filters
hotel_filter = st.sidebar.multiselect("Select Hotel Type", df['hotel'].unique(), default=df['hotel'].unique())
year_filter = st.sidebar.multiselect("Select Year", df['arrival_date_year'].unique(), default=df['arrival_date_year'].unique())
customer_filter = st.sidebar.multiselect("Select Customer Type", df['customer_type'].unique(), default=df['customer_type'].unique())

# Apply filters
df_filtered = df[
    (df['hotel'].isin(hotel_filter)) &
    (df['arrival_date_year'].isin(year_filter)) &
    (df['customer_type'].isin(customer_filter))
]

# KPIs
total_bookings = len(df_filtered)
cancellations = df_filtered['is_canceled'].sum()
cancel_rate = round((cancellations / total_bookings) * 100, 2)
avg_adr = round(df_filtered['adr'].mean(), 2)
avg_lead_time = round(df_filtered['lead_time'].mean(), 1)

st.markdown("### 📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Bookings", total_bookings)
col2.metric("Cancel Rate", f"{cancel_rate}%")
col3.metric("Avg ADR", f"${avg_adr}")
col4.metric("Avg Lead Time", f"{avg_lead_time} days")

# Charts

st.markdown("### 📅 Bookings per Month")
monthly = df_filtered.groupby(['arrival_date_month', 'arrival_date_year']).size().reset_index(name='Bookings')
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
monthly['arrival_date_month'] = pd.Categorical(monthly['arrival_date_month'], categories=month_order, ordered=True)
monthly = monthly.sort_values(by=['arrival_date_year', 'arrival_date_month'])
fig1 = px.bar(monthly, x='arrival_date_month', y='Bookings', color='arrival_date_year', barmode='group')
st.plotly_chart(fig1)

st.markdown("### 🏨 Cancellation Rate by Market Segment")
cancel_segment = df_filtered.groupby('market_segment')['is_canceled'].mean().reset_index()
cancel_segment['is_canceled'] = cancel_segment['is_canceled'] * 100
fig2 = px.bar(cancel_segment, x='market_segment', y='is_canceled', labels={'is_canceled': 'Cancel Rate (%)'})
st.plotly_chart(fig2)

st.markdown("### 💰 ADR Distribution by Hotel")
fig3 = px.box(df_filtered, x='hotel', y='adr')
st.plotly_chart(fig3)

st.markdown("### 👥 Customer Type Distribution")
customer_count = df_filtered['customer_type'].value_counts().reset_index()
customer_count.columns = ['Customer Type', 'Count']
fig4 = px.pie(customer_count, names='Customer Type', values='Count', hole=0.4)
st.plotly_chart(fig4)