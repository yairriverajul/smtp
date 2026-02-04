import os
import smtplib
from email.mime.text import MIMEText

TO_EMAIL = "yaircostac@hotmail.com"

def send_one_email():
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("kenyaportout@gmail.com")   # tu correo remitente
    smtp_pass = os.getenv("pxhqgixiijmtjqfv")   # tu clave/app password
     if not smtp_user or not smtp_pass:
        raise RuntimeError("Faltan SMTP_USER/SMTP_PASS en variables de entorno.")

    subject = "Mensaje de prueba"
    body = "Hola, este es un correo de prueba enviado desde Python."

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = TO_EMAIL

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, [TO_EMAIL], msg.as_string())

    print(f"Correo enviado a {TO_EMAIL}")

if __name__ == "__main__":
    send_one_email()



main()
