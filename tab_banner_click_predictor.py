import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Base CTR for each category
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
    'Health': 0.004
}

# Default CTR for unknown categories
default_ctr = 0.005

# Training data
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

# Train model
X = df[["base_ctr", "brand_score", "offer_score"]]
y = df["clicks"]

model = GradientBoostingRegressor()
model.fit(X, y)

# Streamlit UI
st.title("📊 Irancell Top Banner Click Predictor")

category_options = list(base_ctrs.keys()) + ['Other']
category = st.selectbox("Category", category_options)
brand_score = st.slider("Brand Strength (0 to 5)", 0, 5, 3)
offer_score = st.slider("Offer Strength (0 to 5)", 0, 5, 3)

# Base CTR lookup with fallback
base_ctr = base_ctrs.get(category, default_ctr)

# Prediction
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

# Impressions estimation
impressions = 5_000_000 * 0.5
ctr = predicted_clicks / impressions

# Results
st.markdown("---")
st.subheader("🔎 Estimated Results")
st.write(f"**Estimated CTR:** {round(ctr * 100, 2)}%")
st.write(f"**Estimated Clicks:** {int(predicted_clicks):,} from {int(impressions):,} impressions")
