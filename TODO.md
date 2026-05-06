# CS50 Final Project

Database + Models → Setup SQLite, criar tabelas
Auth → Registration/Login/Logout (sem isso, nada funciona)
Projects → Create/View/List (estrutura base)
Sessions + Notes → Create sessions com notas estruturadas
Search → Buscar sessions por keywords
Refinamentos → Edição, deleção, UI

Database:
- [x] schema.sql com CREATE TABLE para users, projects, sessions, entries
- [x] database.py com funções de conexão
- [x] operaçoes para 4 entidades principais 

User Model (models/user.py):
- [ ] Classe User com métodos
- [ ] register(username, password)
- [ ] verify_password(password)
- [ ] get_by_username(username)

Auth:
- [ ] Hashing de senhas (werkzeug.security)
- [ ] @login_required decorator (utils/decorators.py)
- [ ] /register: validar, hash, salvar em DB
- [ ] /login: buscar user, validar senha, criar sessão
- [x] /logout

Projects:
- [ ] POST /projects (criar)
- [ ] GET /projects (listar)
- [ ] GET /projects/<id> (acessar)

Sessions:
- [ ] POST /projects/<id>/sessions (criar)
- [ ] GET /projects/<id>/sessions (listar)
- [ ] GET /sessions/<id> (visualizar com notes)
- [ ] PUT /sessions/<id> (salvar notes)

Search:
- [ ] GET /search?q=keyword

Templates:
- [ ] login.html: adicionar campo password
- [ ] register.html: adicionar campo password
- [ ] Adicionar mensagens de erro

Config (config.py):
- [ ] SECRET_KEY
- [ ] DATABASE_PATH

