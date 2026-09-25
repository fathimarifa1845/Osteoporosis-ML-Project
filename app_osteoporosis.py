import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier

st.set_page_config(
    page_title="OsteoGuard AI | Osteoporosis Risk Predictor",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 20px;
        border-left: 6px solid #2563eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .risk-high {
        background-color: #fef2f2;
        border: 2px solid #ef4444;
        border-radius: 10px;
        padding: 20px;
        color: #991b1b;
    }
    .risk-low {
        background-color: #f0fdf4;
        border: 2px solid #22c55e;
        border-radius: 10px;
        padding: 20px;
        color: #166534;
    }
</style>
""", unsafe_allow_html=True)

# Determine project root directory dynamically (one folder up from "Streamlit application")
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@st.cache_resource
def load_or_train_pipeline():
    # 1. Candidate paths to load pre-saved model
    model_candidates = [
        os.path.join(BASE_DIR, "Notebook & Saved Model", "osteoporosis_model.pkl"),
        os.path.join(BASE_DIR, "osteoporosis_model.pkl"),
        "osteoporosis_model.pkl",
        os.path.join("Notebook & Saved Model", "osteoporosis_model.pkl")
    ]
    
    for path in model_candidates:
        if os.path.exists(path):
            try:
                return joblib.load(path)
            except Exception:
                pass

    # 2. Fallback: locate osteoporosis.csv using the new folder layout
    csv_candidates = [
        os.path.join(BASE_DIR, "Dataset", "osteoporosis.csv"),
        os.path.join(BASE_DIR, "osteoporosis.csv"),
        "osteoporosis.csv",
        os.path.join("Dataset", "osteoporosis.csv")
    ]
    
    csv_file = next((p for p in csv_candidates if os.path.exists(p)), None)
    if not csv_file:
        st.error("Error: Could not locate 'osteoporosis.csv' in 'Dataset/' or root directory.")
        st.stop()

    df = pd.read_csv(csv_file)
    if "Id" in df.columns:
        df = df.drop(columns=["Id"])

    cat_cols = df.select_dtypes(include="object").columns.tolist()
    df[cat_cols] = df[cat_cols].fillna("Not Reported")

    X = df.drop(columns=["Osteoporosis"])
    y = df["Osteoporosis"]

    num_cols = ["Age"]
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )

    gb_model = GradientBoostingClassifier(
        learning_rate=0.05,
        max_depth=4,
        n_estimators=100,
        subsample=0.8,
        random_state=42
    )

    pipe = Pipeline(steps=[("preprocessor", preprocessor), ("model", gb_model)])
    pipe.fit(X, y)
    return pipe

pipeline = load_or_train_pipeline()

# Header & Overview
st.title("🦴 OsteoGuard AI: Osteoporosis Risk Prediction System")
st.markdown("Clinical decision-support tool providing probabilistic assessment for early intervention and osteoporosis fracture risk mitigation.")
st.markdown("---")

# Layout with Columns
col_inputs, col_results = st.columns([1.1, 1], gap="large")

with col_inputs:
    st.subheader("📋 Patient Clinical & Lifestyle Profile")

    with st.expander("👤 Demographics & Constitutional Factors", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            age = st.slider("Patient Age (Years)", min_value=18, max_value=95, value=65, step=1)
            gender = st.selectbox("Biological Sex", ["Female", "Male"])
            race = st.selectbox("Race / Ethnicity", ["Caucasian", "Asian", "African American"])
        with c2:
            body_weight = st.selectbox("Body Weight Category", ["Normal", "Underweight"])
            hormonal_changes = st.selectbox("Hormonal Profile", ["Normal", "Postmenopausal"])
            family_history = st.selectbox("Family History of Osteoporosis", ["No", "Yes"])

    with st.expander("🥗 Nutrition & Daily Lifestyle", expanded=True):
        c3, c4 = st.columns(2)
        with c3:
            calcium_intake = st.selectbox("Dietary Calcium Intake", ["Low", "Adequate"])
            vitamin_d = st.selectbox("Vitamin D Intake", ["Insufficient", "Sufficient"])
            physical_activity = st.selectbox("Physical Activity Level", ["Active", "Sedentary"])
        with c4:
            smoking = st.selectbox("Smoking Status", ["No", "Yes"])
            alcohol = st.selectbox("Alcohol Consumption", ["Not Reported", "Moderate"])

    with st.expander("💊 Medical History & Pharmacotherapy", expanded=True):
        c5, c6 = st.columns(2)
        with c5:
            medical_cond = st.selectbox("Underlying Secondary Medical Conditions", 
                                        ["Not Reported", "Hyperthyroidism", "Rheumatoid Arthritis"])
            medications = st.selectbox("Prescribed High-Risk Medications", 
                                       ["Not Reported", "Corticosteroids"])
        with c6:
            prior_fractures = st.selectbox("History of Prior Low-Trauma Fractures", ["No", "Yes"])

    predict_btn = st.button("🔍 Assess Osteoporosis Risk", use_container_width=True, type="primary")

with col_results:
    st.subheader("📊 Clinical Risk Assessment Output")

    input_dict = {
        "Age": [age],
        "Gender": [gender],
        "Hormonal Changes": [hormonal_changes],
        "Family History": [family_history],
        "Race/Ethnicity": [race],
        "Body Weight": [body_weight],
        "Calcium Intake": [calcium_intake],
        "Vitamin D Intake": [vitamin_d],
        "Physical Activity": [physical_activity],
        "Smoking": [smoking],
        "Alcohol Consumption": [alcohol],
        "Medical Conditions": [medical_cond],
        "Medications": [medications],
        "Prior Fractures": [prior_fractures]
    }
    input_df = pd.DataFrame(input_dict)

    prob_positive = pipeline.predict_proba(input_df)[0][1]
    prediction = 1 if prob_positive >= 0.50 else 0

    st.write(f"**Predicted Osteoporosis Probability:** `{prob_positive * 100:.1f}%`")
    st.progress(float(prob_positive))

    if prob_positive >= 0.50:
        st.markdown(f"""
        <div class="risk-high">
            <h3 style="margin-top:0;">⚠️ High Risk Detected (Score: {prob_positive * 100:.1f}%)</h3>
            <p>The patient exhibits high-risk indicators associated with secondary and primary bone demineralization.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="risk-low">
            <h3 style="margin-top:0;">✅ Low Risk (Score: {prob_positive * 100:.1f}%)</h3>
            <p>The patient is currently below the critical algorithmic threshold for osteoporosis.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🩺 Clinical Recommendations")
    recommendations = []

    if age >= 65 or prob_positive >= 0.50:
        recommendations.append("Order a diagnostic Dual-Energy X-ray Absorptiometry (DEXA) scan of lumbar spine and femoral neck.")
    if calcium_intake == "Low":
        recommendations.append("Recommend dietary calcium optimization (1,200 mg/day elemental calcium equivalent).")
    if vitamin_d == "Insufficient":
        recommendations.append("Prescribe cholecalciferol (Vitamin D3) supplementation (800–2,000 IU daily).")
    if physical_activity == "Sedentary":
        recommendations.append("Encourage progressive weight-bearing aerobic and muscle-strengthening exercise programs.")
    if medications == "Corticosteroids":
        recommendations.append("Review long-term corticosteroid therapy regimen; evaluate concurrent prophylactic bisphosphonates.")
    if prior_fractures == "Yes":
        recommendations.append("History of prior fracture elevates subsequent fracture hazard; consider initiating antiresorptive or bone-anabolic therapy.")
    if not recommendations:
        recommendations.append("Maintain routine age-appropriate wellness checks and balanced diet.")

    for rec in recommendations:
        st.info(f"• {rec}")

    st.markdown("---")
    st.caption("ℹ️ *Disclaimer: OsteoGuard AI is an adjunctive decision-support tool. All clinical decisions must be guided by verified BMD testing, FRAX scoring, and board-certified physician discretion.*")