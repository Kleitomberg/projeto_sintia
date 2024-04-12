import email.message
import smtplib

from config import Config

config = Config()


def send_email(destino, subject, body): # type: ignore
    """Send an email.

    Parameters:
        destiny (str): Destination email
        subject (str): Subject of the message.
        body (str): The mail's body.
    """
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = config.email
    msg['To'] = destino
    password = config.mail_password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email send to {msg['To']}')  # noqa: T201


def greetings_email(destino, senha, nome): # type: ignore
    template = f"""
    <div>Prezado {nome},</div><br>
    <p>É com grande entusiasmo que damos as boas-vindas ao MagicDocs! Estamos empolgados
    por tê-lo(a) a bordo e esperamos que sua experiência conosco seja tão incrível
    quanto imaginamos.<br>
    No MagicDocs, estamos comprometidos em oferecer uma plataforma
    que simplifica e aprimora a sua jornada na gestão de documentos. Com nossas
    ferramentas intuitivas e recursos inovadores, acreditamos que você encontrará aqui
    a solução perfeita para suas necessidades.<br></p>

    <p>Aqui está sua senha para acesso futuro a nossa plataforma:<br></p>

    <div style="width:100%; display: flex; justify-content:center"><span>{senha}</span><br></div>

    <p>Estamos ansiosos para ver como você usará o MagicDocs para impulsionar a eficiência 
    e a colaboração em seus projetos. Seja parte da nossa comunidade crescente e
    ajude-nos a moldar o futuro da gestão de documentos jurídicos.</p>
    """
    subject = "Seja Bem-vindo ao MagicDocs - Sua Jornada Começa Agora!"

    send_email(destino, subject, template)

def no_credits_email(destino, nome): # type: ignore
    template = f"""
    <div>Prezado {nome},</div><br>
    <p>Informamos que seus créditos no Sintia estão acabando. Para evitar futuros incovenientes, verifique a possibilidade de comprar mais créditos até que a próxima recarga seja efetuada.<br></p>

    <p>Atenciosamente, <br></p>

    <p>Equipe Sintia</p>
    """
    subject = "Seus Créditos estão acabando!"

    send_email(destino, subject, template)

def no_credits_email(destino, nome): # type: ignore
    template = f"""
    <div>Prezado {nome},</div><br>
    <p>Informamos que seus créditos no Sintia acabaram.<br></p>
    <p>A partir de agora qualquer interação de seus clientes com o bot não poderá ser concluída.<br>
        Pedimos desculpas pelos transtornos.
    </p> 
    <p>Atenciosamente, <br></p>

    <p>Equipe Sintia</p>
    """
    subject = "Seus Créditos estão acabando!"

    send_email(destino, subject, template)
