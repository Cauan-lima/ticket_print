

from flask import Flask, render_template, request, redirect, url_for
import os
import win32api
import win32print

app = Flask(__name__)

# Nome exato da impressora no Windows
IMPRESSORA = "EPSON L455"  # <-- coloque o nome da sua impressora aqui

# Mapear os botões para imagens
IMAGENS = {
    "1": "assets/images/Thorfinn 🍁.jpeg",
    "2": "assets/images/Bridge.jpg",
    "3": "assets/images/Escultura.jpg",
    "4": "assets/images/Grafite.jpg",
    "5": "assets/images/Liberdade.jpg",
    "6": "assets/images/Museu da Lingua Portuguesa.jpg",
}

@app.route("/")
def home():
    return render_template("index.html", mensagem="")

@app.route("/imprimir", methods=["POST", "GET"])
def imprimir():
    if request.method == "POST":
        numero = request.form.get("imagem")
        caminho = IMAGENS.get(numero)

        if not caminho or not os.path.exists(caminho):
            return render_template("index.html", mensagem="❌ Imagem não encontrada!")

        try:
            win32print.SetDefaultPrinter(IMPRESSORA)
            win32api.ShellExecute(0, "print", caminho, None, ".", 0)
            return render_template("index.html", mensagem=f"✅ Imagem {numero} enviada para {IMPRESSORA}.")
        except Exception as e:
            return render_template("index.html", mensagem=f"⚠️ Erro: {str(e)}")
    else:
        # Se abrir com GET, volta para a home
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

    app.run(host="0.0.0.0", port=5000, debug=True)