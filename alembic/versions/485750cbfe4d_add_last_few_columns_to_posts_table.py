"""add last few columns to posts table

Revision ID: 485750cbfe4d
Revises: 8e4a6a281c8a
Create Date: 2026-08-30 19:56:48.687292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '485750cbfe4d'
down_revision: Union[str, Sequence[str], None] = '8e4a6a281c8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='True'))
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()') ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
