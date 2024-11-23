-- Criação da tabela de usuários
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de contas a pagar
CREATE TABLE conta_a_pagar (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL,
    data_vencimento DATE NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    categoria VARCHAR(50),
    usuario_id INTEGER REFERENCES usuario(id) ON DELETE CASCADE
);

-- Criação da tabela de contas a receber
CREATE TABLE conta_a_receber (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL,
    data_recebimento DATE NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    categoria VARCHAR(50),
    usuario_id INTEGER REFERENCES usuario(id) ON DELETE CASCADE
);

-- Criação da tabela de compras com cartão de crédito
CREATE TABLE compra_cartao_credito (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL,
    data_compra DATE NOT NULL,
    categoria VARCHAR(50),
    num_parcelas INTEGER DEFAULT 1,
    cartao_utilizado VARCHAR(50),
    limite_cartao NUMERIC(10, 2) NOT NULL,
    usuario_id INTEGER REFERENCES usuario(id) ON DELETE CASCADE
);

-- Criação da tabela de parcelas do cartão de crédito
CREATE TABLE parcelas_cartao (
    id SERIAL PRIMARY KEY,
    compra_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    numero_parcela INTEGER NOT NULL,
    valor_parcela NUMERIC(10, 2) NOT NULL,
    data_parcela DATE NOT NULL,
    FOREIGN KEY (compra_id) REFERENCES compra_cartao_credito(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

-- Criação da tabela de relatórios financeiros
CREATE TABLE relatorio_financeiro (
    id SERIAL PRIMARY KEY,
    tipo_relatorio VARCHAR(50) NOT NULL,
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INTEGER REFERENCES usuario(id) ON DELETE CASCADE
);
