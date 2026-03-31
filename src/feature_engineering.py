def build_student_features(df):
    student_df = df.groupby("student_id").agg({
        "attendance": "mean",
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
        "attendance_rate",
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
    
    return student_df.reset_index()
