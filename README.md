
# Educational Program Impact Analytics System

## Overview

This project simulates and analyses data from a large-scale online educational program (inspired by Neuromatch-style academies). It demonstrates how to build a **complete data analytics pipeline** to evaluate program impact, ensure data quality, and support decision-making.

The system handles:

* Multi-source, multi-year datasets
* Data cleaning and validation
* Feature engineering
* Metric definition and standardisation
* Equity and accessibility analysis
* Reproducible pipelines and reporting

---

## Objectives

* Build a **robust data pipeline** for messy, real-world educational data
* Define **clear and consistent metrics** to evaluate program success
* Analyse **student engagement, completion, and learning outcomes**
* Investigate **equity and accessibility**, including disability-related outcomes
* Communicate insights through **reports and dashboards**

---

## Project Structure

```
neuromatch-impact-project/
│
├── data/
│   ├── raw/                # Simulated raw datasets
│   ├── processed/          # Cleaned, student-level dataset
│
├── notebooks/
│   ├── 00_generate_data.ipynb
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_analysis.ipynb
│   ├── 04_metrics_validation.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── data_quality.py
│   ├── feature_engineering.py
│   ├── metrics.py
│   ├── analysis.py
│   ├── config.py
│
├── dashboard/
│   └── app.py              # Interactive dashboard (Streamlit)
│
├── reports/
│   ├── impact_report.ipynb
│   └── figures/
│
├── run_pipeline.py         # End-to-end pipeline
├── requirements.txt
└── README.md
```

---

## Datasets

The project simulates three core datasets:

### 1. Applications

* Student demographics (country, education level, gender)
* Acceptance status
* Disability status and type

### 2. Daily Surveys

* Attendance
* Engagement scores
* Perceived difficulty

### 3. Final Survey

* Completion status
* Satisfaction
* Self-reported learning

### Accessibility Data

Disability is modelled using broad categories:

* visual, hearing, motor, cognitive, multiple, none, prefer_not_to_say

This allows meaningful **equity and accessibility analysis** while maintaining simplicity and privacy.

> Note: All data is simulated for demonstration purposes only.

---

## Data Pipeline

The pipeline is implemented in `run_pipeline.py` and includes:

1. **Data Loading**
2. **Automated Data Quality Checks**

   * Missing values
   * Duplicates
   * Category validation
   * Range checks
   * Referential integrity
3. **Data Cleaning & Standardization**
4. **Dataset Merging**
5. **Feature Engineering**
6. **Metric Computation**
7. **Processed Data Export**

Run the full pipeline:

```bash
python run_pipeline.py
```

---

## Feature Engineering

Student-level features include:

* `attendance_rate`
* `avg_engagement`
* `engagement_variability`
* `avg_difficulty`
* `early_engagement`
* `total_days`

These features capture **behaviour, consistency, and progression over time**.

---

## Metrics

The project defines standardised metrics for program evaluation:

### Core Metrics

* **Completion Rate**
* **Engagement Index** (normalized)
* **Learning Gain** (engagement-weighted)
* **Satisfaction Score**

### Risk Metrics

* **Dropout Rate**
* **Early Engagement Indicators**

### Equity Metrics

* **Equity Gap** (across groups)
* **Disability Completion Gap**

All metric definitions are centralised and reusable.

---

## Analysis

The analysis focuses on:

* Program effectiveness (engagement, completion, learning)
* Dropout patterns and early warning signals
* Group-level differences (country, education level)
* Accessibility and disability-related outcomes

---

## Dashboard

An interactive dashboard (Streamlit) was developed to 
* Analyse program performance
* Identify dropout patterns
* Evaluate equity across participant groups.
* Integrates multi-source data and
* Provides insights for improving retention and accessibility.

Run locally:

```bash
streamlit run dashboard/app.py
```

---

## Key Highlights

* End-to-end **data ownership pipeline**
* Automated **data quality validation**
* Thoughtful **metric design**
* Focus on **equity and accessibility**
* Clear **decision-oriented insights**
* Fully **reproducible and modular**

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* Add predictive modelling for dropout risk
* Integrate real datasets
* Expand dashboard interactivity
* Automate report generation

---

## Motivation

This project was designed to reflect the challenges of analysing educational program data in a global, inclusive environment. It emphasises not just technical skills, but also:

* clarity in communication
* responsibility in handling sensitive data
* and the ability to translate data into actionable insights

---

## Contact

Feel free to reach out or connect if you’d like to discuss this project or related work.
