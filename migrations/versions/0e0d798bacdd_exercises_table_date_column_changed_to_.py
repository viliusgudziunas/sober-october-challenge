"""Exercises table date column changed to timestamp

Revision ID: 0e0d798bacdd
Revises: ab7067930f8e
Create Date: 2019-10-07 15:58:55.631356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0d798bacdd'
down_revision = 'ab7067930f8e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('exercises', 'date', new_column_name='timestamp')


def downgrade():
    op.alter_column('exercises', 'timestamp', new_column_name='date')
