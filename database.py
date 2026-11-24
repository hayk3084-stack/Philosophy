from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///try.db")
SessionLocal = sessionmaker(bind=engine)


@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()

