import smtplib as s 

ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("EMAILID","PASSWORD")
subject = "TESTING"
body = "HOW ARE YOU ?"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['emailid','emailid']

ob.sendmail('sendermail id', listadd,message)
print("send mail")
ob.quit()
