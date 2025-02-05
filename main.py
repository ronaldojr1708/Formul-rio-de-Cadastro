import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.padding = 25
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nome = ft.TextField(label="Nome", width=400)
    email = ft.TextField(label="Email", width=400)
    mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=3, max_lines=5, width=400)

    sucesso_msg = ft.Text("", color="green")
    nome_exibido = ft.Text("")
    email_exibido = ft.Text("")
    mensagem_exibida = ft.Text("")

    def enviar_form(e):
        if nome.value and email.value and mensagem.value:
            sucesso_msg.value = "Formulário enviado com sucesso!"
            sucesso_msg.color = "green"
            nome_exibido.value = f"📌 Nome: {nome.value}"
            email_exibido.value = f"📧 Email: {email.value}"
            mensagem_exibida.value = f"📝 Mensagem:\n{mensagem.value}"
        else:
            sucesso_msg.value = "Por favor, preencha todos os campos."
            sucesso_msg.color = "red"

        page.update()

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_form)

    page.add(
        ft.Column(
            controls=[
                nome, 
                email, 
                mensagem, 
                botao_enviar, 
                sucesso_msg,
                ft.Divider(),
                nome_exibido,
                email_exibido,
                mensagem_exibida
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
