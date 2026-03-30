def clean_countries(df):
    mapping = {
        "United States": "USA",
        "US": "USA",
        "Brasil": "Brazil",
        "United Kingdom": "UK"
    }
    df["country"] = df["country"].replace(mapping)
    return df


def remove_duplicates(df):
    return df.drop_duplicates(subset=["student_id"])
