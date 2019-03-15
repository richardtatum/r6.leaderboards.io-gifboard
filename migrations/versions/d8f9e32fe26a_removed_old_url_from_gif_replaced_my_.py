"""removed old url from gif, replaced my webm and mp4

Revision ID: d8f9e32fe26a
Revises: 3ff1abe164ce
Create Date: 2019-03-05 11:32:16.682770

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8f9e32fe26a'
down_revision = '3ff1abe164ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gif', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gif', sa.Column('url', mysql.VARCHAR(length=256), nullable=True))
    # ### end Alembic commands ###
