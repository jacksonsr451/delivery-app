"""Update users

Revision ID: 117f1689768c
Revises: 8feaba29dc09
Create Date: 2022-12-05 18:47:18.570543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117f1689768c'
down_revision = '8feaba29dc09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###