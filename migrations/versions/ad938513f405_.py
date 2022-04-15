"""empty message

Revision ID: ad938513f405
Revises: ced5498db9b1
Create Date: 2022-04-09 15:40:21.369061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad938513f405'
down_revision = 'ced5498db9b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('indicator_article', sa.Column('name', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('indicator_article', 'name')
    # ### end Alembic commands ###