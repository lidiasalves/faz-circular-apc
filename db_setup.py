import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('rede_social.db')
    cursor = conn.cursor()
    
    # Tabela para usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    # Tabela para postagens
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS postagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            mensagem TEXT NOT NULL,
            tipo_item TEXT NOT NULL,
            acao TEXT NOT NULL,
            preco REAL,
            imagem TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
