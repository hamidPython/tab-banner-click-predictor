import streamlit as st
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

# CTR پایه برای هر دسته
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

# دیتای فرضی برای آموزش مدل
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
st.title("📊 پیش‌بینی کلیک تاب‌بنر ایرانسل‌من")

# دسته‌بندی از selectbox + ورودی دلخواه
category_choice = st.selectbox(" انتخاب دسته‌بندی:", list(base_ctrs.keys())[:-1] + [" دسته‌بندی دلخواه"])

if category_choice == "🔧 دسته‌بندی دلخواه":
    category_input = st.text_input("نام دسته‌بندی دلخواه:")
    category = category_input if category_input in base_ctrs else "Unknown"
else:
    category = category_choice

# اسلایدرهای امتیاز
st.markdown("### ⭐ امتیاز برند و آفر")
brand_score = st.slider(" قدرت برند (۰ تا ۵)", 0, 5, 3)
offer_score = st.slider(" قدرت آفر (۰ تا ۵)", 0, 5, 3)

# پیش‌بینی
base_ctr = base_ctrs.get(category, base_ctrs["Unknown"])
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

impressions = 5_000_000 * 0.5
ctr = predicted_clicks / impressions

# خروجی‌ها
st.markdown("---")
st.subheader(" نتایج پیش‌بینی")
st.markdown(f" **CTR نهایی پیش‌بینی‌شده:** `{round(ctr * 100, 2)}٪`")
st.markdown(f" **تعداد کلیک تخمینی:** `{int(predicted_clicks):,}` کلیک از `{int(impressions):,}` ایمپرشن")
