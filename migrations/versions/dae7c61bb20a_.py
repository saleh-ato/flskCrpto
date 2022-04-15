"""empty message

Revision ID: dae7c61bb20a
Revises: 339b0490c3ce
Create Date: 2022-04-10 10:31:07.293614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dae7c61bb20a'
down_revision = '339b0490c3ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ADA_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('BNB_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ETH_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('LUNA_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SOL_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('XRP_prc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('XRP_prc')
    op.drop_table('SOL_prc')
    op.drop_table('LUNA_prc')
    op.drop_table('ETH_prc')
    op.drop_table('BNB_prc')
    op.drop_table('ADA_prc')
    # ### end Alembic commands ###
