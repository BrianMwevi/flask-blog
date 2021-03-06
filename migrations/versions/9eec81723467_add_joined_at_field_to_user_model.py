"""Add joined_at field to user model

Revision ID: 9eec81723467
Revises: 895e9cad32bf
Create Date: 2022-05-27 01:48:33.226993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9eec81723467'
down_revision = '895e9cad32bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('author_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'subscriber', 'user', ['author_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('user_subscriber_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'subscriber_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('subscriber_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_subscriber_id_fkey', 'user', 'subscriber', ['subscriber_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'subscriber', type_='foreignkey')
    op.drop_column('subscriber', 'author_id')
    # ### end Alembic commands ###
