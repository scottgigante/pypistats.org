"""add percentage columns to category tables

Revision ID: 698d47684405
Revises: a91799876ec2
Create Date: 2018-09-05 20:33:50.005922

"""
# flake8: noqa
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698d47684405'
down_revision = 'a91799876ec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('python_major', sa.Column('percentages', sa.Float(), nullable=True))
    op.add_column('python_minor', sa.Column('percentages', sa.Float(), nullable=True))
    op.add_column('system', sa.Column('percentages', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('system', 'percentages')
    op.drop_column('python_minor', 'percentages')
    op.drop_column('python_major', 'percentages')
    # ### end Alembic commands ###