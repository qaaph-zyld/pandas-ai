import pandas as pd
from data.sample_dataframe import dataframe

from pandasai import PandasAI
from pandasai.helpers.datasource import sheets_input
from pandasai.llm.openai import OpenAI

df = sheets_input("1IRGJFUpCR0-9tPDk2MgPjQCtNft_4a8B1fHgYK7_LM8", "second")
print(df.dtypes)
# llm = OpenAI()
# pandas_ai = PandasAI(llm, verbose=True, conversational=False)

# response = pandas_ai.run(
#     df,
#     "Calculate the sum of the gdp of north american countries",
# )
# print(response)
Output: 20901884461056
