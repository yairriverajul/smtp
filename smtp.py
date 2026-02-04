import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def send_hola():
    smtp_server = "smtp.gmail.com"
    port = 587
 


 
    sender_email = ("kenyaportout@gmail.com").strip()
    app_password = ("pxhqgixiijmtjqfv").strip()  # no se muestra al escribir
    receiver_email = "yaircostac@hotmail.com"

    if not sender_email or not app_password:
        raise ValueError("Email o App Password vacíos.")

    message = MIMEMultipart()
    message["Subject"] = "Saludo"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText("HOLA", "plain", "utf-8"))

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Correo enviado: HOLA")

send_hola()

