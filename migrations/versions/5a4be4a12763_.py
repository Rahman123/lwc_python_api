"""empty message

Revision ID: 5a4be4a12763
Revises: 65ae59711a88
Create Date: 2020-04-04 20:32:37.329647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a4be4a12763'
down_revision = '65ae59711a88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('joblistings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('datePosted', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('joblistings')
    # ### end Alembic commands ###
