# importar modulo sqlite3
# os para gerenciar caminhos de arquivo

# Configurar caminho do banco de dados
# definir constante com o caminho do arquivo database.db
# caminho relativo para portabilidade

# Funçao de inicialização 
# conectar ao banco
# ler o arquivo schema.sql
# executar script para criar as tabelas
# fechar conexao

# Funçao de conexao reutilizavel
# Retorna uma conexão ao banco 
# Configura row_factory para retornar resultados como dicionários

# Funções auxiliares para operações comuns
# SELECT/INSERT/UPDATE/DELETE
# Pense em como capturar o lastrowid para INSERTs
# Use ? como placeholder nas queries para evitar SQL injection!