#!/usr/bin/python3
"""a script that lists all State objects from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3], pool_pre_ping=True))
    session = Session(engine)
    s = session.query(State).order_by(State.id).all()
    for i in s:
        if 'a' in i.name:
            print(f"{i.id}: {i.name}")
    session.close()
