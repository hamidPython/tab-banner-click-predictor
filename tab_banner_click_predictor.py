
import streamlit as st

# داده‌ها
base_ctrs = {
    'Gold': 0.011,
    'Insurance': 0.007,
    'Food': 0.010,
    'Online/Shopping': 0.012,
    'VOD': 0.009,
    'Crypto': 0.005,
    'Finance/Invest': 0.010,
    'LMS': 0.004,
    'Job': 0.004,
    'Health': 0.004
}

adjustment_factors = {
    'Gold': 0.7,
    'Insurance': 0.65,
    'Food': 0.75,
    'Online/Shopping': 0.85,
    'VOD': 0.8,
    'Crypto': 0.6,
    'Finance/Invest': 0.75,
    'LMS': 0.6,
    'Job': 0.6,
    'Health': 0.65
}

# UI
st.title("📊 پیش‌بینی کلیک روزانه تاب‌بنر ایرانسل‌من")
st.markdown("مدل واقع‌گرایانه بر اساس CTR واقعی بازار و ویژگی‌های برند")

category = st.selectbox("دسته برند:", ["بدون دسته‌بندی (ناشناخته)"] + list(base_ctrs.keys()))
brand_score = st.slider("قدرت برند (۰ تا ۵):", 0, 5, 3)
offer_score = st.slider("جذابیت آفر (۰ تا ۵):", 0, 5, 3)

# تنظیمات کلی
view_rate = 0.5
active_users = 5_000_000
impressions = active_users * view_rate

# محاسبات
if category == "بدون دسته‌بندی (ناشناخته)":
    market_avg_ctr = 0.004  # 0.4٪
    final_ctr = market_avg_ctr * (1 + 0.03 * brand_score + 0.05 * offer_score)
    predicted_clicks = round(impressions * final_ctr)

    st.subheader("📈 مدل اصلاح‌شده (برند بدون دسته‌بندی):")
    st.write(f"- CTR پایه بازار: {round(market_avg_ctr * 100, 2)}٪")
    st.write(f"- CTR نهایی: {round(final_ctr * 100, 2)}٪")
    st.write(f"- ایمپرشن روزانه: {int(impressions):,}")
    st.success(f"**کلیک تخمینی نهایی: {predicted_clicks:,} کلیک**")

else:
    base_ctr = base_ctrs[category]
    adjustment = adjustment_factors[category]
    final_ctr = base_ctr * (1 + 0.05 * brand_score + 0.05 * offer_score)
    theoretical_clicks = impressions * final_ctr
    adjusted_clicks = round(theoretical_clicks * adjustment)

    st.subheader("📈 مدل دسته‌بندی‌شده (واقع‌گرایانه):")
    st.write(f"- CTR پایه: {round(base_ctr * 100, 2)}٪")
    st.write(f"- CTR نهایی: {round(final_ctr * 100, 2)}٪")
    st.write(f"- ایمپرشن روزانه: {int(impressions):,}")
    st.write(f"- کلیک تئوری: {int(theoretical_clicks):,}")
    st.success(f"**کلیک واقع‌گرایانه: {adjusted_clicks:,} کلیک**")
