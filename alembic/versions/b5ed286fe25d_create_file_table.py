"""create file table

Revision ID: b5ed286fe25d
Revises: 
Create Date: 2021-10-06 22:34:41.265217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5ed286fe25d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('file',
                    sa.Column('id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True),
                    sa.Column('password', sa.String(255), nullable=False),
                    sa.Column('filename', sa.String(255), unique=True))


def downgrade():
    op.drop_table('file')
