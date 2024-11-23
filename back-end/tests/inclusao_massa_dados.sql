-- Inserindo usuários
INSERT INTO usuario (nome, email, senha) VALUES
('João Silva', 'joao.silva@email.com', 'scrypt:32768:8:1$bNxOm1CqVJKWasAb$50c2ee763352ec2d81570822526ff29dcdf184818baa222196ad2d8a6ca2556b55fc7f108f7ab4b4f193e39dd4908a52ffd3c2dbf24546aea2aeaff5b5232e4a'), /*senha123*/
('Maria Oliveira', 'maria.oliveira@email.com', 'scrypt:32768:8:1$bNxOm1CqVJKWasAb$50c2ee763352ec2d81570822526ff29dcdf184818baa222196ad2d8a6ca2556b55fc7f108f7ab4b4f193e39dd4908a52ffd3c2dbf24546aea2aeaff5b5232e4a'), /*senha123*/
('Carlos Souza', 'carlos.souza@email.com', 'scrypt:32768:8:1$bNxOm1CqVJKWasAb$50c2ee763352ec2d81570822526ff29dcdf184818baa222196ad2d8a6ca2556b55fc7f108f7ab4b4f193e39dd4908a52ffd3c2dbf24546aea2aeaff5b5232e4a'), /*senha123*/
('Ana Pereira', 'ana.pereira@email.com', 'scrypt:32768:8:1$bNxOm1CqVJKWasAb$50c2ee763352ec2d81570822526ff29dcdf184818baa222196ad2d8a6ca2556b55fc7f108f7ab4b4f193e39dd4908a52ffd3c2dbf24546aea2aeaff5b5232e4a'), /*senha123*/
('Lucas Lima', 'lucas.lima@email.com', 'scrypt:32768:8:1$bNxOm1CqVJKWasAb$50c2ee763352ec2d81570822526ff29dcdf184818baa222196ad2d8a6ca2556b55fc7f108f7ab4b4f193e39dd4908a52ffd3c2dbf24546aea2aeaff5b5232e4a'); /*senha123*/

-- Inserindo contas a pagar
INSERT INTO conta_a_pagar (descricao, valor, data_vencimento, status, categoria, usuario_id) VALUES
('Aluguel', 1200.00, '2024-10-05', false, 'Moradia', 1),
('Conta de Luz', 150.75, '2024-10-10', false, 'Moradia', 1),
('Plano de Saúde', 450.00, '2024-10-15', true, 'Saúde', 2),
('Mensalidade Escolar', 800.00, '2024-10-20', false, 'Educação', 3),
('Internet', 100.00, '2024-10-25', false, 'Internet', 4),
('Netflix', 45.90, '2024-10-30', false, 'Lazer', 5),
('Conta de Água', 100.00, '2024-11-01', false, 'Moradia', 1),
('Energia Elétrica', 200.00, '2024-11-05', false, 'Moradia', 2),
('Plano de Saúde', 500.00, '2024-11-10', true, 'Saúde', 3),
('Curso Online', 150.00, '2024-11-15', false, 'Educação', 4),
('Mensalidade Academia', 80.00, '2024-11-20', true, 'Despesas Pessoais', 5),
('Internet', 120.00, '2024-11-25', false, 'Internet', 1),
('Telefone Fixo', 50.00, '2024-11-30', true, 'Telefonia', 2),
('Parcela Carro', 1000.00, '2024-11-28', false, 'Transporte', 3),
('Streaming TV', 30.00, '2024-12-01', false, 'Lazer', 4),
('Condomínio', 300.00, '2024-12-10', false, 'Moradia', 5);

-- Inserindo contas a receber
INSERT INTO conta_a_receber (descricao, valor, data_recebimento, status, categoria, usuario_id) VALUES
('Salário Setembro', 5000.00, '2024-10-01', true, 'Salário', 1),
('Venda Carro', 20000.00, '2024-10-07', false, 'Vendas', 2),
('Freelance Website', 1500.00, '2024-10-15', false, 'Freelance', 3),
('Seguro de Vida', 1000.00, '2024-10-20', true, 'Seguro', 4),
('Restituição IR', 2500.00, '2024-10-22', false, 'Restituição IR', 5),
('Salário Mensal', 5000.00, '2024-11-30', true, 'Salário', 1),
('Comissão de Vendas', 1200.00, '2024-11-15', false, 'Vendas', 2),
('Reembolso Seguro', 800.00, '2024-12-01', false, 'Seguro', 3),
('Doação Parente', 500.00, '2024-12-05', false, 'Doação', 4),
('Vaquinha Digital', 200.00, '2024-12-10', true, 'Vaquinha', 5),
('Rendimentos Investimentos', 300.00, '2024-11-25', true, 'Rendimentos', 1),
('Freelance Projeto', 1500.00, '2024-12-20', false, 'Freelance', 2),
('Bonificação Anual', 1000.00, '2024-12-15', true, 'Bonificação', 3),
('Férias', 2000.00, '2024-12-20', true, 'Férias', 4),
('Restituição IR', 700.00, '2024-12-31', false, 'Restituição IR', 5);

