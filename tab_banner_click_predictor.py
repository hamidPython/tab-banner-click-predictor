import streamlit as st
import numpy as np
!pip install scikit-learn
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
    'Health': 0.004
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

# آموزش مدل با Gradient Boosting
X = df[["base_ctr", "brand_score", "offer_score"]]
y = df["clicks"]
model = GradientBoostingRegressor()
model.fit(X, y)

# رابط کاربری Streamlit
st.title("📊 پیش‌بینی کلیک تاب‌بنر ایرانسل‌من")

category = st.selectbox("دسته‌بندی برند:", list(base_ctrs.keys()))
brand_score = st.slider("قدرت برند (0 تا 5)", 0, 5, 3)
offer_score = st.slider("قدرت آفر (0 تا 5)", 0, 5, 3)

# پیش‌بینی
base_ctr = base_ctrs[category]
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

impressions = 5_000_000 * 0.5  # فرض: ۵ میلیون DAU × نرخ دیده شدن ۵۰٪
ctr = predicted_clicks / impressions

# نمایش نتایج
st.markdown("---")
st.subheader("🔎 نتایج پیش‌بینی:")
st.write(f"**CTR نهایی پیش‌بینی‌شده:** {round(ctr * 100, 2)}٪")
st.write(f"**تعداد کلیک تخمینی:** {int(predicted_clicks):,} کلیک از {int(impressions):,} ایمپرشن")
