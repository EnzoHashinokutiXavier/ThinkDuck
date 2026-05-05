import sqlite3
import os
import logging


# definir constante com o caminho relativo do arquivo database.db
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

# Funçao de inicialização 
def init_db():
    #Inicializa o banco e cria tabelas a partir do schema.sql
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql') # pega a pasta desse arquivo e procura 'schema.sql'
    if not os.path.exists(schema_path): # Verifica se schema.sql existe
        raise FileNotFoundError(f"schema.sql não encontrado em {schema_path}")
    with sqlite3.connect(DB_PATH) as conn: # conecta ao banco de dados como 'conn'
        with open(schema_path, 'r') as file: # abre schema para leitura como 'file'
            conn.executescript(file.read()) # executa script lido

# Funçao de conexao reutilizavel
# conectar ao banco
def get_db():
    conn = sqlite3.connect(DB_PATH)
    # Configura row_factory para retornar resultados como dicionários
    conn.row_factory = sqlite3.Row 
    # Retorna uma conexão ao banco 
    return conn

# Funções auxiliares para operações comuns
def execute_query(query, params=None, fetch=False):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

# operaçoes para 4 entidades principais : 
# Usuários: criar, buscar por ID, buscar por username, validar senha
# Projetos: criar, listar por usuário, buscar por ID, deletar
# Sessões: criar, listar por projeto, buscar por ID, atualizar status
# Entradas: criar, listar por sessão, buscar por ID