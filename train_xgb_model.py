import pandas as pd
import xgboost as xgb

# Sample training data
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
    {"base_ctr": 0.010, "brand_score": 3, "offer_score": 3, "clicks": 25500},
    {"base_ctr": 0.0095, "brand_score": 4, "offer_score": 4, "clicks": 33000},  # Car
    {"base_ctr": 0.007, "brand_score": 4, "offer_score": 3, "clicks": 24000},  # Reservation
    {"base_ctr": 0.008, "brand_score": 4, "offer_score": 4, "clicks": 28000},  # Travel
]

df = pd.DataFrame(data)

# Features & target
X = df[["base_ctr", "brand_score", "offer_score"]]
y = df["clicks"]

# Train model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=4)
model.fit(X, y)

# Save model
model.save_model("xgb_model.json")
print("✅ Model saved as xgb_model.json")
