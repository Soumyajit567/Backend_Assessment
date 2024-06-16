# from sqlalchemy import Column, Integer, String, ForeignKey
# from .db import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     mobile_no = Column(String, index=True)
#     email = Column(String, index=True)
#     hashed_password = Column(String)

# class Discussion(Base):
#     __tablename__ = "discussions"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     user_id = Column(Integer, ForeignKey("users.id"))

# from sqlalchemy import Column, Integer, String, ForeignKey
# from .db import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     mobile_no = Column(String, index=True)
#     email = Column(String, index=True)
#     hashed_password = Column(String)

# class Discussion(Base):
#     __tablename__ = "discussions"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     file_path = Column(String, nullable=True)  

from sqlalchemy import Column, Integer, String, ForeignKey
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile_no = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)

class Discussion(Base):
    __tablename__ = "discussions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_path = Column(String, nullable=True)
