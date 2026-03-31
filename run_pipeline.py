import pandas as pd

from src.data_cleaning import *
from src.data_quality import *
from src.feature_engineering import *
from src.metrics import *

# 1. Load data
applications = pd.read_csv("data/raw/applications.csv")
daily = pd.read_csv("data/raw/daily_surveys.csv")
final = pd.read_csv("data/raw/final_survey.csv")

# 2. Validate raw data
reports = [
    validate_applications(applications),
    validate_daily(daily, applications),
    validate_final(final, applications)
]

for r in reports:
    r.summary()
    if len(r.errors) > 0:
        raise ValueError("Pipeline stopped due to errors")

# 3. Clean data
applications = clean_countries(applications)
applications = remove_duplicates(applications)

# 4. Merge
df = daily.merge(applications, on=["student_id", "year"])
df = df.merge(final, on=["student_id", "year"])

# 5. Feature engineering
student_df = build_student_features(df)

# 6. Save processed data
student_df.to_csv("data/processed/student_level.csv", index=False)

# 7. Compute metrics
metrics = MetricsCalculator(student_df)

print("Completion Rate:", metrics.completion_rate())
print("Engagement Index:", metrics.engagement_index())
