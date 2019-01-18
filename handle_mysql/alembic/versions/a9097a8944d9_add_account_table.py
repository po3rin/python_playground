"""Add account table

Revision ID: a9097a8944d9
Revises: None
Create Date: 2019-01-18 17:33:45.982064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9097a8944d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(32), nullable=False),
    )


def downgrade():
    op.drop_table('account')
