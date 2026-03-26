import streamlit as st
import numpy as np
import pickle

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="🏥",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
        border: none;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    .result-box {
        background-color: #dcfce7;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #166534;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ── Load Model & Scaler ───────────────────────────────────────
model  = pickle.load(open('model.pkl',  'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# ── Title ─────────────────────────────────────────────────────
st.title("🏥 Medical Insurance Charges Predictor")
st.write("Fill in the details below to predict your insurance charges.")
st.divider()

# ── Input Fields ──────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    age      = st.number_input("🎂 Age",      min_value=18,   max_value=100,  value=30)
    bmi      = st.number_input("⚖️  BMI",      min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.number_input("👶 Children", min_value=0,    max_value=10,   value=0)

with col2:
    sex    = st.selectbox("👤 Sex",    ["male", "female"])
    smoker = st.selectbox("🚬 Smoker", ["no", "yes"])
    region = st.selectbox("🗺️  Region", ["southeast", "southwest", "northwest", "northeast"])

st.divider()

# ── Predict Button ────────────────────────────────────────────
if st.button("🔍 Predict Insurance Charges"):

    # Encode inputs
    sex_enc    = 1 if sex    == "male" else 0
    smoker_enc = 1 if smoker == "yes"  else 0

    region_northwest = 1 if region == "northwest" else 0
    region_southeast = 1 if region == "southeast" else 0
    region_southwest = 1 if region == "southwest" else 0

    # Create array
    input_data = np.array([[age, sex_enc, bmi, children, smoker_enc,
                            region_northwest, region_southeast, region_southwest]])

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict & reverse log transform
    pred = np.expm1(model.predict(input_scaled))

    # Show Result
    st.markdown(f"""
        <div class="result-box">
            🏆 Predicted Insurance Charges : ${pred[0]:,.2f}
        </div>
    """, unsafe_allow_html=True)

    # Extra info
    st.info(f"""
    **Your Input Summary:**
    - Age: {age} | BMI: {bmi} | Children: {children}
    - Sex: {sex} | Smoker: {smoker} | Region: {region}
    """)
