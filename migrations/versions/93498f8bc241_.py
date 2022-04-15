"""empty message

Revision ID: 93498f8bc241
Revises: 2486d94cac4d
Create Date: 2022-04-09 22:46:20.138122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93498f8bc241'
down_revision = '2486d94cac4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('indicator_article', sa.Column('shortdesc', sa.Text(), nullable=True))
    op.drop_column('indicator_article', 'picturemidUrl')
    op.drop_column('indicator_article', 'pictureUrl')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('indicator_article', sa.Column('pictureUrl', sa.VARCHAR(length=40), nullable=True))
    op.add_column('indicator_article', sa.Column('picturemidUrl', sa.VARCHAR(length=40), nullable=True))
    op.drop_column('indicator_article', 'shortdesc')
    # ### end Alembic commands ###