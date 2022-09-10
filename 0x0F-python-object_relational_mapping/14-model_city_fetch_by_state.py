#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(City, State).join(
            State, City.state_id == State.id).order_by(State.id):
        print("{}: ({}) {}".format(inst[1].name, inst[0].id, inst[0].name))


if __name__ == "__main__":
    main()
