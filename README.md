<h1>Projeto FINAN.CE</h1>
<p>Um projeto criado para controle e gerenciamento financeiro, <br/> cujo objetivo é ajudar você a ter uma melhor saúde financeira</p>

<h2>Como Instalar</h2>
<ul>
    <h4>Instalação</h4>
    <li>Em uma nova pasta execute "git clone https://github.com/zefelipe19/finan.ce.git"</li>
    <h4>Ambiente virtual</h4>
    <li>inicie um ambiente virtual "python3 -m venv venv"</li>
    <li>execute "source venv/bin/activate"</li>
    <li>execute "pip install -r requirements.txt"</li>
    <li>execute "python3 manage.py migrate" para criação do banco de dados sqlite3</li>
    <li>execute "python3 manage.py createsuperuser" e siga as instruções para criação do superusuario</li>
    <li>execute "python3 manage.py runserver" para a execução do servidor no "http://localhost:8000"</li>
</ul>
