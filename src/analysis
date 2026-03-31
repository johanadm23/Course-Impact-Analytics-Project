def dropout_risk(df):
    return df[df["attendance_rate"] < 0.5]


def early_engagement_analysis(df):
    return df.groupby("early_engagement")["completion"].mean()
