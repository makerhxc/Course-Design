"""empty message

Revision ID: 4c15b56417ac
Revises: 
Create Date: 2020-01-05 11:55:47.743072

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4c15b56417ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blogs', 'bauid',
               existing_type=mysql.INTEGER(display_width=5),
               nullable=True)
    op.alter_column('blogs', 'btext',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.create_foreign_key(None, 'blogs', 'users', ['bauid'], ['uid'])
    op.alter_column('commits', 'bid',
               existing_type=mysql.INTEGER(display_width=7),
               nullable=True)
    op.alter_column('commits', 'cau',
               existing_type=mysql.INTEGER(display_width=5),
               nullable=True)
    op.alter_column('commits', 'ctext',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.create_foreign_key(None, 'commits', 'users', ['cau'], ['uid'])
    op.create_foreign_key(None, 'commits', 'blogs', ['bid'], ['bid'])
    op.alter_column('users', 'uemail',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20),
               nullable=True)
    op.alter_column('users', 'uname',
               existing_type=mysql.CHAR(charset='utf8', length=20),
               nullable=True)
    op.alter_column('users', 'upasswd',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20),
               nullable=True)
    op.create_index(op.f('ix_users_uemail'), 'users', ['uemail'], unique=True)
    op.create_index(op.f('ix_users_uname'), 'users', ['uname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_uname'), table_name='users')
    op.drop_index(op.f('ix_users_uemail'), table_name='users')
    op.alter_column('users', 'upasswd',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20),
               nullable=False)
    op.alter_column('users', 'uname',
               existing_type=mysql.CHAR(charset='utf8', length=20),
               nullable=False)
    op.alter_column('users', 'uemail',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20),
               nullable=False)
    op.drop_constraint(None, 'commits', type_='foreignkey')
    op.drop_constraint(None, 'commits', type_='foreignkey')
    op.alter_column('commits', 'ctext',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('commits', 'cau',
               existing_type=mysql.INTEGER(display_width=5),
               nullable=False)
    op.alter_column('commits', 'bid',
               existing_type=mysql.INTEGER(display_width=7),
               nullable=False)
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.alter_column('blogs', 'btext',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('blogs', 'bauid',
               existing_type=mysql.INTEGER(display_width=5),
               nullable=False)
    # ### end Alembic commands ###