import base64
import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail, Attachment, FileName, FileType, FileContent, ContentId,\
    Disposition
import os


def send_mail(dest_mail, message_content, message_subject, message_attachment=None):
    api_key = os.getenv("SENDGRID_API_KEY")
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email(os.getenv("MEETING_API_KEY"))
    to_email = To(dest_mail)
    subject = message_subject
    content = Content("text/html", message_content)
    mail = Mail(from_email, to_email, subject, content)

    if message_attachment:
        encoded = base64.b64encode(message_attachment).decode()
        attachment_file = Attachment()
        attachment_file.file_content = FileContent(encoded)
        attachment_file.file_type = FileType('application/pdf')
        attachment_file.file_name = FileName('Compte rendu de réunion.pdf')
        attachment_file.disposition = Disposition('attachment')
        attachment_file.content_id = ContentId('id')
        mail.attachment = attachment_file

    sg.client.mail.send.post(request_body=mail.get())

