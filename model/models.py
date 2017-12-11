# pyramidapp/models.py
import datetime
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension())) #, autocommit=True))
Base = declarative_base()

class LogModel(Base):
    __tablename__ = 'urlaccess'
    id = Column(Integer, primary_key=True)
    idsession = Column(Text)
    endpoint = Column(Text)
    datahora = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, idsession, endpoint):
        self.idsession = idsession
        self.endpoint = endpoint