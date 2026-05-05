# CS50 Final Project

Database + Models → Setup SQLite, criar tabelas
Auth → Registration/Login/Logout (sem isso, nada funciona)
Projects → Create/View/List (estrutura base)
Sessions + Notes → Create sessions com notas estruturadas
Search → Buscar sessions por keywords
Refinamentos → Edição, deleção, UI

Database:
- [ ] schema.sql com CREATE TABLE para users, projects, sessions, entries
- [ ] database.py com funções de conexão

Auth:
- [ ] Hashing de senhas (werkzeug.security)
- [ ] Rotas: /register, /login, /logout
- [ ] Decorator @login_required

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
