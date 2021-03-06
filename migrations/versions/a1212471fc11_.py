"""empty message

Revision ID: a1212471fc11
Revises: 
Create Date: 2019-02-04 14:14:48.511927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1212471fc11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strategy',
    sa.Column('strategy_id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('strategy_id'),
    sa.UniqueConstraint('strategy_id')
    )
    op.create_index(op.f('ix_strategy_common_name'), 'strategy', ['common_name'], unique=True)
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strategy_id', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscription_strategy_id'), 'subscription', ['strategy_id'], unique=False)
    op.create_index(op.f('ix_subscription_timestamp'), 'subscription', ['timestamp'], unique=False)
    op.create_index(op.f('ix_subscription_username'), 'subscription', ['username'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('full_name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_date_joined'), 'user', ['date_joined'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('transaction',
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('security_id', sa.String(length=64), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=True),
    sa.Column('side', sa.String(length=64), nullable=True),
    sa.Column('limit', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('strategy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.strategy_id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    op.create_index(op.f('ix_transaction_security_id'), 'transaction', ['security_id'], unique=False)
    op.create_index(op.f('ix_transaction_side'), 'transaction', ['side'], unique=False)
    op.create_index(op.f('ix_transaction_timestamp'), 'transaction', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_timestamp'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_side'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_security_id'), table_name='transaction')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_date_joined'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_subscription_username'), table_name='subscription')
    op.drop_index(op.f('ix_subscription_timestamp'), table_name='subscription')
    op.drop_index(op.f('ix_subscription_strategy_id'), table_name='subscription')
    op.drop_table('subscription')
    op.drop_index(op.f('ix_strategy_common_name'), table_name='strategy')
    op.drop_table('strategy')
    # ### end Alembic commands ###
