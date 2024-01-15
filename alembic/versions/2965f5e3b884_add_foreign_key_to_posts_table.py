"""Add Foreign Key to Posts Table

Revision ID: 2965f5e3b884
Revises: 814244a4a4e5
Create Date: 2024-01-14 23:50:27.146361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2965f5e3b884'
down_revision = '814244a4a4e5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
