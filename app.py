import tkinter as tk
from tkinter import messagebox
import requests
import sys
import os

# ================= CONFIG =================
VERSAO_LOCAL = "1.0.0"

URL_VERSAO = "https://raw.githubusercontent.com/centralfunerariamuller-arch/teste/main/version.txt"
URL_APP = "https://raw.githubusercontent.com/centralfunerariamuller-arch/teste/main/app.py"
# ==========================================


def verificar_atualizacao():
    status_label.config(text="🔍 Verificando atualização...")
    janela.update()

    try:
        r = requests.get(URL_VERSAO, timeout=5)

        if r.status_code != 200:
            status_label.config(text="❌ Erro ao acessar GitHub")
            return

        versao_online = r.text.strip()

        if versao_online != VERSAO_LOCAL:
            resposta = messagebox.askyesno(
                "Atualização disponível",
                f"Nova versão encontrada: {versao_online}\nDeseja atualizar agora?"
            )
            if resposta:
                atualizar_app()
            else:
                status_label.config(text="ℹ️ Atualização cancelada")
        else:
            status_label.config(text="✅ App já está atualizado")

    except Exception as e:
        status_label.config(text="❌ Erro de conexão")


def atualizar_app():
    status_label.config(text="⬇️ Baixando atualização...")
    janela.update()

    try:
        r = requests.get(URL_APP, timeout=5)

        if r.status_code != 200:
            status_label.config(text="❌ Erro ao baixar app")
            return

        caminho = os.path.abspath(sys.argv[0])

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(r.text)

        messagebox.showinfo(
            "Atualização concluída",
            "O app foi atualizado com sucesso!\nAbra novamente para usar a nova versão."
        )
        janela.destroy()

    except Exception:
        status_label.config(text="❌ Falha na atualização")


# ================= INTERFACE =================
janela = tk.Tk()
janela.title("Meu App Python 🚀")
janela.geometry("400x250")
janela.resizable(False, False)
janela.configure(bg="#1e1e2f")

titulo = tk.Label(
    janela,
    text="Meu App Python",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#1e1e2f"
)
titulo.pack(pady=15)

versao = tk.Label(
    janela,
    text=f"Versão atual: {VERSAO_LOCAL}",
    font=("Segoe UI", 10),
    fg="#cfcfcf",
    bg="#1e1e2f"
)
versao.pack()

btn_atualizar = tk.Button(
    janela,
    text="🔄 Verificar atualização",
    font=("Segoe UI", 11, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    relief="flat",
    width=22,
    command=verificar_atualizacao
)
btn_atualizar.pack(pady=25)

status_label = tk.Label(
    janela,
    text="Pronto",
    font=("Segoe UI", 10),
    fg="#aaaaaa",
    bg="#1e1e2f"
)
status_label.pack(side="bottom", pady=10)

janela.mainloop()
