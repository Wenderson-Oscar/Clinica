# Sistema Clínico utilizando Rest

🏫 Atividade acâdemica

Descrição: prototipo para marcar consultas e adicionar médicos e seus horarios e agendas; na área de adm foi usado uma **api** para melhor gerenciar os médicos.
<hr>

Menu
=================
<!--ts-->
   * [Tecnologias Utilizadas](#tecnologias-utilizadas)
   * [Como Instalar](#como-instalar)
<!--te-->

## Tecnologias Utilizadas

🧰 Visual Code

🔨 Python

📚 Django

📖 Rest_Framework

## Como Instalar

Iremos Clonar o repositorio

```
git clone https://github.com/Wenderson-Oscar/Clinica.git
```

agora iremos baixar o ambiente virtual

```
pip install virtualenv
```
caso ja tenha instalado iremos criar o ambiente virtual

Windows:

```
python -m venv env
```
Linux:

```
virtualenv env
```
Ativando o ambiente virtual

Windows:

```
env\Scripts\activate
```

Linux:

```
. env/bin/activate
```
Agora iremos baixar as dependencias 

```
pip install -r requirements.txt
```

Iremos baixar o banco

```
python manage.py migrate
```
Agora iremos criar o super usuarios

```
python manage.py createsuperuser
```
depois de preencher as informações poderemos iniciar 

```
python manage.py runserver
```
