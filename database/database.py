import sqlite3
import os

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
def execute_query(query, params=None, fetch=False): # fetch = true quando precisar retornar dados
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
# parametro ? para evitar sql injection

# Usuários: criar, buscar por ID, buscar por username, validar senha

# Criar usuario
def create_user(username, password_hash):
    # usar INSERT e  capturar o ID retornado (lastrowid)
    return
    
# Buscar por id
def get_user_by_id(user_id):
    # usar SELECT com WHERE, fetch = true
    return

# Buscar usuario por username
def get_user_by_username(username):
    # filtrar por username
    return

# Validar senha
def validate_password(user_id, password_hash):
    # buscar user_id, compara o password_hash
    return

# Projetos: criar, listar por usuário, buscar por ID, deletar

# Criar projeto
def create_project(user_id, name):
    # cria um novo projeto vinculado com o usuario
    return

# Listar projetos
def get_projects_by_user(user_id):
    # lista todos projetos do usuario
    return

# Buscar projetos
def get_project_by_id(project_id):
    # Busca um projeto específico
    return

# Deletar projeto
def delete_project(project_id):
    # Deleta um projeto
    return

# Sessões: criar, listar por projeto, buscar por ID, atualizar status

# Criar sessao
def create_session(project_id, title):
    # Criar sessao dentro de um projeto, nao esqueça que sessao começa com status = 'open'
    return

# Listar sessoes
def get_sessions_by_project(project_id):
    # Listar todas as sessoes de um projeto
    return

# Buscar sessao
def get_session_by_id(session_id):
    # Busca sessao especifica
    return

# Atualizar status
def update_session_status(session_id, status):
    # atualiza status open -> resolved
    return

# Entradas: criar, listar por sessão, buscar por ID

# Criar entrada
def create_entry(session_id, entry_type, content):
    # Cria entrada (type: problem, hypothesis, test, solution)
    return

# Listar entradas
def get_entries_by_session(session_id):
    # Lista todas as entradas de uma sessao
    return

# Buscar sessao
def get_entry_by_id(entry_id):
    # Busca entrada específica 
    return