#encoding: utf-8
from django.core.mail import EmailMessage


def enviar_mail_cambio_de_datos(request):
    subject = "El cliente %s solicita cambio de datos personales" % request.user.get('usuario')
    body = "Estos son los nuevos datos del cliente:\n"
    from_email = "jose@o2w.es"
    to_email = "jose@o2w.es"
    for key, val in request.DATA.items():
        body += "%s: %s\n" % (key, val)

    mail = EmailMessage(subject, body, from_email, [to_email])
    mail.send()


def enviar_mail_de_contacto(request):
    subject = "El cliente %s solicita contacto" % request.user.get('usuario')
    body = "Estos son los datos del cliente:\n"
    from_email = "jose@o2w.es"
    to_email = "jose@o2w.es"

    for key, val in request.DATA.items():
        body += "%s: %s\n" % (key, val)

    mail = EmailMessage(subject, body, from_email, [to_email])
    mail.send()
