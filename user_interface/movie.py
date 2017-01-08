import sys
import os
import sqlite3
sys.path.insert(0, os.path.abspath('../'))
from user_interface import projection
from settings import sql_creation_settings
from queries import manage_db_queries

class Movie:
    def __init__(self, m_id, name, rtg):
        self.init_database()
        self.id = m_id
        self.name = name
        self.rating = rtg
        self.projections = []
        self.add_projections()
        self.conn.close()

    def init_database(self):
        self.conn = sqlite3.connect(sql_creation_settings.DATABASE_NAME)
        self.c = self.conn.cursor()

    def add_projections(self):
        db_projections = self.c.execute(manage_db_queries.SHOW_PROJECTIONS, [self.id]).fetchall()
        for db_projection in db_projections:
            self.projections.append(projection.Projection(*db_projection))

    def print_projections(self):
        for projection in self.projections:
            print(projection)