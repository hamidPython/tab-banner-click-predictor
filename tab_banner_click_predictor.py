
import streamlit as st
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

# Base CTR per category (estimated)
base_ctrs = {
    'Gold': 0.011,
    'Insurance': 0.005,
    'Food': 0.009,
    'Online/Shopping': 0.0099,
    'VOD': 0.009,
    'Crypto': 0.005,
    'Finance/Invest': 0.010,
    'LMS': 0.004,
    'Job': 0.004,
    'Health': 0.004,
    'Unknown': 0.006
}

# Training data (hypothetical)
data = [
    {"base_ctr": 0.011, "brand_score": 4, "offer_score": 3, "clicks": 25960},
    {"base_ctr": 0.009, "brand_score": 3, "offer_score": 3, "clicks": 26056},
    {"base_ctr": 0.011, "brand_score": 2, "offer_score": 2, "clicks": 3295},
    {"base_ctr": 0.005, "brand_score": 3, "offer_score": 2, "clicks": 19000},
    {"base_ctr": 0.0099, "brand_score": 3, "offer_score": 4, "clicks": 21000},
    {"base_ctr": 0.005, "brand_score": 2, "offer_score": 2, "clicks": 6300},
    {"base_ctr": 0.004, "brand_score": 1, "offer_score": 1, "clicks": 2900},
    {"base_ctr": 0.004, "brand_score": 2, "offer_score": 2, "clicks": 3200},
    {"base_ctr": 0.004, "brand_score": 2, "offer_score": 2, "clicks": 3100},
    {"base_ctr": 0.010, "brand_score": 3, "offer_score": 3, "clicks": 25500}
]

df = pd.DataFrame(data)

X = df[["base_ctr", "brand_score", "offer_score"]]
y = df["clicks"]
model = GradientBoostingRegressor()
model.fit(X, y)

# UI
st.title("📊 IrancellMan TopBanner Click Predictor")

# Category selection + custom input
category_choice = st.selectbox(" Select brand category:", list(base_ctrs.keys())[:-1] + [" Custom category"])

if category_choice == " Custom category":
    category_input = st.text_input("Enter your custom category:")
    category = category_input if category_input in base_ctrs else "Unknown"
else:
    category = category_choice

st.markdown("### ⭐ Brand and Offer Scores")
brand_score = st.slider("Brand strength (0 to 5)", 0, 5, 3)
offer_score = st.slider("Offer attractiveness (0 to 5)", 0, 5, 3)

# Prediction
base_ctr = base_ctrs.get(category, base_ctrs["Unknown"])
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

# Impression estimate
dau = 5_000_000
visibility_rate = 0.5
impressions = dau * visibility_rate

# Final CTR (calibrated around 0.004 real-world value)
ctr = predicted_clicks / impressions
ctr_calibrated = ctr * 0.9  # small calibration factor to adjust to ~0.4% real-world average

# Output
st.markdown("---")
st.subheader("📈 Prediction Results")
st.markdown(f"**Estimated CTR:** `{round(ctr_calibrated * 100, 2)}%`")
st.markdown(f"**Estimated Clicks:** `{int(predicted_clicks):,}` clicks from `{int(impressions):,}` impressions")
