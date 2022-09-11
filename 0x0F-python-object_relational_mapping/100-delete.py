#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker

import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter(State.id == 1).first()
    session.delete(update_state)

    session.commit()


if __name__ == "__main__":
    main()
