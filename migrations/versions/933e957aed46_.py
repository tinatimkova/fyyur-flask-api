"""empty message

Revision ID: 933e957aed46
Revises: fa7961ef17fe
Create Date: 2020-05-06 15:18:38.250315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933e957aed46'
down_revision = 'fa7961ef17fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
