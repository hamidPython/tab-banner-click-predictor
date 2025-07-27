
import streamlit as st
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

# CTR پایه برای هر دسته (با Unknown)
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

# دیتای آموزشی برای مدل
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

# UI با فاصله‌های بهتر
st.title("📊 پیش‌بینی کلیک تاب‌بنر ایرانسل‌من")

category_input = st.text_input("🗂 دسته‌بندی برند (مثلاً Gold، Insurance، یا هر چیز دیگر):", "Gold")
category = category_input if category_input in base_ctrs else "Unknown"

st.markdown("### ⭐ امتیاز برند و آفر")
brand_score = st.slider("🔹 قدرت برند (۰ تا ۵)", 0, 5, 3)
offer_score = st.slider("🔸 قدرت آفر (۰ تا ۵)", 0, 5, 3)

base_ctr = base_ctrs[category]
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

impressions = 5_000_000 * 0.5
ctr = predicted_clicks / impressions

st.markdown("---")
st.subheader("🔎 نتایج پیش‌بینی")
st.markdown(f"📌 **CTR نهایی پیش‌بینی‌شده:** `{round(ctr * 100, 2)}٪`")
st.markdown(f"📌 **تعداد کلیک تخمینی:** `{int(predicted_clicks):,}` کلیک از `{int(impressions):,}` ایمپرشن")

