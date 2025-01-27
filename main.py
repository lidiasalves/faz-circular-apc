import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, Listbox, filedialog
from PIL import Image, ImageTk

# Conexão com o banco de dados
def conectar_bd():
    return sqlite3.connect('rede_social.db')

# Função para registrar usuário
def registrar_usuario():
    nome = entry_nome.get()
    senha = entry_senha.get()
    confirmacao_senha = entry_confirmacao_senha.get()

    if senha != confirmacao_senha:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", f"Usuário {nome} registrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe!")
    finally:
        limpar_campos()

# Função para limpar campos de entrada
def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_senha.delete(0, 'end')
    entry_confirmacao_senha.delete(0, 'end')

# Configuração da interface gráfica
app = Tk()
app.title("Rede Social")
app.geometry("300x300")

Label(app, text="Nome de Usuário:").pack()
entry_nome = Entry(app)
entry_nome.pack()

Label(app, text="Senha:").pack()
entry_senha = Entry(app, show="*")
entry_senha.pack()

Label(app, text="Confirme a Senha:").pack()
entry_confirmacao_senha = Entry(app, show="*")
entry_confirmacao_senha.pack()

Button(app, text="Registrar", command=registrar_usuario).pack()

app.mainloop()

# Função para login de usuário
def login_usuario():
    nome = entry_login_nome.get()
    senha = entry_login_senha.get()

    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
        abrir_tela_usuario(nome)
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")

# Função para abrir a tela do usuário
def abrir_tela_usuario(nome):
    # Fecha a janela de login
    tela_login.destroy()

    # Cria a nova janela
    tela_usuario = Tk()
    tela_usuario.title(f"Bem-vindo, {nome}")
    tela_usuario.geometry("400x400")

    Label(tela_usuario, text=f"Olá, {nome}!", font=("Arial", 14)).pack(pady=10)

    # Botão para postar item
    Button(tela_usuario, text="Postar Item", command=lambda: postar_item(nome)).pack(pady=5)

    # Botão para ver feed
    Button(tela_usuario, text="Ver Feed", command=lambda: ver_feed(nome)).pack(pady=5)

    # Botão para logout
    Button(tela_usuario, text="Logout", command=tela_usuario.destroy).pack(pady=5)

    tela_usuario.mainloop()

def postar_item(nome):
    def salvar_postagem():
        mensagem = entry_mensagem.get()
        tipo_item = entry_tipo_item.get()
        acao = entry_acao.get()
        preco = entry_preco.get()
        imagem = entry_imagem.get()

        conn = conectar_bd()
        cursor = conn.cursor()

        # Recuperar ID do usuário
        cursor.execute("SELECT id FROM usuarios WHERE nome = ?", (nome,))
        usuario_id = cursor.fetchone()[0]

        # Inserir a postagem no banco de dados
        cursor.execute(
            "INSERT INTO postagens (usuario_id, mensagem, tipo_item, acao, preco, imagem) VALUES (?, ?, ?, ?, ?, ?)",
            (usuario_id, mensagem, tipo_item, acao, preco if preco else None, imagem if imagem else None),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Postagem realizada com sucesso!")
        tela_postagem.destroy()

        def selecionar_imagem(): 
            imagem_caminho = filedialog.askopenfilename() 
            entry_imagem_caminho.delete(0, 'end') 
            entry_imagem_caminho.insert(0, imagem_caminho) 
            
            # Exibir a imagem selecionada 
            imagem = Image.open(imagem_caminho) 
            imagem = imagem.resize((100, 100), Image.LANCZOS)
            imagem_tk = ImageTk.PhotoImage(imagem) 
            label_imagem.config(image=imagem_tk) 
            label_imagem.image = imagem_tk
 

    # Janela de postagem
    tela_postagem = Tk()
    tela_postagem.title("Postar Item")
    tela_postagem.geometry("300x400")

    Label(tela_postagem, text="Mensagem:").pack()
    entry_mensagem = Entry(tela_postagem)
    entry_mensagem.pack()

    Label(tela_postagem, text="Tipo do Item:").pack()
    entry_tipo_item = Entry(tela_postagem)
    entry_tipo_item.pack()

    Label(tela_postagem, text="Ação (Doar/Vender):").pack()
    entry_acao = Entry(tela_postagem)
    entry_acao.pack()

    Label(tela_postagem, text="Preço (se aplicável):").pack()
    entry_preco = Entry(tela_postagem)
    entry_preco.pack()

    Label(tela_postagem, text="Imagem (Caminho):").pack()
    entry_imagem = Entry(tela_postagem)
    entry_imagem.pack()

    Button(tela_postagem, text="Salvar", command=salvar_postagem).pack(pady=10)
    tela_postagem.mainloop()

def ver_feed(nome):
    # Janela para o feed
    tela_feed = Tk()
    tela_feed.title("Feed")
    tela_feed.geometry("400x400")

    Label(tela_feed, text="Postagens:", font=("Arial", 14)).pack(pady=10)

    # Recuperar postagens do banco
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.nome, p.mensagem, p.tipo_item, p.acao, p.preco, p.imagem 
        FROM postagens p
        JOIN usuarios u ON p.usuario_id = u.id
    """)
    postagens = cursor.fetchall()
    conn.close()

    for postagem in postagens:
        usuario, mensagem, tipo_item, acao, preco, imagem = postagem
        texto_post = f"{usuario}: {mensagem} ({tipo_item} - {acao})"
        if preco:
            texto_post += f" - Preço: R${preco}"
        if imagem:
            texto_post += f" - Imagem: {imagem}"
        Label(tela_feed, text=texto_post, wraplength=350, justify="left").pack(anchor="w", padx=10)

        # Exibir a imagem se houver 
        if imagem_caminho: 
            imagem = Image.open(imagem_caminho) 
            imagem = imagem.resize((100, 100), Image.LANCZOS) 
            imagem_tk = ImageTk.PhotoImage(imagem) 
            Label(tela_feed, image=imagem_tk).pack(anchor="w", padx=10) 
            # Necessário para evitar que a imagem seja coletada pelo garbage collector 
            label_imagem = Label(tela_feed, image=imagem_tk) 
            label_imagem.image = imagem_tk 
            label_imagem.pack(anchor="w", padx=10)

    tela_feed.mainloop()

# Tela principal
tela_login = Tk()
tela_login.title("Login")
tela_login.geometry("300x250")

Label(tela_login, text="Nome de Usuário:").pack()
entry_login_nome = Entry(tela_login)
entry_login_nome.pack()

Label(tela_login, text="Senha:").pack()
entry_login_senha = Entry(tela_login, show="*")
entry_login_senha.pack()

Button(tela_login, text="Login", command=login_usuario).pack(pady=10)

tela_login.mainloop()


