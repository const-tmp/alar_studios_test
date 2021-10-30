from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.scoping import ScopedSession

from alar_studios_test.config import DB_URL

engine = create_engine(DB_URL, echo=False)

db_session: ScopedSession = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
