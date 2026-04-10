class MetricsCalculator:
    
    def __init__(self, df):
        self.df = df
    
    def completion_rate(self):
        return self.df["completion"].mean()
    
    def engagement_index(self):
        return self.df["avg_engagement"].mean() / 5
    
    def learning_gain(self):
        return (
            self.df["learning"] * 
            self.df["attendance_rate"]
        ).mean()
    
    def equity_gap(self, col):
        grouped = self.df.groupby(col)["completion"].mean()
        return grouped.max() - grouped.min()

    def avg_satisfaction(self):
        return self["satisfaction"].mean()
