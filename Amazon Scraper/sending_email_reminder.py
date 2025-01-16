import smtplib

class MailSender():
    def __init__(self):
        self.user_name = "" #senders email
        self.user_password = "" #app password
        self.client_email = "" #recievers email

    def mail_sender(self, message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=self.user_name, password= self.user_password)
        connection.sendmail(from_addr=self.user_name, to_addrs=self.client_email, msg =f"Subject: Amazon Price change reminder\n\n {message}")