-- Inserindo cartões de crédito
INSERT INTO cartao_credito (nome_cartao, limite_cartao, data_vencimento, usuario_id) VALUES
('Visa', 15000.00, '2024-12-31', 1),
('Mastercard', 4000.00, '2024-11-30', 2),
('Amex', 10000.00, '2024-10-31', 4);

-- Inserindo compras com cartão de crédito
INSERT INTO compra_cartao_credito (descricao, valor, data_compra, categoria, num_parcelas, cartao_utilizado, usuario_id) VALUES
('Supermercado', 300.00, '2024-10-05', 'Alimentação', 1, 1, 1),
('Compra de Livros', 150.00, '2024-10-07', 'Educação', 3, 2, 2),
('Academia', 200.00, '2024-10-10', 'Saúde', 2, 1, 1),
('Celular Novo', 1200.00, '2024-10-12', 'Despesas Pessoais', 12, 3, 4),
('Viagem', 5000.00, '2024-10-20', 'Lazer', 6, 1, 1),
('Supermercado', 400.00, '2024-11-05', 'Alimentação', 1, 1, 1),
('Notebook Novo', 3500.00, '2024-11-10', 'Educação', 6, 2, 2),
('Refeição Restaurante', 120.00, '2024-11-12', 'Alimentação', 1, 1, 1),
('Fones de Ouvido', 300.00, '2024-11-15', 'Despesas Pessoais', 3, 3, 4),
('Viagem de Férias', 8000.00, '2024-12-01', 'Lazer', 12, 1, 1);

-- Inserindo parcelas de compras com cartão de crédito
INSERT INTO parcelas_cartao (compra_id, usuario_id, numero_parcela, valor_parcela, data_parcela) VALUES
(1, 1, 1, 300.00, '2024-10-05'),
(2, 2, 1, 50.00, '2024-11-07'),
(2, 2, 2, 50.00, '2024-12-07'),
(2, 2, 3, 50.00, '2025-01-07'),
(3, 1, 1, 100.00, '2024-11-10'),
(3, 1, 2, 100.00, '2024-12-10'),
(4, 4, 1, 100.00, '2024-11-12'),
(4, 4, 2, 100.00, '2024-12-12'),
(4, 4, 3, 100.00, '2025-01-12'),
(4, 4, 4, 100.00, '2025-02-12'),
(4, 4, 5, 100.00, '2025-03-12'),
(4, 4, 6, 100.00, '2025-04-12'),
(4, 4, 7, 100.00, '2025-05-12'),
(4, 4, 8, 100.00, '2025-06-12'),
(4, 4, 9, 100.00, '2025-07-12'),
(4, 4, 10, 100.00, '2025-08-12'),
(4, 4, 11, 100.00, '2025-09-12'),
(4, 4, 12, 100.00, '2025-10-12'),
(5, 1, 1, 833.33, '2024-11-20'),
(5, 1, 2, 833.33, '2024-12-20'),
(5, 1, 3, 833.33, '2025-01-20'),
(5, 1, 4, 833.33, '2025-02-20'),
(5, 1, 5, 833.33, '2025-03-20'),
(5, 1, 6, 833.33, '2025-04-20'),
(6, 1, 1, 400.00, '2024-11-05'),
(7, 2, 1, 583.33, '2024-12-10'),
(7, 2, 2, 583.33, '2025-01-10'),
(7, 2, 3, 583.33, '2025-02-10'),
(7, 2, 4, 583.33, '2025-03-10'),
(7, 2, 5, 583.33, '2025-04-10'),
(7, 2, 6, 583.33, '2025-05-10'),
(8, 1, 1, 120.00, '2024-11-12'),
(9, 4, 1, 100.00, '2024-12-15'),
(9, 4, 2, 100.00, '2025-01-15'),
(9, 4, 3, 100.00, '2025-02-15'),
(10, 1, 1, 666.67, '2024-12-01'),
(10, 1, 2, 666.67, '2025-01-01'),
(10, 1, 3, 666.67, '2025-02-01'),
(10, 1, 4, 666.67, '2025-03-01'),
(10, 1, 5, 666.67, '2025-04-01'),
(10, 1, 6, 666.67, '2025-05-01'),
(10, 1, 7, 666.67, '2025-06-01'),
(10, 1, 8, 666.67, '2025-07-01'),
(10, 1, 9, 666.67, '2025-08-01'),
(10, 1, 10, 666.67, '2025-09-01'),
(10, 1, 11, 666.67, '2025-10-01'),
(10, 1, 12, 666.67, '2025-11-01');
