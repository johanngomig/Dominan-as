# **Funcionalidades Implementadas no Sistema**

## **1. Módulo de Contas a Pagar**
### **Descrição:**
O módulo de **Contas a Pagar** permite ao usuário registrar todas as suas despesas futuras, como contas de água, luz, internet, aluguel e outros gastos recorrentes ou eventuais.

### **Funcionalidades Implementadas:**
- **Registro de Contas a Pagar**: 
  - Permite ao usuário adicionar uma nova conta a pagar, com descrição, valor, data de vencimento, categoria e status (paga ou pendente).
  - O status de pagamento é controlado por um campo **checkbox** que, quando marcado, indica que a conta já foi paga.
  
- **Visualização de Contas**:
  - Exibe uma lista de todas as contas a pagar, com detalhes como descrição, valor, data de vencimento, categoria e status (paga ou pendente).
  
- **Edição de Contas a Pagar**:
  - O usuário pode editar uma conta existente, atualizando qualquer informação como a descrição, valor, data de vencimento, categoria e status.
  
- **Botão de Edição**:
  - Na lista de contas, ao lado de cada conta, há um botão para editar a conta. Isso facilita o gerenciamento das contas a pagar.

- **Botão de Exclusão**:
  - Na lista de contas, ao lado de cada conta, há um botão para excluir a conta.

### **Funcionalidades Não Implementadas:**
- **Implementar notificações ou lembretes automáticos para contas próximas do vencimento**
  - Deixei na lista de implementação fora do meu conhecimento para implementar caso tivesse tempo hábil.

---

## **2. Módulo de Contas a Receber**
### **Descrição:**
O módulo de **Contas a Receber** permite ao usuário registrar todas as suas receitas, como salários, rendimentos e outras fontes de receita.

### **Funcionalidades Implementadas:**
- **Registro de Contas a Receber**:
  - O usuário pode adicionar uma nova conta a receber, incluindo uma descrição, valor, data de recebimento, categoria e status.

- **Visualização de Contas a Receber**:
  - Exibe todas as contas a receber em uma lista, mostrando os detalhes como descrição, valor, data de recebimento, categoria e status (recebido ou pendente).

- **Edição e Exclusão de Contas a Receber**:
  - Semelhante ao Módulo de Contas a Pagar, facilita o gerenciamento das contas a pagar.

### **Funcionalidades Não Implementadas:**
- **Implementar suporte para receitas recorrentes**
  - Da mesma forma deixei para implementar caso tivesse tempo hábil.

---

## **3. Módulo de Compras com Cartão de Crédito**
### **Descrição:**
O módulo de **Compras com Cartão de Crédito** permite ao usuário registrar todas as compras realizadas com cartão de crédito, gerenciar as parcelas das compras e acompanhar o limite do cartão.

### **Funcionalidades Implementadas:**
- **Registro de Compras**:
  - O usuário pode adicionar uma compra, incluindo a descrição, valor, data da compra, categoria, número de parcelas e o cartão utilizado.
  
- **Gerenciamento de Parcelas**:
  - O sistema divide automaticamente o valor da compra pelo número de parcelas e cria uma entrada para cada parcela, com sua data de vencimento.
  
- **Limite de Cartão**:
  - O sistema verifica o limite do cartão antes de registrar uma nova compra. Se o valor da compra ultrapassar o limite disponível, uma mensagem de erro é exibida e a compra não é registrada.
  
- **Visualização de Compras**:
  - Exibe todas as compras realizadas com cartão de crédito em uma tabela, mostrando detalhes como descrição, valor, categoria, número de parcelas e o limite disponível do cartão.
  
- **Visualização de Parcelas**:
  - O usuário pode visualizar todas as parcelas associadas a uma compra específica, com detalhes como número da parcela, valor e status (paga, vencida ou próxima de vencer).

- **Exclusão de Compra com Cartão**:
  - Permite a exclusão da Compra com Cartão juntamente com as parcelas para que seja incluída novamente mantendo a integridade das parcelas.

## **4. Módulo de Relatórios Financeiros**
### **Descrição:**
O módulo de **Relatórios Financeiros** permite ao usuário visualizar suas despesas e receitas, com a possibilidade de filtrar por período e tipo de relatório.

### **Funcionalidades Implementadas:**
- **Relatório de Despesas por Categoria**:
  - O sistema gera um relatório com todas as despesas do usuário, agrupadas por categoria e dentro de um período especificado.
  
- **Relatório de Saldo entre Contas a Pagar e Receber**:
  - Gera um relatório com o saldo total entre as contas a pagar, a receber e a compras de cartão, ajudando o usuário a visualizar o quanto ele deve, o quanto espera receber e o quanto gastou no cartão em um determinado período.

- **Gráficos**:
  - O sistema gera gráficos interativos usando a biblioteca **Chart.js**, permitindo que o usuário visualize suas finanças de forma mais clara.

### **Funcionalidades Não Implementadas:**
- **Exportação para PDF ou Excel ainda não foi implementada**
  - Deixei na lista de implementação fora do meu conhecimento para implementar caso tivesse tempo hábil.

---

## **5. Controle de Acesso de Usuário**
### **Descrição:**
O sistema utiliza um processo de autenticação por login e senha para garantir que as informações financeiras de cada usuário sejam privadas e seguras.

### **Funcionalidades Implementadas:**
- **Registro de Usuário**:
  - O sistema permite que novos usuários se registrem, criando uma conta com nome, e-mail e senha.
  
