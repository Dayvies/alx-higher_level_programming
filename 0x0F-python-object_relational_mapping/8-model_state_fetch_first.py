#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)


def main():
    """main function for database query"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()
    if not first:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))


if __name__ == "__main__":
    main()
