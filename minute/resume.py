from datetime import datetime
import pdfkit
from jinja2 import Template
from minute.models import Meeting
from minute.template_serializers import TemplateMeetingSerializer


def convert_to_date(date):
    if date:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        return date.strftime('le %d/%m/%Y à %H:%M')
    return None


def convert_to_name(first_name, last_name):

    return f"{first_name} {last_name}"


def convert_html_to_pdf(html):
    return pdfkit.from_string(html, False)


def generate_html(data):
    data = {
        **data, 'convert_to_date': convert_to_date, 'convert_to_name': convert_to_name
    }
    with open("minute/template/minute_template_body.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    result = template.render(data)
    return result


def generate_pdf(meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)
    model_data = TemplateMeetingSerializer(instance=meeting).data
    html = generate_html(model_data)
    pdf = convert_html_to_pdf(html)
    return pdf

