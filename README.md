# Estoque

.Repositório criado para desenvolvimento de sistema de gerenciamento de estoque.<br />

# Como rodar o projeto?

.Clone esse repositório.<br />
.Crie um virtualenv com Python 3<br />
.Ative o virtualenv<br />
.Instale as dependências<br />
.Rode as migrações<br />

.git clone https://github.com/rg3915/estoque.git<br />
.cd estoque<br />
.python3 -m venv .venv<br />
.source .venv/bin/activate<br />
.pip install -r requirements.txt<br />
.python contrib/env_gen.py<br />
.python manage.py migrate<br />

## Links

.[python-decouple](https://github.com/henriquebastos/python-decouple)<br />
.[package-of-the-week-python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)<br />