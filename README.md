(https://github.com/JefersonnL/SaudadesDela/blob/main/static/VV.png?raw=true)

# Meu Projeto de Treino

## Descrição

Este é um aplicativo web para gerenciamento de treinos e registro de atividades físicas. O projeto permite que os usuários se registrem, façam login e visualizem diferentes rotinas de treino. Foi desenvolvido usando Flask para o backend e inclui uma interface de usuário responsiva.

## Funcionalidades

- **Cadastro de Usuários**: Permite que novos usuários se registrem.
- **Login**: Permite que usuários existentes façam login.
- **Visualização de Treinos**: Exibe diferentes rotinas de treino, incluindo exercícios para várias partes do corpo.
- **Gerenciamento de Treinos**: Exibe e organiza listas de exercícios para diferentes grupos musculares.

## Tecnologias Usadas

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS
- **Banco de Dados**: SQLite
- **Gerenciamento de Pacotes**: pip

## Instalação

Para configurar e executar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório**:
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
2. **Configurar o ambiente virtual**
Criar um ambiente virtual Python para isolar as dependências do projeto. O usuário pode fazer isso com os seguintes comandos:
   python -m venv venv
   venv\Scripts\activate
3. **Instalar as dependências**
As dependências estão listadas no arquivo requirements.txt. O próximo passo é instalar essas dependências usando pip:
   pip install -r requirements.txt
4. **Configurar o banco de dados**
O projeto usa SQLite, que é leve e não exige instalação de um servidor de banco de dados. Para criar o banco de dados, pode ser necessário rodar os scripts de configuração:
   python create_db.py
5. **Executar o programa**
Após a instalação e configuração, o usuário pode iniciar o programa usando o comando:
   python app.py
**O servidor Flask vai rodar localmente, e o usuário poderá acessar o aplicativo através do navegador no endereço http://127.0.0.1:5000.**
