# Criar um Chat - Project Chatai

# --------------- Estrutura Lógica -------------------

# Título: Project Chatai
# Botão iniciar Chat:
    # Pop Up / Modal
# -> Inside Modal: Título: Bem vindo ao Project Chatai
# ->                Campo: Escreva o seu nome no chat
# ->                Botão: Entrar no Chat

# chat:
# Campo: Digite sua mensagem
# Botão: Enviar

# --------------- Fim Estrutura Lógica ------------------

# Framework (Flet) / Instalar o Flet

#Importar a Framework Flet
from cgitb import text
from tkinter import Label
from turtle import onclick
import flet as ft

#Eis o App/Site
def main(pagina):
    
    texto = ft.Text("Project Chatai")
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
         # Adicionar Mensagem no Chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        print("mensagem")
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
           
    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        # Limpar o chat
        campo_mensagem.value = " "
        pagina.update()
            

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    linha = ft.Row([campo_mensagem, botao_enviar])
    
    
        
    def entrar_chat(evento):
        #objetivo:
        # Fechar o Pop Up
        popup.open=False
        # tirar o botao iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o titulo
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # colocar o campo de digitar mensagem
        # (pagina.add(campo_mensagem))
        # criar o botao enviar
        pagina.add(linha)
        pagina.update()
        print("Entrando no Chat")
    
    titulo_popup = ft.Text("Bem vindo ao Chatai")
    nome_usuario = ft.TextField(label="Escreva seu nickname")
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    
    popup = ft.AlertDialog(
        modal=True,
        open=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]   
        )
    
#  Funções da Página:

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
        
  
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)




# Adições à página
    pagina.add(texto)
    pagina.add(botao_iniciar)

#Rodar o site    
ft.app(target=main, view=ft.WEB_BROWSER)

