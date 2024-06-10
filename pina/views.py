from django.shortcuts import render
from dotenv import load_dotenv
import os
import base64
import sendgrid
from sendgrid.helpers.mail import *
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib import messages
load_dotenv() 

def index(request):
    return render(request, "pina/index.html")

def portfolio(request):
    return render(request, "pina/portfolio.html")

def crie(request):
    return render(request, "pina/crie.html")

def crie_form(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        telefone = request.POST["telefone"]
        messagem = request.POST["messagem"]
        link = request.POST["link"]
        file = request.FILES.get("file")

        conteudo = f'<p><b>Nome:</b> {nome.upper()} </p>'
        conteudo += f'<p><b>Email:</b> {email}</p>' 
        conteudo += f'<p><b>Telefone:</b> {telefone}</p>' 
        conteudo += f'<p><b>Link Portfolio:</b> {link}</p>' 
        conteudo += f'<p><b>Messagem:</b> {messagem}</p>'

        message = Mail(
            from_email = 'fabricio@rooster.dev.br',
            to_emails = 'mauricio.molina@rooster.dev.br',
            subject = nome.upper() + ' completou o formulario: CRIE CONOSCO',
            html_content = conteudo
        )

        if file:
            file_content = base64.b64encode(file.read()).decode()
            file_name = FileName(file.name)
            file_type = FileType(file.content_type)
            disposition = Disposition('attachment')
            attachment = Attachment(file_content, file_name, file_type, disposition)
            message.attachment = attachment            

        try:
            sg = sendgrid.SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code) 
            print(response.body)
            print(response.headers)

            messages.success(request, "O formulario foi enviado com sucesso!")
            return HttpResponseRedirect(reverse("index"))

        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request,  "pina/crie.html")