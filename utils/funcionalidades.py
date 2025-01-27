from tkinter import messagebox
from utils.database import inserir_usuario, buscar_usuario, inserir_postagem, buscar_postagens

def registrar_usuario(nome, senha, confirmacao_senha):
    if senha != confirmacao_senha:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return False
    try:
        inserir_usuario(nome, senha)
        messagebox.showinfo("Sucesso", f"Usuário {nome} registrado com sucesso!")
        return True
    except Exception as e:
        messagebox.showerror("Erro", "Usuário já existe!")
        return False

def autenticar_usuario(nome, senha):
    usuario = buscar_usuario(nome, senha)
    if usuario:
        return usuario
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")
        return None

def postar_item(usuario_id, mensagem, tipo_item, acao, preco=None, imagem=None):
    try:
        inserir_postagem(usuario_id, mensagem, tipo_item, acao, preco, imagem)
        messagebox.showinfo("Sucesso", "Postagem realizada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", "Não foi possível postar o item.")
