import sys
import os
import re
sys.path.insert(0, os.path.abspath('./Cinema'))
from queries import create_db_queries
from settings import sql_creation_settings
from user_interface import user
from user_interface import interface
import sqlite3


def main():
    conn = sqlite3.connect(sql_creation_settings.DATABASE_NAME)
    c = conn.cursor()
    c.execute(create_db_queries.DROP_MOVIES_TABLE)
    c.execute(create_db_queries.CREATE_MOVIES_TABLE)
    c.execute(create_db_queries.DROP_PROJECTIONS_TABLE)
    c.execute(create_db_queries.CREATE_PROJECTIONS_TABLE)
    c.execute(create_db_queries.DROP_USERS_TABLE)
    c.execute(create_db_queries.CREATE_USERS_TABLE)
    c.execute(create_db_queries.DROP_RESERVATIONS_TABLE)
    c.execute(create_db_queries.CREATE_RESERVATIONS_TABLE)
    for movie in create_db_queries.INITIAL_MOVIES:
        c.execute(create_db_queries.CREATE_INITIAL_MOVEIS, movie)
    for projection in create_db_queries.INITIAL_PROJECTIONS:
        c.execute(create_db_queries.CREATE_INITIAL_PROJECTIONS, projection)
    conn.commit()
    conn.close()

    inf = interface.Interface()
    # inf.show_movies()
    # inf.show_movie_projections(1, '2014-04-01')
    # inf.make_reservation()
    # inf.logout()
    # inf.make_reservation()


if __name__ == "__main__":
    main()