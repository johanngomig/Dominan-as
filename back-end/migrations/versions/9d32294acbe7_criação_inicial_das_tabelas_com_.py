"""Criação inicial das tabelas com migration

Revision ID: 9d32294acbe7
Revises: 
Create Date: 2024-09-14 13:34:26.040746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9d32294acbe7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criação da tabela de usuários
    op.create_table(
        'usuario',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('senha', sa.String(255), nullable=False),
        sa.Column('data_criacao', sa.TIMESTAMP, server_default=sa.func.now())
    )

    # Criação da tabela de contas a pagar
    op.create_table(
        'conta_a_pagar',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('descricao', sa.String(255), nullable=False),
        sa.Column('valor', sa.Numeric(10, 2), nullable=False),
        sa.Column('data_vencimento', sa.Date, nullable=False),
        sa.Column('status', sa.Boolean, default=False),
        sa.Column('categoria', sa.String(50)),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE"))
    )

    # Criação da tabela de contas a receber
    op.create_table(
        'conta_a_receber',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('descricao', sa.String(255), nullable=False),
        sa.Column('valor', sa.Numeric(10, 2), nullable=False),
        sa.Column('data_recebimento', sa.Date, nullable=False),
        sa.Column('status', sa.Boolean, default=False),
        sa.Column('categoria', sa.String(50)),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE"))
    )

    # Criação da tabela de cartão de crédito
    op.create_table(
        'cartao_credito',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome_cartao', sa.String(50), nullable=False),
        sa.Column('data_vencimento', sa.Date, nullable=False),
        sa.Column('limite_cartao', sa.Numeric(10, 2), nullable=False),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE"))
    )
    
    # Criação da tabela de compras com cartão de crédito
    op.create_table(
        'compra_cartao_credito',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('descricao', sa.String(255), nullable=False),
        sa.Column('valor', sa.Numeric(10, 2), nullable=False),
        sa.Column('data_compra', sa.Date, nullable=False),
        sa.Column('categoria', sa.String(50)),
        sa.Column('num_parcelas', sa.Integer, default=1),
        sa.Column('cartao_utilizado', sa.Integer, sa.ForeignKey('cartao_credito.id', ondelete="CASCADE")),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE"))
    )

    # Criação da tabela de parcelas do cartão
    op.create_table(
        'parcelas_cartao',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('compra_id', sa.Integer, sa.ForeignKey('compra_cartao_credito.id', ondelete="CASCADE")),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE")),
        sa.Column('numero_parcela', sa.Integer, nullable=False),
        sa.Column('valor_parcela', sa.Numeric(10, 2), nullable=False),
        sa.Column('data_parcela', sa.Date, nullable=False)
    )

    # Criação da tabela de relatórios financeiros
    op.create_table(
        'relatorio_financeiro',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tipo_relatorio', sa.String(50), nullable=False),
        sa.Column('data_geracao', sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuario.id', ondelete="CASCADE"))
    )


def downgrade() -> None:
    # Reversão das tabelas
    op.drop_table('relatorio_financeiro')
    op.drop_table('parcelas_cartao')
    op.drop_table('compra_cartao_credito')
    op.drop_table('cartao_credito')
    op.drop_table('conta_a_receber')
    op.drop_table('conta_a_pagar')
    op.drop_table('usuario')
