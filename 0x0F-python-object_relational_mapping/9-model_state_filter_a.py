#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Connecting"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).filter(State.name.like('%a%'))
    for sts in first_state:
        print("{}: {}".format(sts.id, sts.name))
    session.close()
