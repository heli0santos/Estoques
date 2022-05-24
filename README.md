# Estoque
.Repositório criado para desenvolvimento de sistema de gerenciamento de estoque.

# Como rodar o projeto?

.Clone esse repositório.
.Crie um virtualenv com Python 3
.Ative o virtualenv
.Instale as dependências
.Rode as migrações

.git clone https://github.com/rg3915/estoque.git
.cd estoque
.python3 -m venv .venv
.source .venv/bin/activate
.pip install -r requirements.txt
.python contrib/env_gen.py
.python manage.py migrate

## Links

.[python-decouple](https://github.com/henriquebastos/python-decouple)
.[package-of-the-week-python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)