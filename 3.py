from email.message import EmailMessage
import ssl
import smtplib as sm


def sendMail(email):
        email_from = "adithya.acharya@funwithprogramming.com"
        email_password="SangamOne$1"
        email_to=email

        subject="type_Trivia: Finish Creating your account!"

        body = ""

        em=EmailMessage()
        em["From"]= email_from
        em['To']=email_to
        em["Subject"]=subject
        em.set_content(body,subtype="html")
        context = ssl.create_default_context()




        sm.SMTP_SSL('mail.funwithprogramming.com',465,context=context)
        sm.login(email_from,email_password)
        sm.sendmail(email_from, email_to, em.as_string())
        

sendMail("ckuthyar@gmail.com")

