"""Change is_active to is_subscriber in Subscriber model

Revision ID: c3a6af9cd49e
Revises: 94e12a392376
Create Date: 2022-05-25 16:55:27.035823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3a6af9cd49e'
down_revision = '94e12a392376'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('is_subscriber', sa.Boolean(), nullable=True))
    op.drop_column('subscriber', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('subscriber', 'is_subscriber')
    # ### end Alembic commands ###
