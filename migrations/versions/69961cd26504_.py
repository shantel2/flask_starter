"""empty message

Revision ID: 69961cd26504
Revises: 
Create Date: 2022-03-21 00:07:02.410287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69961cd26504'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=80), nullable=True),
    sa.Column('Description', sa.String(length=2355), nullable=True),
    sa.Column('No. of Rooms', sa.String(length=3), nullable=True),
    sa.Column('No. of Bathrooms', sa.String(length=3), nullable=True),
    sa.Column('Price', sa.String(length=12), nullable=True),
    sa.Column('Property Type', sa.String(length=9), nullable=True),
    sa.Column('Location', sa.String(length=80), nullable=True),
    sa.Column('Photo Name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homes')
    # ### end Alembic commands ###
