class DataQualityReport:
    def __init__(self, name):
        self.name = name
        self.errors = []
        self.warnings = []
    
    def add_error(self, msg):
        self.errors.append(msg)
    
    def add_warning(self, msg):
        self.warnings.append(msg)
    
    def summary(self):
        print(f"\n Data Quality Report: {self.name}")
        print("-" * 40)
        
        if not self.errors and not self.warnings:
            print(" No issues found")
        
        if self.errors:
            print("\n Errors:")
            for e in self.errors:
                print(f"- {e}")
        
        if self.warnings:
          print("\n⚠️ Warnings:")
          for w in self.warnings:
            print(f"- {w}")
        # check mising values
        def check_missing(df, report, threshold=0.1):
          missing = df.isnull().mean()
          for col, ratio in missing.items():
            if ratio > threshold:
              report.add_warning(f"{col} has {ratio:.1%} missing values")

        # check duplicate values
        def check_duplicates(df, report, subset):
          dup = df.duplicated(subset=subset).sum()
          if dup > 0:
            report.add_warning(f"{dup} duplicate rows found for {subset}")

        # validate categories
        def check_categories(df, col, valid_values, report):
          invalid = ~df[col].isin(valid_values)
          if invalid.sum() > 0:
            report.add_warning(
              f"{invalid.sum()} invalid values in {col}: "
              f"{df.loc[invalid, col].unique()}"
            )

        # check ranges
        def check_range(df, col, min_val, max_val, report):
          invalid = (df[col] < min_val) | (df[col] > max_val)
          if invalid.sum() > 0:
            report.add_error(
              f"{invalid.sum()} values out of range in {col}"
            )
        # renferential check (may not use this yet)
        def check_foreign_key(child_df, parent_df, key, report):
          missing_keys = ~child_df[key].isin(parent_df[key])
          if missing_keys.sum() > 0:
            report.add_error(
              f"{missing_keys.sum()} {key}s in child not found in parent"
            )

        # validate datasets
        def validate_applications(df):
          report = DataQualityReport("Applications")
    
          check_duplicates(df, report, ["student_id"])
    
          check_categories(
            df, "education_level",
            ["undergrad", "masters", "phd"],
            report
           )
          return report
          
        def validate_daily(df, applications):
          report = DataQualityReport("Daily Surveys")
          check_missing(df, report)
          check_range(df, "engagement_score", 1, 5, report)
          check_foreign_key(df, applications, "student_id", report)
          return report
          
        def validate_final(df, applications):
          report = DataQualityReport("Final Survey")
          check_range(df, "satisfaction", 1, 5, report)
          check_foreign_key(df, applications, "student_id", report)
          return report


         



    
