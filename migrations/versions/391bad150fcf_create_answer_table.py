"""create answer table

Revision ID: 391bad150fcf
Revises: 9ba95cad337e
Create Date: 2021-09-03 02:24:53.935540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391bad150fcf'
down_revision = '9ba95cad337e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_a", sa.JSON(), nullable=False),
        sa.Column("content_b", sa.JSON(), nullable=False),
        sa.Column("question_id", sa.Integer()),
        sa.ForeignKeyConstraint(
            ["question_id"], ["questions.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade():
    op.drop_table("answers")
