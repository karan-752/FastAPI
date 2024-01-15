"""Create Post Table

Revision ID: 3beaeed595f8
Revises: 
Create Date: 2024-01-14 18:58:14.299438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3beaeed595f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
