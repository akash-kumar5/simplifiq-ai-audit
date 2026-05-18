from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
import os
import markdown

def generate_pdf(company, insights):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("report_template.html")
    formatted_insight = markdown.markdown(insights)
    html_content = template.render(
        company=company,
        insights = formatted_insight
    )


    REPORT_DIR = "reports"

    os.makedirs(REPORT_DIR, exist_ok=True)

    output_path = os.path.join(
    REPORT_DIR,
    f"{company}_audit_report.pdf"
    )

    with open(output_path, "wb") as pdf_file:

        pisa_status = pisa.CreatePDF(
            html_content,
            dest=pdf_file
        )

    if pisa_status.err:
        return None

    return output_path