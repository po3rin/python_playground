import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


print(sqlalchemy.__version__)
engine = create_engine('mysql+mysqlconnector://po3rin:1234567890@localhost/test_db', echo=True)

Base = declarative_base()
class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    username = Column(String)

account = Account(username="po3rin")
print(account.username)

Session = sessionmaker(bind=engine)
session = Session()
session.add(account)

session.commit()

our_users = session.query(Account).all()
for user in our_users:
    print(user.username)