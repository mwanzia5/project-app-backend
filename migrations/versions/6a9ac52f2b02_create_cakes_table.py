"""create cakes table

Revision ID: 6a9ac52f2b02
Revises: 
Create Date: 2023-12-20 16:42:13.146105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a9ac52f2b02'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Text(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cakes')
    # ### end Alembic commands ###
