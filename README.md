# AI Business Audit Automation System

An AI-powered lead intake and business audit automation platform built using FastAPI, Next.js, OpenAI, Google Sheets API, and Resend.
This system automates the complete workflow from lead submission to personalized AI-generated business audit delivery.

---

# Features
* Modern Next.js frontend
* FastAPI backend architecture
* Website scraping and company enrichment
* AI-generated business insights using LLMs
* Personalized PDF audit generation
* Automated email delivery with PDF attachment
* Google Sheets lead logging (mini CRM workflow)
* Responsive and clean UI
* Automated end-to-end workflow

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
PDF Audit Report Creation
        ↓
Automated Email Delivery
        ↓
Google Sheets Lead Logging
```

---

# Tech Stack

## Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Axios

## Backend

* FastAPI
* Python
* BeautifulSoup
* OpenAI SDK
* Jinja2
* xhtml2pdf
* Resend API
* Google Sheets API

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

## 1. Clone Repository

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
```

---

# Google Sheets Integration

## Steps

1. Create Google Cloud Project
2. Enable Google Sheets API
3. Create Service Account
4. Download credentials JSON
5. Rename to:

```txt
credentials.json
```

6. Place inside:

```txt
server/
```

7. Share Google Sheet with service account email.

---

# Email Delivery

Email delivery is implemented using Resend.

Due to Resend sandbox limitations, emails can currently only be sent to verified recipient addresses unless a custom domain is configured.

---

# AI Audit Report

The generated report includes:

* Company Overview
* Business Observations
* AI Automation Opportunities
* Recommended AI Solutions
* Expected Business Impact

---


# Future Improvements

* Advanced web scraping
* Multi-page PDF reports
* AI-powered lead scoring
* Company logo extraction
* Google Drive PDF archiving
* Authentication system
* Admin dashboard
* Database integration
* Async background job queue

---

# Assumptions

* Public company websites are accessible.
* AI-generated insights are advisory in nature.
* Users provide valid company website URLs.

---

# Limitations

* Some websites may block scraping.
* AI output quality depends on available website content.
* Email sandbox restrictions apply in testing mode.

---

# Author

Akash Kumar

Built as part of the SimplifiIQ AI Software Developer Intern Assessment.
