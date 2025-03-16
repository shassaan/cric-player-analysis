from src.schema.schema import Schema
import json
import pandas as pd

schema = Schema()
mapped_data = schema.map_to_schema(json.loads(open('data/sample.json').read()), "json_source")
df = pd.DataFrame()
for player in mapped_data:
    data = player.dict()
    df = pd.concat([df,pd.DataFrame([data])], ignore_index=True)



print(df.dtypes)

df.to_parquet("data/sample.parquet")
