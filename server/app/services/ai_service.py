import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def generate_ai_insights(company, industry, challenge, scraped_content):
    industry = industry or "Not specified"
    challenge = challenge or "Not specified"
    prompt = f"""
You are a senior AI automation consultant preparing a highly personalized business audit for a potential client.

Your task is to analyze the company's website content and business context, then generate concise, practical, and business-oriented recommendations.

Avoid generic AI buzzwords.

Focus on:
- operational inefficiencies
- workflow bottlenecks
- repetitive tasks
- customer experience improvements
- lead management
- internal productivity
- automation opportunities
- AI-driven optimization

Company Name:
{company}

Industry:
{industry}

Business Challenge:
{challenge}

Website Content:
{scraped_content}

Generate the response in this exact structure:

# Company Overview
Briefly explain what the company does.

# Key Observations
Mention 3-4 specific observations about their business model, workflow, or product positioning.

# AI Automation Opportunities
Suggest realistic AI automations specific to their business.

# Recommended Solutions
Recommend actionable AI-powered systems, workflows, or integrations.

# Expected Business Impact
Mention measurable outcomes like:
- time savings
- improved lead conversion
- reduced manual work
- faster reporting
- improved customer support

Keep the tone professional, concise, and consulting-oriented.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content