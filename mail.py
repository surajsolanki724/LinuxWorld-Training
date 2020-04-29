#!/usr/bin/python36
#for executable

import smtplib

username="linuxsmtp123@gmail.com"
password="redhat123"
#dir(smtplib)
mail_servar=smtplib.SMTP(host='smtp.gmail.com',port=587)
mail_servar.starttls()
mail_servar.login(username,password)
text="hello suraj how are you somebody are hack yor data"
mail_servar.sendmail(username,"sssolanki724@gmail.com",text)
mail_servar.quit()
