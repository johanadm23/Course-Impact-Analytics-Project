import streamlit as st
import pandas as pd

st.set_page_config(page_title="Program Impact Dashboard", layout="wide")

st.title("Educational Program Impact Dashboard")
st.markdown("Analyze program performance, engagement, and equity outcomes")

@st.cache_data
def load_data():
    return pd.read_csv("../data/processed/student_level.csv")

df = load_data()
st.sidebar.header("Filters")

year_filter = st.sidebar.selectbox(
    "Select Year",
    options=["All"] + sorted(df["year"].unique().tolist())
)

country_filter = st.sidebar.multiselect(
    "Select Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

disability_filter = st.sidebar.selectbox(
    "Disability Status",
    options=["All", "With Disability", "Without Disability"]
)

filtered_df = df.copy()

if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year"] == year_filter]

filtered_df = filtered_df[filtered_df["country"].isin(country_filter)]

if disability_filter == "With Disability":
    filtered_df = filtered_df[filtered_df["has_disability"] == 1]
elif disability_filter == "Without Disability":
    filtered_df = filtered_df[filtered_df["has_disability"] == 0]

completion_rate = filtered_df["completion"].mean()
engagement = filtered_df["avg_engagement"].mean()
satisfaction = filtered_df["satisfaction"].mean()
dropout_rate = 1 - completion_rate

col1, col2, col3, col4 = st.columns(4)

col1.metric("Completion Rate", f"{completion_rate:.2f}")
col2.metric("Engagement", f"{engagement:.2f}")
col3.metric("Satisfaction", f"{satisfaction:.2f}")
col4.metric("Dropout Rate", f"{dropout_rate:.2f}")

st.subheader("Engagement vs Completion")

chart_data = filtered_df[["completion", "avg_engagement"]]

st.bar_chart(chart_data.groupby("completion").mean())

st.subheader("Early Engagement vs Completion")

early = filtered_df.groupby("completion")["early_engagement"].mean()

st.bar_chart(early)

st.subheader("Completion Rate by Country")

country_data = filtered_df.groupby("country")["completion"].mean().sort_values()

st.bar_chart(country_data)

st.subheader("Accessibility Insights")

disability_data = filtered_df.groupby("has_disability")["completion"].mean()

st.bar_chart(disability_data)

if len(disability_data) == 2:
    gap = disability_data.max() - disability_data.min()
    st.metric("Disability Equity Gap", f"{gap:.2f}")

st.subheader("Participation Length (Days)")

st.bar_chart(filtered_df["total_days"].value_counts().sort_index())

st.subheader("Key Insights")

if completion_rate < 0.7:
    st.warning("Completion rate is below expected levels")

if gap > 0.1:
    st.warning("Significant equity gap detected (disability)")

if engagement < 3:
    st.warning("Low engagement levels detected")

st.subheader("Sample Data")

st.dataframe(filtered_df.head(100))
