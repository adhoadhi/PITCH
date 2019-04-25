"""second

Revision ID: 184aef8bddaf
Revises: a15624f0a827
Create Date: 2019-04-25 10:54:17.504517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '184aef8bddaf'
down_revision = 'a15624f0a827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'pitch_categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###
