"""Added mp4, webm and single frame columns to gif

Revision ID: 3ff1abe164ce
Revises: 202f848131fe
Create Date: 2019-03-05 11:30:58.511715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ff1abe164ce'
down_revision = '202f848131fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gif', sa.Column('frame', sa.String(length=256), nullable=True))
    op.add_column('gif', sa.Column('mp4', sa.String(length=256), nullable=True))
    op.add_column('gif', sa.Column('webm', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gif', 'webm')
    op.drop_column('gif', 'mp4')
    op.drop_column('gif', 'frame')
    # ### end Alembic commands ###