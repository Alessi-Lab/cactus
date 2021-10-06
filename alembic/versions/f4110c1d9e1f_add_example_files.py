"""Add example files

Revision ID: f4110c1d9e1f
Revises: b5ed286fe25d
Create Date: 2021-10-06 22:48:07.070855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from cactus.database import File

revision = 'f4110c1d9e1f'
down_revision = 'b5ed286fe25d'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
