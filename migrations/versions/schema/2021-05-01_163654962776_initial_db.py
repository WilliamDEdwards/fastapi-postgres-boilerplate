"""initial_db.

Revision ID: 163654962776
Revises: 
Create Date: 2021-05-01 04:18:05.217003

"""
import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op
from server import db

# revision identifiers, used by Alembic.
revision = '163654962776'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public')

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_types',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('product_type', sa.String(length=510), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_type')
    )
    op.create_table('products',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('created_at', db.UtcTimestamp(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', db.UtcTimestamp(timezone=True), nullable=False),
    sa.Column('updated_at', db.UtcTimestamp(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('created_at', db.UtcTimestamp(timezone=True),nullable=False),
    sa.Column('updated_at', db.UtcTimestamp(timezone=True),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('products')
    op.drop_table('product_types')
    # ### end Alembic commands ###
