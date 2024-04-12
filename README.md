# Almoxarifado - DPPE

## Descrição do projeto

Este projeto vem com o objetivo de substituir o sistema Santo Ivo, que atualmente é utilizado na gestão de almoxarifado e patrimônio da Defensoria Pública do Estado de Pernambuco.

## Dependências

[Poetry 1.5.0](https://python-poetry.org/)

[Python 3.12.0](https://www.python.org/)

[Django 5.0.3](https://www.djangoproject.com/)

## Instalação

1. Instalar o pipx:

`pipx` é utilizado para instalar aplicações do tipo CLI do python globalmente, enquanto as mantém isoladas em ambientes virtuais.

```cmd
pip install pipx
```

2. Instalando o poetry:

`Poetry` é uma ferramenta para gerenciamento de dependências e empacotamento em Python. Ela permite que você declare as bibliotecas nas quais seu projeto depende e irá gerenciá-las (instalar/atualizar) para você. Poetry oferece um arquivo de bloqueio para garantir que não ocorra instalações repetíveis e pode construir seu projeto para distribuição.

A versão utilizada no projeto é a `1.5.0`. Esta informação é importante pois pode haver alguma mudança entre uma versão e outra que interfira no funcionamento do projeto.

```cmd
pipx install poetry==1.5.0
```

3. Instalando dependências

```cmd
poetry init
```

O comando acima instala todas as dependências contidas no arquivo `pyproject.toml`

## Comandos úteis

```python
# Monta o projeto.
poetry init

# Acessa o ambiente virtual (similar ao venv do python virtual enviroment)
poetry shell

# Adiciona pacotes python ao projeto.
poetry add pacote

# Remove pacotes python do projeto.
poetry remove pacote

# Executa um comando dentro do ambiente do poetry
poetry run comando (Ex: 'poetry run python manage.py runserver')
```

### Comandos configurados via taskipy

[Taskipi](https://github.com/taskipy/taskipy) é um biblioteca para python que auxilia na execução de comandos repetíveis, tornando-os mais simples e de fácil execução. Ex:

O comando `python manage.py runserver` pode ser configurado no arquivo `pyproject.toml` dentro da sessão `[tool.taskipy.tasks]` de uma forma mais simples.

```python
[tool.taskipy.tasks]
start = "python manage.py runserver"
```

Dessa forma, ao invés de executar o comando inteiro por extenso é possível executar apenas `task start` se você estiver dentro do shell do poetry ou `poetry run task start` se você estiver fora do shell.

Aqui estão alguns comandos já configurados no taskipy

```python
# runserver
poetry run task start "ou" task start

# migrate
poetry run task migrate "ou" task migrate

# makemigrations
poetry run task make "ou" task make

# test
poetry run task test "ou" task test
```
