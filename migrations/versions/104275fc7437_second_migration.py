"""Second migration

Revision ID: 104275fc7437
Revises: 87fedc688bb3
Create Date: 2020-12-10 21:05:03.435895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104275fc7437'
down_revision = '87fedc688bb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'blog_title')
    # ### end Alembic commands ###
