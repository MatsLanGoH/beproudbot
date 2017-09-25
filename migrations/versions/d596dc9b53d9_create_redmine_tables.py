"""create redmine tables

Revision ID: d596dc9b53d9
Revises: 2ffb0d589280
Create Date: 2017-08-14 14:43:31.234637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd596dc9b53d9'
down_revision = '2ffb0d589280'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('redmine_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=9), nullable=False, unique=True),
    sa.Column('api_key', sa.Unicode(length=40), nullable=False, unique=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('redmine_projectchannel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False, unique=True),
    sa.Column('channels', sa.Unicode(length=249), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('redmine_projectchannel')
    op.drop_table('redmine_users')
    ### end Alembic commands ###