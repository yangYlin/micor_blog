"""new fields in user model

Revision ID: 7384408da364
Revises: 49c71cb9d3f4
Create Date: 2020-12-10 21:29:52.369852

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7384408da364'
down_revision = '49c71cb9d3f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###