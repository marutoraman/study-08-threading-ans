# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session,Session
import os
import ulid
from dotenv import load_dotenv
load_dotenv() #環境変数のロード
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

SQLALCHEMY_DATABASE_URL = os.environ["DB_PATH"]
SQLALCHEMY_DATABASE_URL += '?charset=utf8mb4'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=360,pool_size=100)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
session = scoped_session(SessionLocal)


# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close() # pylint: disable=no-member

def get_db_instance():
  return SessionLocal()

'''
def clean_db():
  metadata = MetaData()
  metadata.reflect(bind=engine)
  engine.execute("SET FOREIGN_KEY_CHECKS = 0")
  for tbl in metadata.tables:
    if tbl.find('manaus_') != 0: continue
    engine.execute("DROP TABLE " + tbl)
  engine.execute("SET FOREIGN_KEY_CHECKS = 1")
'''

def get_ulid():
  return ulid.new().str
