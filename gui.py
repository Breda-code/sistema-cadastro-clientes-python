from tkinter import *

class Gui:
    def __init__(self):

        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        # Janela
        self.window = Tk()
        self.window.title("PYSQL versão 1.0")

        # Variáveis
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels
        Label(self.window, text="Nome").grid(row=0, column=0)
        Label(self.window, text="Sobrenome").grid(row=1, column=0)
        Label(self.window, text="E-mail").grid(row=2, column=0)
        Label(self.window, text="CPF").grid(row=3, column=0)

        # Entrys
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        self.entNome.grid(row=0, column=1)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        # Listbox + Scroll
        self.listClientes = Listbox(self.window, width=60)
        self.listClientes.grid(row=0, column=2, rowspan=10)

        self.scrollClientes = Scrollbar(self.window)
        self.scrollClientes.grid(row=0, column=3, rowspan=10, sticky='NS')

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Botões
        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnAtualizar = Button(self.window, text="Atualizar")
        self.btnDeletar = Button(self.window, text="Deletar")
        self.btnFechar = Button(self.window, text="Fechar", command=self.window.destroy)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnAtualizar.grid(row=7, column=0, columnspan=2)
        self.btnDeletar.grid(row=8, column=0, columnspan=2)
        self.btnFechar.grid(row=9, column=0, columnspan=2)

        # Aparência
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=self.x_pad, pady=self.y_pad)
            elif widget_class in ("Listbox", "Scrollbar"):
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky="N")

    def run(self):
        self.window.mainloop()