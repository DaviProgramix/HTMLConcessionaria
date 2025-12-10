import tkinter as tk
from tkinter import messagebox
import speedtest
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def testar_internet():
    botao.config(state="disabled", text="Testando")
    janela.update()

    try:
        teste = speedtest.Speedtest()

        # Dowload : 
        label_download.config(text="Testando Dowload")
        janela.update()
        velocidade_download = teste.download() / 10**6

        # Upload : 
        label_upload.config(text="Testando Upload")
        janela.update()
        velocidade_upload = teste.upload() / 10**6

        # Ping : 
        ping = teste.results.ping

        # Exibe os Resultados : 
        label_download.config(text=f"Dowload : {velocidade_download: .2f} Mbps ")
        label_upload.config(text=f"Upload : {velocidade_upload: .2f} Mbps ")
        label_ping.config(text=f"Ping : {ping: .2f} ")

    except Exception as e:
        massagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

    botao.config(state="normal", text="Fazer Teste")

janela = customtkinter.CTk()
janela = tk.Tk()
janela.title("Teste de Velocidade")
janela.geometry("300x200")

botao = tk.Button(janela, text="Fazer Teste", command=testar_internet)
botao.pack(padx=10, pady=10)

label_download = tk.Label(janela, text="Download: ")
label_download.pack(padx=10, pady=10)

label_upload = tk.Label(janela, text="Upload: ")
label_upload.pack(padx=10, pady=10)

label_ping = tk.Label(janela, text="Ping: ")
label_ping.pack(padx=10, pady=10)

janela.mainloop()