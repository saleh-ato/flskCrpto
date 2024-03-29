"""empty message

Revision ID: 3b204454e08e
Revises: 38b1a5bbc639
Create Date: 2022-04-09 11:46:30.199135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b204454e08e'
down_revision = '38b1a5bbc639'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usual_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Website', sa.String(length=45), nullable=True),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('MaxSupply', sa.Integer(), nullable=True),
    sa.Column('GitHubLink', sa.String(length=55), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usual_info')
    # ### end Alembic commands ###
