import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def abrir_arquivo():
    global latitudes_longitudes
    # Abre a janela de diálogo para selecionar um arquivo de texto
    # Obtém o número inserido pelo usuário
    numero = entrada_numero.get()
    if not numero:
        messagebox.showerror("Erro", "Insira o número de frota antes de importar o arquivo.")
        return

    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if arquivo:
        # Lê o conteúdo do arquivo
        with open(arquivo, 'r') as file:
            linhas = file.readlines()



        # Filtra as linhas que contêm a string "KIJO120,02" seguida do número
        latitudes_longitudes = []
        for linha in linhas:
            if f"KIJO120,02,{numero}" in linha:
                partes = linha.split(',')
                if len(partes) >= 8:
                    latitude = partes[6]
                    longitude = partes[7]
                    latitudes_longitudes.append(f"{latitude},{longitude}\n")

        if latitudes_longitudes:
            # Exibe as latitudes e longitudes na caixa de texto
            texto_caixa.delete(1.0, tk.END)  # Limpa a caixa de texto existente
            for info in latitudes_longitudes:
                texto_caixa.insert(tk.END, info)

def salvar_arquivo():
    global latitudes_longitudes
    if latitudes_longitudes:
        # Abre uma janela de diálogo para salvar o arquivo
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])

        if arquivo:
            # Salva as latitudes e longitudes em um novo arquivo
            with open(arquivo, 'w') as file:
                file.writelines(latitudes_longitudes)
                messagebox.showinfo(f"Sucesso", "LatLong do HoverBee {numero} foram salvas com sucesso!")

# Cria a janela principal
janela = tk.Tk()
janela.title("HoverBee LATLONG Converter - V1.0.0.0")
janela.geometry("800x600")  # Define o tamanho da janela para 800x600 pixels
janela.resizable(False, False)

# Cria um campo de texto para o usuário inserir o número
entrada_numero_label = tk.Label(janela, text="Número de Frota:")
entrada_numero_label.pack()
entrada_numero = tk.Entry(janela)
entrada_numero.pack()

# Cria um botão para abrir o arquivo
botao_abrir = tk.Button(janela, text="Importar KIJO Log", command=abrir_arquivo)
botao_abrir.pack(pady=10, padx=10)

# Cria um botão para salvar as informações
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_arquivo)
botao_salvar.pack(pady=10, padx=10)

# Cria uma caixa de texto para exibir as latitudes e longitudes
texto_caixa = tk.Text(janela, wrap=tk.WORD, width=80, height=30)  # Tamanho da caixa de texto
texto_caixa.pack()

# Inicia a interface gráfica
janela.mainloop()
