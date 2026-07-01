"""Yellow Pin Travel Website"""

import os
import json
from flask import Flask, render_template, send_from_directory

import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from pathlib import Path


app = Flask(__name__)

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


# def main():
#    get_email_creds()
#    gmail_send_message_jen()

# Test comment for branch commit

def get_email_creds():
    """Gets gmail API authentication token."""

    # Identify file paths
    creds_path = Path(".") / "secrets" / "credentials.json"
    token_path = Path(".") / "secrets" / "token.json"

    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    return creds


def gmail_send_message_jen():
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = get_email_creds()

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content("This is automated draft mail")

        message["To"] = "mspaits@gmail.com"
        message["From"] = "mspaitsdev@gmail.com"
        message["Subject"] = "Test from YPT"

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


@app.route("/")
def index():
    """Home page"""

    return render_template('index.html')


@app.route("/about")
def about():
    """About page"""

    return render_template('about.html')


@app.route("/services")
def services():
    """Services page"""

    return render_template('services.html')


@app.route("/contact")
def contact():
    """Contact page"""

    return render_template('contact.html')


@app.route("/thank-you")
def thank_you():
    """Thank you page"""

    return render_template('thank-you.html')


@app.route("/privacy")
def privacy():
    """Privacy page"""

    return render_template('privacy.html')


@app.route("/terms")
def terms():
    """Terms and conditions page"""

    return render_template('terms.html')


@app.route("/accessibility")
def accessability():
    """Accessibility page"""

    return render_template('accessibility.html')


@app.route("/sitemap.xml")
def sitemap():
    """Sitemap for search engines"""

    return send_from_directory(app.root_path, "sitemap.xml", mimetype="application/xml")


@app.route("/robots.txt")
def robotstxt():
    """Robots.txt for search engines"""

    return send_from_directory(app.root_path, "robots.txt", mimetype="text/plain")


@app.route("/picsapi")
def picsapi():
    """API route to send img file paths and names"""

    path = "static/images/rand_stock"
    file_list = os.listdir(path)

    path_list = []
    for file in file_list:
        path_list.append(os.path.join(path, file))

    json_list = json.dumps(path_list)

    return json_list


if __name__ == "__main__":
    app.run(debug=True)
    # main()
