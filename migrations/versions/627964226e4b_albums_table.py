"""albums table

Revision ID: 627964226e4b
Revises: a54ee921105b
Create Date: 2020-12-30 16:07:13.702201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '627964226e4b'
down_revision = 'a54ee921105b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('albums')
    # ### end Alembic commands ###
