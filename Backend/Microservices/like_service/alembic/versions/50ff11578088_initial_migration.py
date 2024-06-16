"""Initial migration

Revision ID: 50ff11578088
Revises: f1fd0581ae6b
Create Date: 2024-06-20 08:42:07.623298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50ff11578088'
down_revision: Union[str, None] = 'f1fd0581ae6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('mobile_no', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_mobile_no'), 'users', ['mobile_no'], unique=True)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_table('discussions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_discussions_id'), 'discussions', ['id'], unique=False)
    op.create_index(op.f('ix_discussions_title'), 'discussions', ['title'], unique=False)
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content_id', sa.Integer(), nullable=False),
    sa.Column('content_type', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_likes_id'), 'likes', ['id'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('discussion_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['discussion_id'], ['discussions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_content'), 'comments', ['content'], unique=False)
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_index(op.f('ix_comments_content'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_likes_id'), table_name='likes')
    op.drop_table('likes')
    op.drop_index(op.f('ix_discussions_title'), table_name='discussions')
    op.drop_index(op.f('ix_discussions_id'), table_name='discussions')
    op.drop_table('discussions')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_mobile_no'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
