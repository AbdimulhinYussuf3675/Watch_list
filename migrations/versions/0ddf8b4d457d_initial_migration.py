"""Initial Migration

Revision ID: 0ddf8b4d457d
Revises: 4ffcf25df101
Create Date: 2021-06-09 06:50:12.671836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ddf8b4d457d'
down_revision = '4ffcf25df101'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_aecure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_aecure')
    # ### end Alembic commands ###
