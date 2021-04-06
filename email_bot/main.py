import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('gokulpollachi25@gmail.com','pollachi25')
server.sendmail('gokulpollachi25@gmail.com',
                'pushpamlogu@gmail.com',
                'hi am gokul L')
print("gmail sent")

