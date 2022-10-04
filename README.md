# TaskBoard Web Application


## Estruturação do Projeto
---


<details>
<summary>Passo a passo</summary>

```bash
git clone
```

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
django-admin startproject config .
```

```bash
django-admin startapp taskboard
```

```bash
touch taskboard/urls.py
```

```bash
touch taskboard/serializer.py
```

```bash
touch taskboard/forms.py
```

```bash
mkdir taskboard/templates
```

```bash
mkdir taskboard/templates/modals
```

```bash
touch taskboard/templates/base.html
```

```bash
touch taskboard/templates/board.html
```

```bash
touch taskboard/templates/index.html
```

```bash
touch taskboard/templates/modals/new_task.html
```

```bash
touch taskboard/templates/modals/new_board.html
```

```bash
mkdir taskboard/static
```

```bash
mkdir taskboard/static/assets
```

```bash
mkdir taskboard/static/css
```

```bash
mkdir taskboard/static/js
```

```bash
touch taskboard/static/style.css
```

![Database diagram](/db-diagram.png "Database diagram")

Planejamento de rotas:
```bash
'/' -> tela com diversos boards e botão para novos boards
'/new-board' -> criação de novo board
'/<int:board_id>' -> tela do board com diversas tasks
'/<int:board_id>/new-task' -> criação de novas tasks
'/api/<int:board_id>' -> endpoint da api que retorna as tasks do board
'/api/<int:board_id>/<str:status>' -> endpoint da api que retorna as tasks do board com status específico
```

Planejamento de templates:
```bash
'base.html' -> base dos templates que será exportada para os demais templates 
'index.html' -> tela com um botão para novos boards + listagem dos boards criados 
'board.html' -> tela do board + botão de nova task + listagem das tasks
'new_task.html' -> modal para criação de tasks
'new_board.html' -> modal para criação de boards 
'edit_status.html' -> modal para edição de status
```
</details>

<br>
<br>



## Execução da aplicação
---

<details>
<summary>Passo a passo</summary>

1. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instale os requerimentos para a aplicação

```bash
pip install -r requirements.txt
```

4. Crie a migrações necessárias

```bash
python3 manage.py makemigrations
```

5. Realize as migrações

```bash
python3 manage.py migrate
```

6. Rode a aplicação

```bash
python3 manage.py runserver
```

</details>