import os
import resend
from dotenv import load_dotenv
import base64

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to_email, company, pdf_path):

    with open(pdf_path, "rb") as f:
        pdf_data = base64.b64encode(f.read()).decode("utf-8")

    params = {
        "from": "onboarding@resend.dev",
        "to": [to_email],
        "subject": f"{company} AI Audit Report",
        "html": f"""
        <h2>Your AI Audit Report is Ready</h2>

        <p>
            Please find attached your personalized AI automation audit report for {company}.
        </p>
        """,
        "attachments": [
            {
                "filename": f"{company}_audit_report.pdf",
                "content": pdf_data
            }
        ]
    }

    email = resend.Emails.send(params)

    return email