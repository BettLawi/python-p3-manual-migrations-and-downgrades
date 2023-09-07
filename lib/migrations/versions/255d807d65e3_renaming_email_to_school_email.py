"""Renaming email to school email

Revision ID: 255d807d65e3
Revises: 5c97757d6159
Create Date: 2023-09-07 07:54:30.724849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '255d807d65e3'
down_revision = '5c97757d6159'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('email', 'school email')


def downgrade() -> None:
    op.rename_table('school email', 'email')
