"""Create addresses

Revision ID: 308fd6e66f02
Revises: 73f856b2ba63
Create Date: 2022-12-04 22:21:41.469765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308fd6e66f02'
down_revision = '73f856b2ba63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('neigborhod', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addresses')
    # ### end Alembic commands ###