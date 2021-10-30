import secrets
from datetime import datetime, timezone, timedelta

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship, Query

from alar_studios_test.config import SESSION_DURATION
from alar_studios_test.db.connection import engine, db_session


class Base(declarative_base(bind=engine)):
    __abstract__ = True

    query: Query = db_session.query_property()

    def __repr__(self):
        return f'<{self.__class__.__name__} {" ".join([f"{c.name}={getattr(self, c.name)}" for c in self.__table__.c])}>'


class User(Base):
    __tablename__ = 'users'

    """
    User model
    
    name: str                   Unique username as primary key
    password_hash: str          PBKDF2
    permissions: Permissions    Link to Permissions object
    updated: datetime           Last update time
    """

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(32), unique=True)
    password_hash: str = Column(String(102), nullable=False)
    permissions: 'Permissions' = relationship('Permissions', back_populates='user', uselist=False)
    updated: datetime = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(tz=timezone(timedelta(hours=3))),
        onupdate=lambda: datetime.now(tz=timezone(timedelta(hours=3)))
    )
    auth_token = Column(String(64))
    token_expire = Column(DateTime())

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'permissions': {
                'read': self.permissions.read,
                'create': self.permissions.create,
                'update': self.permissions.update,
                'delete': self.permissions.delete
            },
            'updated': self.updated
        }

    def create_token(self):
        # TODO: JWT auth
        self.auth_token = secrets.token_hex()
        print(f'{self.auth_token=}')
        self.renew_token()

    def renew_token(self):
        self.token_expire = datetime.now() + timedelta(seconds=SESSION_DURATION)
        print(f'{self.token_expire=}')
        db_session.commit()

    def remove_token(self):
        self.auth_token = None
        self.token_expire = None
        db_session.commit()

    @staticmethod
    def check_token(token: str):
        # TODO: JWT auth
        user: User = User.query.filter_by(auth_token=token).one_or_none()
        if user is None:
            return None
        if user.token_expire > datetime.now():
            user.renew_token()
            return user
        else:
            user.remove_token()
            return None



class Permissions(Base):
    __tablename__ = 'permissions'

    """
    Permissions model

    username: str   User name, ForeignKey to check for User existence
    read: bool      Permission for reading
    create: bool    Permission for creating
    update: bool    Permission for updating
    delete: bool    Permission for deleting
    """

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user: User = relationship(User, back_populates='permissions')
    read = Column(Boolean, default=True, nullable=False)
    create = Column(Boolean, default=False, nullable=False)
    update = Column(Boolean, default=False, nullable=False)
    delete = Column(Boolean, default=False, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all()
