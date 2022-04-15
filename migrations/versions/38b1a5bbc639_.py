"""empty message

Revision ID: 38b1a5bbc639
Revises: 5b57d61e1b69
Create Date: 2022-04-03 11:40:34.957800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38b1a5bbc639'
down_revision = '5b57d61e1b69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('imgSlug', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('articleDate', sa.DateTime(), nullable=True),
    sa.Column('articleText', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    # ### end Alembic commands ###
