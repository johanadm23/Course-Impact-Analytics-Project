def build_student_features(df):
    student_df = df.groupby("student_id").agg({
        "day": "count",  # attendance signal
        "engagement_score": ["mean", "std"],
        "difficulty": "mean",
        "completion": "max",
        "satisfaction": "mean",
        "self_reported_learning": "mean",
        "has_disability": "max",
        "disability_type": "first",
        "country": "first",
        "year": "first"
    })
    
    student_df.columns = [
        "total_days",
        "avg_engagement",
        "engagement_variability",
        "avg_difficulty",
        "completion",
        "satisfaction",
        "learning",
        "has_disability",
        "disability_type",
        "country",
        "year"
    ]
    # attendance rate 
    student_df["attendance_rate"] = student_df["total_days"] / 15 # course lasts 15 days
    
    return student_df.reset_index()
