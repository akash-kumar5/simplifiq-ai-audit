from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, EmailStr
from app.services.pdf_service import generate_pdf
from app.services.scraper import scrape_company_website
from app.services.ai_service import generate_ai_insights
from app.services.email_service import send_email
from app.services.sheets_service import log_lead
from app.services.drive_service import upload_pdf

router = APIRouter()


class LeadData(BaseModel):
    name: str
    email: EmailStr
    company: str
    website: HttpUrl
    industry: str | None = None
    challenge: str | None = None


@router.post("/submit-lead")
async def submit_lead(data: LeadData):

    website_data = scrape_company_website(data.website)

    ai_insights = generate_ai_insights(
        company=data.company,
        industry=data.industry,
        challenge=data.challenge,
        scraped_content=website_data.get("content", ""),
    )

    pdf_path = generate_pdf(company=data.company, insights=ai_insights)

    upload_pdf(pdf_path, f"{data.company}_audit_report.pdf")
    email_response = send_email(
        to_email=data.email, company=data.company, pdf_path=pdf_path
    )

    log_lead(data, "Completed")

    return {
        "success": True,
        "message": "Lead processed successfully",
        "pdf_path": pdf_path,
        "ai_insights": ai_insights,
        "email_response": email_response,
    }


#     {
#   "name": "Akash",
#   "email": "akash@gmail.com",
#   "company": "Notion",
#   "website": "https://notion.so",
#   "industry": "SaaS",
#   "challenge": "Improve workflow automation"
# }
