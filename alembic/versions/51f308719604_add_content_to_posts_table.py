"""add content to posts table

Revision ID: 51f308719604
Revises: 938e1bb64f3f
Create Date: 2026-08-30 18:58:54.708750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51f308719604'
down_revision: Union[str, Sequence[str], None] = '938e1bb64f3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
