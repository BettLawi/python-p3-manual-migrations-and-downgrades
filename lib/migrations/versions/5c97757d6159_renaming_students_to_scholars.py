"""Renaming students to scholars

Revision ID: 5c97757d6159
Revises: 791279dd0760
Create Date: 2023-09-07 07:47:10.557634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c97757d6159'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

