from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
DATABASE_URL = "sqlite+aiosqlite:///db.sqlite"


sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL,
    session_dependency_key="session",
    before_send_handler="autocommit",
    create_all=True
)