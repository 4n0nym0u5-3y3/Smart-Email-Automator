# Smart Email Automator

**Smart Email Automator** is a Python-based script that automates the process of sending emails with attachments and images at specified intervals. It supports flexible scheduling, logging, and easy configuration via a JSON file.

## Features

- **Configuration via JSON**: Customize SMTP settings, email content, and schedule in a user-friendly JSON file.
- **Logging**: Keep track of email activities, including successful sends and errors, in a log file.
- **Flexible Scheduling**: Schedule emails to be sent at specific intervals, daily, or weekly.
- **Image and Attachment Support**: Easily attach multiple images and files to your emails.

## Requirements

- Python 3.x
- `smtplib`, `schedule`, `json`, `logging`
  
Install the required Python libraries if you haven't already:
```bash
pip install schedule
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone 'link'
   cd smart-email-automator
   ```

2. **Configure your email settings**:
   - Open `email_config.json` and update the following:
     - `smtp_server`: SMTP server address (e.g., `smtp.gmail.com` for Gmail).
     - `smtp_port`: SMTP port (e.g., `587` for TLS).
     - `email`: Your email address.
     - `password`: Your email password (consider using environment variables for security).
     - `subject`: The subject of your email.
     - `body`: The text body of your email.
     - `images`: List of paths to images you want to include.
     - `attachments`: List of paths to files you want to attach.
     - `recipients`: List of recipient email addresses.
     - `schedule`: Define your schedule for sending emails.

3. **Run the script**:
   ```bash
   python smart_email_automator.py
   ```

## Configuration

The email settings and schedule are stored in the `email_config.json` file:

```json
{
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "email": "your_email@gmail.com",
    "password": "your_password",
    "subject": "Scheduled Email",
    "body": "This is an automated email sent by Smart Email Automator.",
    "images": [
        "path/to/image1.jpg",
        "path/to/image2.png"
    ],
    "attachments": [
        "path/to/file1.pdf",
        "path/to/file2.docx"
    ],
    "recipients": [
        "recipient1@example.com",
        "recipient2@example.com"
    ],
    "schedule": [
        {
            "type": "interval",
            "interval": 10
        },
        {
            "type": "daily",
            "time": "08:00"
        },
        {
            "type": "weekly",
            "day": "Friday",
            "time": "14:00"
        }
    ]
}
```

### Schedule Types

- **Interval**: Sends emails every specified number of minutes.
- **Daily**: Sends emails at a specific time every day.
- **Weekly**: Sends emails on a specific day and time each week.

### Example Configurations

1. **Send an email every 10 minutes**:
   ```json
   {
       "type": "interval",
       "interval": 10
   }
   ```

2. **Send an email every day at 8:00 AM**:
   ```json
   {
       "type": "daily",
       "time": "08:00"
   }
   ```

3. **Send an email every Friday at 2:00 PM**:
   ```json
   {
       "type": "weekly",
       "day": "Friday",
       "time": "14:00"
   }
   ```

## Logging

The script logs all actions, including successful email sends and any errors, to `email_automator.log`. This file is automatically created in the same directory as the script.

## Security Considerations

- **Email Password**: For security reasons, avoid hardcoding your email password. Consider using environment variables or a secure vault.
- **Attachments**: Be mindful of the files you attach to avoid accidentally sending sensitive information.

