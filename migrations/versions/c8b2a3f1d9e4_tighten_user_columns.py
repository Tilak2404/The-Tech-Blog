'''tighten user columns

Revision ID: c8b2a3f1d9e4
Revises: 806ec8923758
Create Date: 2026-02-26 00:00:00

'''
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8b2a3f1d9e4'
down_revision = '806ec8923758'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column(
            'profile_image',
            existing_type=sa.String(length=20),
            type_=sa.String(length=128),
            existing_nullable=False,
        )
        batch_op.alter_column(
            'email',
            existing_type=sa.String(length=64),
            nullable=False,
        )
        batch_op.alter_column(
            'username',
            existing_type=sa.String(length=64),
            nullable=False,
        )
        batch_op.alter_column(
            'password_hash',
            existing_type=sa.String(length=128),
            nullable=False,
        )


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column(
            'password_hash',
            existing_type=sa.String(length=128),
            nullable=True,
        )
        batch_op.alter_column(
            'username',
            existing_type=sa.String(length=64),
            nullable=True,
        )
        batch_op.alter_column(
            'email',
            existing_type=sa.String(length=64),
            nullable=True,
        )
        batch_op.alter_column(
            'profile_image',
            existing_type=sa.String(length=128),
            type_=sa.String(length=20),
            existing_nullable=False,
        )
