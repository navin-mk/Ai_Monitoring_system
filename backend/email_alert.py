import smtplib
from email.mime.text import MIMEText

def send_email_alert(message):
    try:
        sender_email = "navinmahendran2004@gmail.com"
        receiver_email = "navinmahendran2004@gmail.com"
        password = "ydezxhddpajammpu"   #paste app password here

        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = "AI Monitoring Alert"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("Email sent!")

    except Exception as e:
        print("Email failed:", e)