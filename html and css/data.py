import pandas as pd
df = pd.read_csv('Resources/cities.csv')
df.to_html('csvtodata.html', index=False,classes='table table-light table-hover')