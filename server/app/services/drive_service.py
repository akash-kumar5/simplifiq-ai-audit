from googleapiclient.discovery import build

from googleapiclient.http import MediaFileUpload

from oauth2client.service_account import (
    ServiceAccountCredentials
)

scope = [
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

service = build(
    "drive",
    "v3",
    credentials=credentials
)

FOLDER_ID = "1C-J2vrUlkcVAZSczvz76EE3kUpU2rU3G"


def upload_pdf(pdf_path, filename):

    file_metadata = {
        "name": filename,
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        pdf_path,
        mimetype="application/pdf"
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    return file.get("id")