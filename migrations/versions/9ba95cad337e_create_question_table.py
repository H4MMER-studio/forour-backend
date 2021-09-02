"""create question table

Revision ID: 9ba95cad337e
Revises: 
Create Date: 2021-08-30 01:02:43.909436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba95cad337e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade():
    op.drop_table("questions")
    pass
