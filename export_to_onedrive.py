# Databricks notebook source
import pandas as pd
from sqlalchemy import create_engine
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext

# Connect to PostgreSQL
engine = create_engine('postgresql://user:password@localhost:5432/aquarius_db') # real URL is removed
query = "SELECT * FROM timesheets"
df = pd.read_sql(query, engine)

# Connect to OneDrive via SharePoint API
client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
site_url = "https://company.sharepoint.com/sites/TimesheetData"    #real URL is removed
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

# Append CSV ----------
file_url = "/Shared Documents/timesheet_data.csv"

# Convert DataFrame to CSV 
df.to_csv("timesheet_data.csv", index=False)

# Upload CSV to OneDrive (overwrite for auto-refresh)
with open("timesheet_data.csv", 'rb') as file:
ctx.web.get_file_by_server_relative_url(file_url).upload(file).execute_query()
