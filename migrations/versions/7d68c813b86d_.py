"""empty message

Revision ID: 7d68c813b86d
Revises: dae7c61bb20a
Create Date: 2022-04-10 12:11:55.327422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d68c813b86d'
down_revision = 'dae7c61bb20a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expectation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ShortName', sa.String(length=30), nullable=True),
    sa.Column('time_Open', sa.String(length=30), nullable=True),
    sa.Column('Open', sa.Float(), nullable=True),
    sa.Column('Close', sa.Float(), nullable=True),
    sa.Column('High', sa.Float(), nullable=True),
    sa.Column('Low', sa.Float(), nullable=True),
    sa.Column('Volume', sa.Float(), nullable=True),
    sa.Column('trades_Count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('XRP_prc')
    op.drop_table('ADA_prc')
    op.drop_table('SOL_prc')
    op.drop_table('BNB_prc')
    op.drop_table('LUNA_prc')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LUNA_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('time_Open', sa.VARCHAR(length=30), nullable=True),
    sa.Column('Open', sa.FLOAT(), nullable=True),
    sa.Column('Close', sa.FLOAT(), nullable=True),
    sa.Column('High', sa.FLOAT(), nullable=True),
    sa.Column('Low', sa.FLOAT(), nullable=True),
    sa.Column('Volume', sa.FLOAT(), nullable=True),
    sa.Column('trades_Count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('BNB_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('time_Open', sa.VARCHAR(length=30), nullable=True),
    sa.Column('Open', sa.FLOAT(), nullable=True),
    sa.Column('Close', sa.FLOAT(), nullable=True),
    sa.Column('High', sa.FLOAT(), nullable=True),
    sa.Column('Low', sa.FLOAT(), nullable=True),
    sa.Column('Volume', sa.FLOAT(), nullable=True),
    sa.Column('trades_Count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SOL_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('time_Open', sa.VARCHAR(length=30), nullable=True),
    sa.Column('Open', sa.FLOAT(), nullable=True),
    sa.Column('Close', sa.FLOAT(), nullable=True),
    sa.Column('High', sa.FLOAT(), nullable=True),
    sa.Column('Low', sa.FLOAT(), nullable=True),
    sa.Column('Volume', sa.FLOAT(), nullable=True),
    sa.Column('trades_Count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ADA_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('time_Open', sa.VARCHAR(length=30), nullable=True),
    sa.Column('Open', sa.FLOAT(), nullable=True),
    sa.Column('Close', sa.FLOAT(), nullable=True),
    sa.Column('High', sa.FLOAT(), nullable=True),
    sa.Column('Low', sa.FLOAT(), nullable=True),
    sa.Column('Volume', sa.FLOAT(), nullable=True),
    sa.Column('trades_Count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('XRP_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('time_Open', sa.VARCHAR(length=30), nullable=True),
    sa.Column('Open', sa.FLOAT(), nullable=True),
    sa.Column('Close', sa.FLOAT(), nullable=True),
    sa.Column('High', sa.FLOAT(), nullable=True),
    sa.Column('Low', sa.FLOAT(), nullable=True),
    sa.Column('Volume', sa.FLOAT(), nullable=True),
    sa.Column('trades_Count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('expectation')
    # ### end Alembic commands ###