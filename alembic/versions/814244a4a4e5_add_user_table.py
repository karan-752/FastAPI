"""Add User Table

Revision ID: 814244a4a4e5
Revises: 12a5b1a1474d
Create Date: 2024-01-14 23:31:17.403369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814244a4a4e5'
down_revision = '12a5b1a1474d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
