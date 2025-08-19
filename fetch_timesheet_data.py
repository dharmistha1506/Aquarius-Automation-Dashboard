# Databricks notebook source

import requests
import pandas as pd
from sqlalchemy import create_engine

# Fetch data from Aquarius API (original URL, and Token is removed)
api_url = "https://ABC-api.company.com/timesheets"
headers = {"Authorization": "Bearer <API_TOKEN>"} 

response = requests.get(api_url, headers=headers)
data = response.json() 

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Data validation
df = df[df['hours_worked'] > 0]  # remove invalid hours
df['date_worked'] = pd.to_datetime(df['date_worked'], errors='coerce')
df = df.dropna(subset=['date_worked'])  # drop invalid dates

# Insert into PostgreSQL
engine = create_engine('postgresql://<user>:<password>@localhost:6564/mydb')  # original removed

df.to_sql('timesheets', engine, if_exists='append', index=False)
