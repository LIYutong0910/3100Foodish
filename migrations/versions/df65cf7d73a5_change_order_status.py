"""change order status

Revision ID: df65cf7d73a5
Revises: f9c43e75a67c
Create Date: 2019-03-05 13:21:38.534034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df65cf7d73a5'
down_revision = 'f9c43e75a67c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('status', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'status')
    # ### end Alembic commands ###