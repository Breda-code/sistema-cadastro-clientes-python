from tkinter import END
from gui import Gui
import backend as core

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)

    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def inserir_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def atualizar_command():
    selected_tuple = app.listClientes.get(app.txtNome.get())

    if not selected_tuple:
        print("Nenhum item selecionado")
        return

    selected = app.listClientes.get(selected_tuple[0])
    registro_id = selected[0]

    core.update(
        registro_id,
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    )

    view_command()

def deletar_command():
        selected_tuple = app.listClientes.curselection()

        if not selected_tuple:
            return # evita erro se nada tiver selecionado

        selected = app.listClientes.get(selected_tuple[0])
        id = selected[0]

        core.delete(id)
        view_command()

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(0, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(0, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(0, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(0, selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListBoxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command = view_command)
    app.btnBuscar.configure(command = search_command)
    app.btnInserir.configure(command = inserir_command)
    app.btnAtualizar.configure(command = atualizar_command)
    app.btnDeletar.configure(command = deletar_command)
    app.btnFechar.configure(command = app.window.destroy)
    app.run()
