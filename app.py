import smtplib
import email.message
from dotenv import load_dotenv
import os


load_dotenv()


def send_email():
    try:
        # Corpo da Mensagem
        body_email = """
        <h3>Olá, este é um teste para enviar emails com Python</h3>
        """

        msg = email.message.Message()
        msg['Subject'] = "Teste Email com Python"    # Assunto do Email
        msg['From'] = os.environ['SMTP_EMAIL_FROM']  # Remetente
        msg['To'] = 'destinatario@gmail.com'         # Destinatário
        passwd = os.environ['SMTP_PASSWORD_EMAIL']   # Servidor SMTP
        msg.add_header('Content-Type', 'text/html')  # Cabeçalho da requisição
        msg.set_payload(body_email)
        
        
        serv_email = smtplib.SMTP(os.environ['SMTP_SERVER'])
        serv_email.starttls()
        serv_email.login(msg['From'], passwd)
        serv_email.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
        print('Email Enviado!')
        serv_email.quit()
    except:
        print('Erro ao enviar o email!')
    

send_email()