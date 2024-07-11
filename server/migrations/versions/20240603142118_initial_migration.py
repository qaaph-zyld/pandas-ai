"""initial_migration

Revision ID: 51e3880da98b
Revises: 
Create Date: 2024-06-03 14:21:18.361386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "51e3880da98b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organization",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("is_default", sa.Boolean(), nullable=True),
        sa.Column("settings", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_organization_id"), "organization", ["id"], unique=False)
    op.create_index(
        op.f("ix_organization_name"), "organization", ["name"], unique=False
    )
    op.create_table(
        "user",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("first_name", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("verified", sa.Boolean(), nullable=True),
        sa.Column("last_name", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_table(
        "api_keys",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.Column("api_key", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_api_keys_id"), "api_keys", ["id"], unique=False)
    op.create_table(
        "connector",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("config", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id", name="uq_connector_id"),
    )
    op.create_index(op.f("ix_connector_id"), "connector", ["id"], unique=False)
    op.create_table(
        "organization_membership",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.Column("role", sa.String(), nullable=True),
        sa.Column("verified", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_organization_membership_id"),
        "organization_membership",
        ["id"],
        unique=False,
    )
    op.create_table(
        "workspace",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.Column("slug", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_workspace_id"), "workspace", ["id"], unique=False)
    op.create_table(
        "dataset",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("table_name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("head", sa.JSON(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.Column("connector_id", sa.UUID(), nullable=True),
        sa.Column("field_descriptions", sa.JSON(), nullable=True),
        sa.Column("filterable_columns", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(
            ["connector_id"],
            ["connector.id"],
        ),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_dataset_id"), "dataset", ["id"], unique=False)
    op.create_table(
        "user_conversation",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("workspace_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("valid", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspace.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_user_conversation_id"), "user_conversation", ["id"], unique=False
    )
    op.create_table(
        "user_space",
        sa.Column("workspace_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspace.id"],
        ),
        sa.PrimaryKeyConstraint("workspace_id", "user_id"),
    )
    op.create_table(
        "conversation_message",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("conversation_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("query", sa.String(), nullable=True),
        sa.Column("response", sa.JSON(), nullable=True),
        sa.Column("code_generated", sa.String(), nullable=True),
        sa.Column("label", sa.String(), nullable=True),
        sa.Column("log_id", sa.UUID(), nullable=True),
        sa.Column("settings", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(
            ["conversation_id"],
            ["user_conversation.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_conversation_message_id"), "conversation_message", ["id"], unique=False
    )
    op.create_table(
        "dataset_space",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("dataset_id", sa.UUID(), nullable=True),
        sa.Column("workspace_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["dataset_id"],
            ["dataset.id"],
        ),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspace.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_dataset_space_id"), "dataset_space", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_dataset_space_id"), table_name="dataset_space")
    op.drop_table("dataset_space")
    op.drop_index(op.f("ix_conversation_message_id"), table_name="conversation_message")
    op.drop_table("conversation_message")
    op.drop_table("user_space")
    op.drop_index(op.f("ix_user_conversation_id"), table_name="user_conversation")
    op.drop_table("user_conversation")
    op.drop_index(op.f("ix_dataset_id"), table_name="dataset")
    op.drop_table("dataset")
    op.drop_index(op.f("ix_workspace_id"), table_name="workspace")
    op.drop_table("workspace")
    op.drop_index(
        op.f("ix_organization_membership_id"), table_name="organization_membership"
    )
    op.drop_table("organization_membership")
    op.drop_index(op.f("ix_connector_id"), table_name="connector")
    op.drop_table("connector")
    op.drop_index(op.f("ix_api_keys_id"), table_name="api_keys")
    op.drop_table("api_keys")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_organization_name"), table_name="organization")
    op.drop_index(op.f("ix_organization_id"), table_name="organization")
    op.drop_table("organization")
    # ### end Alembic commands ###
