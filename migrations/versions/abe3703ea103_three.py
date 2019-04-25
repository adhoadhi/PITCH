"""three

Revision ID: abe3703ea103
Revises: c93f792d29c4
Create Date: 2019-04-25 12:21:09.862628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abe3703ea103'
down_revision = 'c93f792d29c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'c')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('c', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###