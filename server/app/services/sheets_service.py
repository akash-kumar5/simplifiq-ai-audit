import gspread

from datetime import datetime

from oauth2client.service_account import (
    ServiceAccountCredentials
)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

import os
import json

credentials_dict = json.loads(
    os.getenv("GOOGLE_CREDENTIALS")
)

credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict,
    scope
)

client = gspread.authorize(credentials)

sheet = client.open(
    "AI Audit Leads"
).sheet1


def log_lead(data, status):
    print("Logging lead to Google Sheets...")

    row = [

        str(datetime.now()),

        str(data.name),

        str(data.email),

        str(data.company),

        str(data.website),

        str(data.industry).strip() if data.industry else "Not Provided",
        
        str(data.challenge).strip() if data.challenge else "Not Provided",

        status
    ]

    sheet.append_row(row)
    print("Lead logged successfully.")