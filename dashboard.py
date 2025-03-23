import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from io import BytesIO

st.title("Comprehensive Hotel Booking Analysis")

# Upload CSV Button
st.sidebar.subheader("📤 Upload New Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:5000/upload_csv", files=files)
    st.sidebar.success("Dataset Updated!")

# Fetch analytics data
st.subheader("📊 Revenue Trends & Analytics")
analytics_response = requests.get("http://127.0.0.1:5000/analytics").json()

# Display Cancellation Rate
st.metric("📉 Cancellation Rate", analytics_response["cancellation_rate"])

# Fetch Revenue Trends Plot
response = requests.get("http://127.0.0.1:5000/plot_revenue")
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    st.image(image, caption="Monthly Revenue Trends", use_column_width=True)
else:
    st.error("⚠️ Failed to load revenue trends graph. Please ensure Flask is running.")


# **Formatted Top Booking Countries**
st.subheader("🌍 Top Booking Countries")
top_countries = analytics_response.get("top_countries", {})

if top_countries:
    for country, count in top_countries.items():
        st.write(f"• **{country}**: {count} bookings")
else:
    st.error("⚠️ No country data available.")

# **Formatted Lead Time Distribution**
st.subheader("📈 Lead Time Distribution")
lead_time = analytics_response.get("lead_time_distribution", {})

if lead_time:
    st.write(f"• **Mean Lead Time:** {lead_time['mean']:.2f} days")
    st.write(f"• **Min Lead Time:** {lead_time['min']} days")
    st.write(f"• **Max Lead Time:** {lead_time['max']} days")
    st.write(f"• **Standard Deviation:** {lead_time['std']:.2f}")
else:
    st.error("⚠️ No lead time data available.")

# **Formatted Forecasted Revenue Trends**
st.subheader("💰 Forecasted Revenue Trends (Next 12 Months)")
predictions = requests.get("http://127.0.0.1:5000/predict_revenue").json().get("predicted_revenue", {})

if predictions:
    for date, revenue in predictions.items():
        st.write(f"• **{date}:** ${revenue:,.2f}")
else:
    st.error("⚠️ No forecast data available.")

# **AI Chatbot**
st.subheader("🦾 Ask AI about Bookings")
user_query = st.text_input("Enter your query:")
if user_query:
    try:
        response = requests.post("http://127.0.0.1:5000/ask", json={"query": user_query})
        
        if response.status_code == 400:
            st.error("⚠️ Invalid request: Make sure to enter a valid query.")
        elif response.status_code == 500:
            st.error("❌ AI processing error. Try again later.")
        else:
            ai_response = response.json()
            if "answer" in ai_response:
                st.write("🧠 AI Response:", ai_response["answer"])
            else:
                st.error("⚠️ AI returned an empty response. Please try again.")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection error: {e}")
