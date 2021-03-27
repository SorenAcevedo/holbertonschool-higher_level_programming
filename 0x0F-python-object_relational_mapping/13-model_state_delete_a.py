#!/usr/bin/python3
"""
This module use sqlalchemy to print only
the first object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://' +
                       '{}:{}@localhost/{}'.format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(engine)
session = Session()

if __name__ == "__main__":
    delete_state = session.query(State).filter(State.name.contains('a'))
    for del_st in delete_state:
        session.delete(del_st)
    session.commit()