- **Login e Autenticação**:
  - Para acessar o sistema, os usuários devem fazer login com suas credenciais. A senha é armazenada de forma segura, utilizando algoritmos de hashing.
  
- **Sessões**:
  - O sistema utiliza sessões para manter os usuários autenticados durante a navegação, que expira após 60 minutos. As rotas críticas, como o gerenciamento de contas e recebimentos, só são acessíveis a usuários autenticados.
  
- **Logout**:
  - O usuário pode fazer logout a qualquer momento, encerrando sua sessão e garantindo a segurança de suas informações.

---

## **Funcionalidades Extras Implementadas**

### **1. Feedback Visual com Flash Messages**
- O sistema utiliza **flash messages** para fornecer feedback imediato ao usuário sobre ações realizadas, como adicionar, editar ou excluir uma conta.
- As mensagens aparecem por 2 segundos e são automaticamente ocultadas usando **JavaScript**.

### **2. Edição de Contas a Pagar e a Receber**
- Para facilitar o gerenciamento financeiro, os módulos permitem a edição dos dados inseridos. O usuário pode ajustar detalhes de uma conta ou recebimento, como o valor, data de vencimento e status.
  
### **3. Design Responsivo**
- O uso de **Bootstrap 5.3** garante que o sistema seja responsivo, ou seja, que funcione corretamente em diferentes tamanhos de tela, desde dispositivos móveis até desktops.

### **4. Módulo de Cadastro de Cartão de Crédito**
### **Descrição:**
O módulo de **Cadastro de Cartão de Crédito** permite ao usuário cadastrar um ou mais cartões de créditos e acompanhar sua quantidade, data de vencimento e limite restante.

### **Funcionalidades Implementadas:**
- **Cadastro de Cartão**:
  - O usuário pode adicionar um cartão, incluindo o nome, limite do cartão de crédito e a data de vencimento.
  
- **Edição e Exclusão de Cartão**:
  - Permite edição e a exclusão do Cartão, exclusão somente caso não haja nenhuma compra associada a ele.

---

# **Estrutura Geral:**
## **Front-end**

### **Tecnologias Utilizadas:**
1. **HTML5**: A estrutura básica das páginas web foi desenvolvida com HTML5.
2. **CSS3**: Utilizado para estilização das páginas.
3. **Bootstrap 5.3**: Um framework CSS que facilita a criação de layouts responsivos e componentes visuais (botões, tabelas, formulários, etc.).
4. **JavaScript**: Usado para funcionalidades básicas do lado do cliente, como a exibição e ocultação automática de mensagens de alerta.
5. **Jinja**: Um mecanismo de template usado por padrão no FLask.

---

## **Back-end**

### **Tecnologias Utilizadas:**
1. **Flask**: Framework web minimalista em Python que foi utilizado para gerenciar as rotas, sessões de usuários e renderização de templates HTML.
2. **SQLAlchemy**: ORM (Object-Relational Mapping) que facilita a interação entre a aplicação e o banco de dados, permitindo a manipulação de dados como objetos Python.
3. **Werkzeug Security**: Utilizado para a geração e verificação de hashes de senhas.

---

## **Database**

### **Tecnologia Utilizada:**
- **PostgreSQL**: Banco de dados relacional que armazena todas as informações financeiras e de usuários.

---

## **Migrations**

### **Tecnologia Utilizada:**
- **Alembic**: Ferramenta para o controle de versão do banco de dados, usada para criar e aplicar migrações.

---

## **Requerimentos Necessários**

### **Instalação das Dependências do Projeto:**

1. **Python 3.x**: Linguagem principal usada no projeto.

2. **Bibliotecas Python:**
   - Flask
   - Flask-SQLAlchemy
   - Flask-Migrate (para integrar Alembic e Flask)
   - PostgreSQL (como banco de dados)
   - Alembic (para migrations)
   - Python-Decouple (para gerenciamento de variáveis de ambiente)

---

## **Execução do Projeto**

1. **Configurar o Banco de Dados:**
- Crie um banco de dados no PostgreSQL, por exemplo:

    ```sql
    CREATE DATABASE controle_financeiro;
    ```

2. **Instalar as Dependências do Python:**
- Execuar o comando
    ```bash
    cd .\back-end\
    pip install -r requirements.txt
    ```

3. **Configurar as Variáveis de Ambiente:**
- No arquivo `/back-end/config/config.py`, atualize suas variáveis de configuração, como:

    ```bash
    DATABASE_URL = os.getenv("DATABASE_URL",'postgresql://usuario:senha@localhost:porta/controle_financeiro')
    ```
- E no arquivo `/back-end/alembic.ini`,

    ```bash
    sqlalchemy.url = postgresql://usuario:senha@localhost:porta/controle_financeiro
    ```

4. **Rodar as Migrações:**
- Garantir a execução do comando à partir do diretório /back-end

    ```bash
    cd .\back-end\
    alembic upgrade head
    ```

5. **Popular a Base (Opcional):**
- Rodar o Script SQL ```/back-end/tests/inclusao_massa_dados.sql``` para inseção de massa de testes. Obs, a senha para todos os usuários é: senha123

6. **Iniciar o Servidor:**
    ```bash
    cd .\back-end\
    python app.py
    ```

7. **Executar o Caminho Ideal:**
- Remover todos os dados já incluídos na base ```controle_financeiro```
  ```sql
    TRUNCATE usuario CASCADE RESTART IDENTITY
  ```
- Seguir os passos do arquivo ```/back-end/tests/README.md``` para entender o fluxo do sistema.

Agora você pode acessar a aplicação web no navegador usando o endereço **http://127.0.0.1:5000**.
