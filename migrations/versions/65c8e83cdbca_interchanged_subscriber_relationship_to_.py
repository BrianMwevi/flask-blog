"""Interchanged subscriber relationship to User Model

Revision ID: 65c8e83cdbca
Revises: da0017bd2a25
Create Date: 2022-05-25 19:33:16.855086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c8e83cdbca'
down_revision = 'da0017bd2a25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subscriber', 'subscriber', ['user_id'], ['id'])
    op.drop_constraint('user_subscriber_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'subscriber_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('subscriber_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_subscriber_id_fkey', 'user', 'subscriber', ['subscriber_id'], ['id'])
    op.drop_constraint(None, 'subscriber', type_='foreignkey')
    op.drop_column('subscriber', 'user_id')
    # ### end Alembic commands ###
