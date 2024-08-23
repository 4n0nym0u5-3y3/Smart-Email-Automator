import schedule
import time
import smtplib
import json
import logging
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os

# Configure logging
logging.basicConfig(filename='email_automator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file):
    """Loads email configuration from a JSON file."""
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def create_email(config):
    """Creates an email based on the provided configuration."""
    msg = MIMEMultipart()
    msg['Subject'] = config['subject']
    msg.attach(MIMEText(config['body'], 'plain'))

    if config.get('images'):
        for img_path in config['images']:
            with open(img_path, 'rb') as img_file:
                img_data = img_file.read()
            msg.attach(MIMEImage(img_data, name=os.path.basename(img_path)))

    if config.get('attachments'):
        for attachment_path in config['attachments']:
            with open(attachment_path, 'rb') as attachment_file:
                attach_data = MIMEApplication(attachment_file.read(),
                                              name=os.path.basename(attachment_path))
            attach_data['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(attach_data)

    return msg

def send_email(config):
    """Connects to the SMTP server and sends an email."""
    try:
        with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as smtp:
            smtp.starttls()
            smtp.login(config['email'], config['password'])
            msg = create_email(config)
            smtp.sendmail(config['email'], config['recipients'], msg.as_string())
            logging.info(f"Email sent successfully to {', '.join(config['recipients'])}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def schedule_emails(config):
    """Schedules email sending based on the provided configuration."""
    for schedule_item in config['schedule']:
        if schedule_item['type'] == 'interval':
            schedule.every(schedule_item['interval']).minutes.do(send_email, config=config)
        elif schedule_item['type'] == 'daily':
            schedule.every().day.at(schedule_item['time']).do(send_email, config=config)
        elif schedule_item['type'] == 'weekly':
            day = getattr(schedule.every(), schedule_item['day'].lower())
            day.at(schedule_item['time']).do(send_email, config=config)
        logging.info(f"Scheduled email: {schedule_item}")

if __name__ == "__main__":
    # Load configuration
    config = load_config('email_config.json')

    # Schedule emails
    schedule_emails(config)

    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
