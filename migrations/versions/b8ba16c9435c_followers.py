"""followers

Revision ID: b8ba16c9435c
Revises: 7384408da364
Create Date: 2020-12-23 22:53:11.093483

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b8ba16c9435c'
down_revision = '7384408da364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
                    sa.Column('follower_id', sa.Integer(), nullable=True),
                    sa.Column('followed_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
