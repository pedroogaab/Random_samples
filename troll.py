import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

import random


email_origin = input("E-mail: ")
smtp = str(email_origin.split("@")[-1])
if smtp == "gmail.com":
    smtp_server = "smtp.gmail.com"
elif smtp in ["outlook.com", "hotmail.com"]:
    smtp_server = "smtp.office365.com"
else:
    print("Provedor de e-mail não suportado: " + smtp)
    exit()

smtp_port = 587
password = getpass.getpass("Password: ", stream=None)

email_destiny = ""


assuntos_ = ["lindo", "corno", "guei", "estranho", "doido", "bebado", "noia", "doidao", "louco", "jogar de freefas", "nerdao", "ruim de bola", "lambe bolas"]

papos_ = ['couve flor', 'papel higiênico', 'papelão', 'banana', 'computador', 'chave de fenda', 'abacaxi', 'mouse', 'pneu', 'espelho', 'batata', 'lápis', 'lâmpada', 'tesoura', 'cenoura', 'cadeira', 'martelo', 'ventilador', 'geladeira', 'tomate', 'violão', 'meia', 'escova de dentes', 'mochila', 'berinjela', 'copo', 'carro', 'garrafa', 'sofá', 'amendoim']

emails = 0
while True:
    try: 
        n = random.randrange(len(assuntos_)-1)
        assunt = assuntos_[n]
        
        m = random.randrange(len(papos_)-1)
        papos = papos_[m]
        
        msg = MIMEMultipart()
        msg["From"] = email_origin
        msg["To"] = email_destiny
        msg["Subject"] = f"Eaii {assunt}"
        msg.attach(
        MIMEText(f"agora é {papos}", "plain")
        )
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_origin, password)
            server.send_message(msg)
            print("E-mail enviado com sucesso!")
            emails += 1
    except:
        print(f"cabou :( com {emails} enviados")
        break