import smtplib


def send_email():

#Connecting to SMTP server

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    login = 'xxxx'

#Login is your email and password for authentication

    server.login(login, 'password')


#Sending an email, informing that someone has sent me a messege on olx

    msg = 'Someone has sent you a message'

    link = 'https://www.olx.pl/mojolx/wiadomosci'

    server.sendmail(login, 'xyz@abc.com',
                    f'{msg} \n\n\n Check: {link}')
    
    server.quit()
