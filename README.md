# Sistema Clínico utilizando Rest

<img src="pacote_readme/" alt="exemplo imagem">

>Prototipo para marcar consultas e adicionar médicos e seus horarios e agendas, na área de adm foi usado uma **api** para gerenciar os médicos.

* [Demostração em Vídeo]()

🏫 Atividade acâdemica

## Tecnologias Utilizadas

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">

## 🚀 Processo de Instalação

Para instalar **Clínica**, siga estas etapas:

Linux:
```
git clone https://github.com/Wenderson-Oscar/Clinica.git
virtualenv env
. env/bin/activate
pip install -r requirementes.txt
```

Windows:
```
git clone https://github.com/Wenderson-Oscar/Clinica.git
python -m venv env
env\Scripts\activate
pip install -r requirementes.txt
```

## ☕ Como Utlizar a Aplicação

Para usar **Clínica**, siga estas etapas:

```
python manage.py migrate clientes
python manage.py migrate medico
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
