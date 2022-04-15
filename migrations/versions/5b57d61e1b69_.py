"""empty message

Revision ID: 5b57d61e1b69
Revises: 
Create Date: 2022-02-19 04:45:16.687579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b57d61e1b69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BTC_prc',
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
    op.create_table('coins__table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ShortName', sa.String(length=10), nullable=True),
    sa.Column('FullName', sa.String(length=20), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('percent', sa.String(length=10), nullable=True),
    sa.Column('marketcap', sa.String(length=20), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coins__table')
    op.drop_table('BTC_prc')
    # ### end Alembic commands ###
