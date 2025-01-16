from Scraper import Soup
from sending_email_reminder import MailSender

URL = "https://www.amazon.com/SAMSUNG-Technology-Intelligent-Turbowrite-MZ-V9S2T0B/dp/B0DHLCRF91/ref=sr_1_10?dib=eyJ2IjoiMSJ9.EoJi2KGtyKkHzukpwyJrsl175r-A3P4yOeGTZX-HRIQlMVreLOsxBv_ykFjm70R2_AudO8cDyEfA_gYNDMXOEudsdrPLTyNdshVE1dtF0z9oWrR1wSAz_lxHSgo7jsY4L5ehHb5VeEFz3idwbRGDofPZozfQI5_Mj4D_AzRYY-G1Ac-TsraZUdR1cVU2XfOOAJxlI1WPEOxNZl_axJKKWvJCAdVWcecH2fyuvuPaUsWHJK-VFJE4Yf_CGvL82WTsxcXzORTU_I__T_MrlNfd0QkulA0rHZxT2Z1kK1TRdLSFTiyF_gYVCth3goVNAxnJEGVeDlrFDBJRv3hQrWWM2-IhRr8yTlmFERGnhEQzbH0.COu_hVYiJhVfuZYbm7Soc3Z8JkxhUBmgwxG5v7X_5V4&dib_tag=se&qid=1736782074&s=computers-intl-ship&sr=1-10&th=1"
obj = Soup(web_address=URL)
price =float(obj.soup())

mail = MailSender()

if 90 < price < 120:
    message = f"""This is a reminder for you to buy your items. 
                  follow the following link to buy {URL}"""
    mail.mail_sender(message=message)
else: 
    message = f"""This is just a reminder, 
    the needed price is not reached yet. Current price is ${price}."""
    mail.mail_sender(message=message)

