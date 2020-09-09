import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *


def send_mail(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(subject, 'utf-8')

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename="report.html"'
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.connect(smtp_server, 465)
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, to_addr, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
