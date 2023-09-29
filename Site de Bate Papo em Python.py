# pip install flet
# flet -> FrontEnd/BackEnd

# PROJETO HASHZAP

# botao de iniciar o chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

# Passo a passo para construir um site com flet

# 1° - Importar o Flet

import flet as ft

# 2° - Criar uma função no python que gerencia a página

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()
    
    nome_usuario = ft.TextField(label="Escreva seu Nome")
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
            pagina.update()
        else:
           usuario_mensagem = mensagem["usuario"]
           chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat",
                                        size=12, italic=True, color=ft.colors.DEEP_ORANGE_ACCENT))

    # PUBSUB
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        # limpar o campo de mensagens
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma Mensagem", on_submit=enviar_mensagem)

    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        #adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        pagina.update()
        # remover o botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo de mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
            
            ))
        
        # criar o botão de enviar mensagem do usuario
        pagina.add(botao_enviar_mensagem)
    
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title=ft.Text("Bem Vindos ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )
    
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

# 3° - Executar o Site

ft.app(target=main, view=ft.WEB_BROWSER, port=2023)


# Dicionários em Python:

#produto = {
        #"produto": "iphone",
        #"preço": 6500,
        #"quantidade": 150
# }

# produto["quantidade"]

#Intranet:

# ipconfig
#Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.3.28

# Internet:

#deploy