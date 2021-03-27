#!/usr/bin/python3
"""
This module use sqlalchemy to print only
the first object from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://' +
                           '{}:{}@localhost/{}'.format(sys.argv[1],
                                                       "soren",
                                                       sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    sts_cts = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)
    for s, c in sts_cts:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
