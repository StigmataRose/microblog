"""followers

Revision ID: 50dc8b9a1058
Revises: a15bc674ee1c
Create Date: 2024-05-28 11:37:03.111464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50dc8b9a1058'
down_revision = 'a15bc674ee1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
