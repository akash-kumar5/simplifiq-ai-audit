# AI Business Audit Automation Platform

An end-to-end AI-powered business audit automation system built using FastAPI, Next.js, OpenAI, Google Sheets API, Google Drive API, and Resend.

The platform automates the complete lead-to-report workflow by collecting prospect information, enriching company data through website scraping, generating AI-driven business insights, creating personalized PDF audit reports, delivering reports via email, and logging leads into Google Sheets.

---

# Features

- AI-powered business audit generation
- Modern Next.js frontend
- FastAPI backend architecture
- Company website scraping and enrichment
- Personalized AI-generated business insights
- Dynamic PDF report generation
- Automated email delivery with PDF attachment
- Google Sheets lead logging
- Google Drive PDF archiving
- Responsive and clean user interface
- End-to-end automated workflow

---

# Workflow

```txt
User Form Submission
        ↓
Lead Validation
        ↓
Company Website Scraping
        ↓
AI Insight Generation
        ↓
PDF Report Generation
        ↓
Email Delivery
        ↓
Google Sheets Logging
        ↓
Google Drive Archiving
```

---

# Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Axios

## Backend

- FastAPI
- Python
- OpenAI SDK
- BeautifulSoup
- Jinja2
- xhtml2pdf
- Resend API
- Google Sheets API
- Google Drive API

---

# Project Structure

```txt
client/
│
├── app/
├── public/
└── package.json

server/
│
├── app/
│   ├── routes/
│   └── services/
│
├── templates/
├── reports/
├── requirements.txt
└── .env.example
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <your_repo_url>
cd <repo_name>
```
---

# Frontend Setup

```bash
cd client
npm install
npm run dev
```

Frontend runs on:

```txt
http://localhost:3000
```

---

# Backend Setup

```bash
cd server
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

# Environment Variables

Create a `.env` file inside `server/`

```env
OPENAI_API_KEY=
OPENAI_BASE_URL=
RESEND_API_KEY=
GOOGLE_CREDENTIALS=
```

---

# Google Services Setup

## Google Sheets API

1. Create a Google Cloud project
2. Enable Google Sheets API
3. Create a Service Account
4. Generate credentials
5. Share the target Google Sheet with the service account email

---

## Google Drive API

1. Enable Google Drive API
2. Create a Drive folder for report storage
3. Share the folder with the service account email

---

# AI Audit Report Includes

- Company Overview
- Business Observations
- AI Automation Opportunities
- Recommended AI Solutions
- Expected Business Impact

---

# Future Improvements

- Advanced website scraping
- Multi-page PDF reports
- AI-powered lead scoring
- Company logo extraction
- Authentication system
- Admin dashboard
- Database integration
- Background task queue
- Async processing

---

# Assumptions

- Public company websites are accessible
- Users provide valid website URLs
- AI-generated insights are advisory in nature

---

# Limitations

- Some websites may block scraping
- AI output quality depends on website content availability
- Resend sandbox restrictions apply in testing mode

---

# Author

Akash Kumar

Built for the SimplifiIQ AI Software Developer Intern Assessment.