"""fix viewed field

Revision ID: 64f062cdb8eb
Revises: 0b3f9309d615
Create Date: 2019-08-17 22:00:18.167494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64f062cdb8eb'
down_revision = '0b3f9309d615'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('viewed',
               existing_type=sa.BLOB(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('viewed',
               existing_type=sa.BLOB(),
               nullable=True)

    # ### end Alembic commands ###
