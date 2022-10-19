import smtplib
mail = smtplib.SMTP('smtp.gmail.com','587')
mail.starttls()
mail.login("send_mail_name", "****************") # enter your google app password not your mail password
message = "message_you_want_to_send"
mail.sendmail("sending_mail" ,"receiving_mail", message)
mail.quit()