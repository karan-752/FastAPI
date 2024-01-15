"""Add Columns to Post Table

Revision ID: 8d58b6317d1d
Revises: 2965f5e3b884
Create Date: 2024-01-15 00:09:59.005406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d58b6317d1d'
down_revision = '2965f5e3b884'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.BOOLEAN, nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
