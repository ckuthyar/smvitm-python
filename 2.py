from email.message import EmailMessage
import ssl
import smtplib


def sendMail(email):
        email_from = "adithya.acharya@funwithprogramming.com"
        email_password=""
        email_to=email

        subject="type_Trivia: Finish Creating your account!"

        body = f""" <!DOCTYPE html>
<html>
    <body>
    <div> <img src="static/type_trivia (1).svg"> </div>
    <h1>
        type_Trivia: Finish Creating your account!
    </h1>    
        
    <h2>    
        Here's your verification code
    </h2>
    <h1>
        
    </h1>
    </body>
    </html>
        """

        em=EmailMessage()
        em["From"]= email_from
        em['To']=email_to
        em["Subject"]=subject
        em.set_content(body,subtype="html")
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('mail.funwithprogramming.com',465,context=context) as smtp:
            smtp.login(email_from,email_password)
            smtp.sendmail(email_from,email_to,em.as_string())

sendMail("adithya.acharya@funwithprogramming.com")
sendMail("samyam.pejathaya@funwithprogramming.com")






