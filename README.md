# AI-Powered Hotel Booking Analytics & Chatbot

## Overview

This project is an **AI-driven hotel booking analytics and chatbot system**, designed to provide **real-time insights, revenue forecasting, and an interactive assistant** using **Flask, Streamlit, and Gemini AI**.

### **Core Features**

✔️ **Live Hotel Analytics** – Track revenue, cancellations, and top booking sources 
✔️ **AI Chatbot** – Get booking-related answers via Gemini AI 
✔️ **Revenue Forecasting** – Predict future revenue using Facebook Prophet   
✔️ **User-Friendly Dashboard** – Intuitive Streamlit interface for visualization 
✔️ **CSV File Support** – Upload datasets dynamically for instant updates 

---

## **Technology Stack**

🔹 **Backend**: Flask (REST API)  
🔹 **Frontend**: Streamlit (Dashboard UI)  
🔹 **AI Model**: Google Gemini 1.5 Pro  
🔹 **Data Handling**: Pandas, NumPy  
🔹 **Visualization**: Matplotlib, Seaborn  
🔹 **Forecasting**: Facebook Prophet

---

## **Project Structure**

```
📂 hotel_booking_analysis_project/
│── 📄 app.py                 # Flask API (Backend)
│── 📄 dashboard.py           # Streamlit UI (Frontend)
│── 📄 hotel_bookings.csv      # Sample Dataset
│── 📄 requirements.txt        # Dependencies List
│── 📄 README.md               # Documentation
```

---

## **Installation & Setup Guide**

### Step 1: Clone the Repository

```bash
git clone https://github.com/Aryan-Rajesh-Python/LLM-Powered-Booking-Analytics-QA-System.git
cd LLM-Powered-Booking-Analytics-QA-System
```

### Step 2: Create & Activate a Virtual Environment _(Optional)_

```bash
python -m venv venv
# Windows
env\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Google Gemini API Key

1. Visit [Google AI Console](https://ai.google.dev/)
2. Generate an API key
3. Open `app.py` and replace:

```python
GOOGLE_API_KEY = "your-gemini-api-key-here"
```

4. **Alternatively**, create a `.env` file to store the key securely.

---

## **Running the Application**

### Step 1: Start the Backend (Flask API)

```bash
python app.py
```

**Flask API is available at:** `http://127.0.0.1:5000/`

### Step 2: Start the Frontend (Streamlit Dashboard)

```bash
streamlit run dashboard.py
```

**Streamlit UI is available at:** `http://localhost:8501/`

---

## **Example AI Queries**

Use the chatbot to ask business-related questions such as:
1️⃣ _What’s the average cancellation rate?_  
2️⃣ _Which month has the highest revenue?_  
3️⃣ _Predict hotel revenue for the next quarter._  
4️⃣ _Which countries have the most hotel bookings?_  
5️⃣ _What strategies help reduce cancellations?_

---

## **API Endpoints**

| Endpoint           | Method | Description                                                          |
| ------------------ | ------ | -------------------------------------------------------------------- |
| `/analytics`       | GET    | Retrieve revenue trends, cancellation rates, and top booking sources |
| `/predict_revenue` | GET    | Forecast hotel revenue for the next 12 months                        |
| `/upload_csv`      | POST   | Upload and update dataset for analysis                               |
| `/ask`             | POST   | AI-powered chatbot for booking-related inquiries                     |

---
