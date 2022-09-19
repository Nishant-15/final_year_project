from pandas_profiling import ProfileReport
import pandas as pd
df = pd.read_csv("dataset.csv")

profile = ProfileReport(df, title="Traffic Volume count Data analysis Report", explorative=True)
profile.to_file("Analysis.html")