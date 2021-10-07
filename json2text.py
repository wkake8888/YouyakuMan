import pandas as pd
df = pd.read_json('2020-12.test.json')
df.to_csv('./test_text.txt', index=False)