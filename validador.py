
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("🔐 Verificador de Força de Senha"),
    ui.input_text("senha", "Digite sua senha:", ""),
    ui.output_text("forca")
)

def server(input, output, session):
    @output()
    @render.text
    def forca():
        senha = input.senha()
        if len(senha) < 6:
            return "Fraca: muito curta!"
        elif senha.isalpha() or senha.isdigit():
            return "Média: adicione letras e números!"
        elif any(c in "!@#$%" for c in senha):
            return "Forte: boa senha!"
        else:
            return "Boa: mas pode melhorar com símbolos especiais."

app = App(app_ui, server)
