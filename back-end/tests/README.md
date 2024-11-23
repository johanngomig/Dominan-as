### Guia de Caminho Ideal

#### 1. **Registro no Sistema**
   - **URL**: `http://127.0.0.1:5000/`
   - **Passos**:
     1. Acesse a URL `http://127.0.0.1:5000/`.
     2. Clique no link Registre-se.
     2. Insira seu nome, e-mail e senha cadastrados.
     3. Após o Registro bem-sucedido, você será redirecionado para a tela de Login.

#### 2. **Login no Sistema**
   - **URL**: `/login`
   - **Passos**:
     1. Acesse a URL `/login`.
     2. Insira seu e-mail e senha cadastrados.
     3. Após o login bem-sucedido, você será redirecionado para o dashboard.

#### 3. **Dashboard**
   - **URL**: `/dashboard`
   - **Passos**:
     1. Se você não for redirecionado para a URL `/dashboard` clique no menu da barra de navegação `Gestão Doméstica`.
     2. No dashboard, você verá as contas pendentes, pagas e o total.
     3. Use esta página para ter uma visão geral das suas finanças.

#### 4. **Gerenciar Contas a Pagar**
   - **URL**: `/contas_a_pagar`
   - **Passos**:
     1. Acesse a URL `/contas_a_pagar` ou clique no menu da barra de navegação `Contas a Pagar`.
     2. Visualize a lista de todas as suas contas a pagar.
     3. Para adicionar uma nova conta, clique em "Adicionar Nova Conta".
     4. Preencha o formulário com as informações da conta (descrição, valor, data de vencimento, categoria, status(Pago ou Não)) e salve.
     5. Para editar uma conta existente, clique no botão "Editar" ao lado da conta desejada.
     6. Para excluir uma conta, clique no botão "Excluir" e confirme a exclusão.

#### 5. **Gerenciar Contas a Receber**
   - **URL**: `/contas_a_receber`
   - **Passos**:
     1. Acesse a URL `/contas_a_receber` ou clique no menu da barra de navegação `Contas a Receber`.
     2. Visualize a lista de todas as suas contas a receber.
     3. Para adicionar uma nova conta, clique em "Adicionar Nova Conta a Receber".
     4. Preencha o formulário com as informações da receita (descrição, valor, data de recebimento, categoria, , status(Recebido ou Não)) e salve.
     5. Para editar uma conta existente, clique no botão "Editar" ao lado da conta desejada.
     6. Para excluir uma conta, clique no botão "Excluir" e confirme a exclusão.

#### 6. **Gerenciar Cartões de Crédito**
   - **URL**: `/cartoes_credito`
   - **Passos**:
     1. Acesse a URL `/cartoes_credito` ou clique no menu da barra de navegação `/cartoes_credito`.
     2. Visualize a lista de todos aos cartões cadastrados.
     3. Para adicionar um novo cartão, clique em "Cadastrar Novo Cartão de Crédito".
     4. Preencha o formulário com as informações da receita (nome, data de vencimento, limite e salve.
     5. Para editar um cartão existente, clique no botão "Editar" ao lado do cartão desejado.
     6. Para excluir um cartão, clique no botão "Excluir" e confirme a exclusão.

#### 7. **Gerenciar Compras com Cartão de Crédito**
   - **URL**: `/compras_cartao`
   - **Passos**:
     1. Acesse a URL `/compras_cartao` ou clique no menu da barra de navegação `Compras com Cartão`.
     2. Visualize a lista de todas as compras feitas com cartão de crédito, com informações de valor, data e parcelas.
     3. Para adicionar uma nova compra, clique em "Adicionar Nova Compra".
     4. Preencha o formulário com as informações da compra (descrição, valor, data, categoria, parcelas, cartão utilizado).
     5. O sistema automaticamente divide o valor pelas parcelas e cria os registros de cada parcela.
     6. Para visualizar as parcelas de uma compra, clique em "Ver Parcelas" ao lado da compra.
     7. Para excluir uma compra com cartão, clique no botão "Excluir" e confirme a exclusão, as parcelas serão excluidas jutamente com a compra.

#### 8. **Visualizar Parcelas de Compras com Cartão**
   - **URL**: `/compras_cartao/<int:compra_id>/parcelas`
   - **Passos**:
     1. Após cadastrar uma compra parcelada, acesse a URL `/compras_cartao` ou clique no menu da barra de navegação `Compras com Cartão`.
     2. Clique no botão "Ver Parcelas" ao lado da compra desejada.
     3. A página exibirá todas as parcelas, com valores e status (vencida, em dia ou vencimento em breve).

#### 9. **Gerar Relatórios Financeiros**
   - **URL**: `/relatorios`
   - **Passos**:
     1. Acesse a URL `/relatorios` ou clique no menu da barra de navegação `Relatórios`.
     2. Escolha o tipo de relatório (despesas por categoria ou saldo entre contas a pagar, receber e compras com cartão).
     3. Selecione o período de apuração.
     4. Clique em "Gerar Relatório" para visualizar os gráficos e dados.
     5. O relatório será exibido em forma de gráfico.

#### 10. **Gerenciar Perfil do Usuário**
   - **URL**: `/perfil_usuario`
   - **Passos**:
     1. Acesse a URL `/perfil_usuario` ou clique no menu da barra de navegação que contem o ícone de perfil e seu nome.
     2. Edite seu nome, e-mail e senha, se necessário.
     3. Salve as alterações.

#### 11. **Logout**
   - **URL**: `/logout`
   - **Passos**:
     1. Acesse a URL `/logout` ou clique no menu da barra de navegação que contem o ícone de logout e o texto sair.
     2. Você vai sair da conta e retornar à página de login.