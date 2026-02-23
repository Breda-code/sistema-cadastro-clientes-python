# 📌 Sistema de Cadastro de Clientes - Python + Tkinter + SQLite

Aplicação desktop desenvolvida em Python utilizando Tkinter para interface gráfica e SQLite como banco de dados.

O projeto implementa um sistema completo de CRUD (Create, Read, Update, Delete) para gerenciamento de clientes.

---

## 🚀 Funcionalidades

✔ Inserir novos clientes  
✔ Listar todos os registros  
✔ Buscar clientes por nome, sobrenome, e-mail ou CPF  
✔ Atualizar dados  
✔ Deletar registros  
✔ Interface gráfica simples e funcional  

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Tkinter (Interface gráfica)
- SQLite3 (Banco de dados)
- Programação orientada a objetos
- Arquitetura separando GUI e Backend

---

## 🧠 Estrutura do Projeto

sistema-cadastro-clientes/
│
├── aplicacao.py # Controle da aplicação e integração GUI + backend
├── backend.py # Regras de negócio e acesso ao banco de dados
├── gui.py # Interface gráfica com Tkinter
├── clientes.db # Banco de dados SQLite
└── README.md

---

## 🗄 Banco de Dados

O sistema utiliza SQLite e cria automaticamente a tabela `clientes` com a seguinte estrutura:

- id (INTEGER PRIMARY KEY)
- nome (TEXT)
- sobrenome (TEXT)
- email (TEXT)
- cpf (TEXT)

---

## ▶ Como Executar o Projeto

1. Clone o repositório
2. Acesse a pasta do projeto
3. Execute o arquivo principal
