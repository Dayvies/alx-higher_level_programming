#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == sys.argv[4]).first()
    if not instance:
        print("Not found")
    else:
        print(instance.id)


if __name__ == "__main__":
    main()
