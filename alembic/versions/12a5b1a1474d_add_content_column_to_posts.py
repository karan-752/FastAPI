"""Add Content Column to Posts

Revision ID: 12a5b1a1474d
Revises: 3beaeed595f8
Create Date: 2024-01-14 23:01:21.902113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12a5b1a1474d'
down_revision = '3beaeed595f8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column("posts", 'content')
    pass
