import smtplib
sender_mail = input("enter your sender's mail : ")
password = input("enter your sender's mail password :")
message = input("enter the message you want to send :")
receiver_mail = input("enter receiver's mail :")
mail = smtplib.SMTP('smtp.gmail.com','587')
mail.starttls()
mail.login( sender_mail , password ) # enter your google app password not your mail password
mail.sendmail( sender_mail, receiver_mail, message)
mail.quit()