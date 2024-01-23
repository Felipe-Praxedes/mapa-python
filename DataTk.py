import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class SelecionarData:

    def obter_data_selecionada(self):
        data_selecionada = self.cal.get_date()
        print("Data selecionada:", data_selecionada)

    def ajustar_tamanho_fonte(self, event=None):
        tamanho_fonte = int(self.root.winfo_width() / 30)  # Ajuste conforme necessário
        self.cal.config(font=("Arial", tamanho_fonte))
    
    def printar(self):
        print("Algumas coisas")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Campo de Data Selecionável")

        self.cal = DateEntry(self.root, width=12, background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.cal.pack(padx=10, pady=10)

        self.root.bind("<Configure>", self.ajustar_tamanho_fonte)

        btn = ttk.Button(self.root, text="Obter Data Selecionada", command=self.obter_data_selecionada)
        btn.pack(pady=10)

        self.printar()

        self.root.mainloop()
        
