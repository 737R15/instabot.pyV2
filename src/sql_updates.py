# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

def check_and_update(self):
    """ At the Program start, i does look for the sql updates """
    self.follows_db_c.execute("CREATE TABLE IF NOT EXISTS usernames (username varchar(300))")
    self.follows_db_c.execute("CREATE TABLE IF NOT EXISTS medias (media_id varchar(300))")
    medias_info = self.follows_db_c.execute("pragma table_info(medias)")
    medias_column_status = [o for o in medias_info if o[1] == "status"]
    if not medias_column_status:
        self.follows_db_c.execute("ALTER TABLE medias ADD COLUMN status integer")
    medias_info = self.follows_db_c.execute("pragma table_info(medias)")
    medias_column_status = [o for o in medias_info if o[1] == "datetime"]
    if not medias_column_status:
        self.follows_db_c.execute("ALTER TABLE medias ADD COLUMN datetime integer")
    #print(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())))

def check_already_liked(self, media_id):
    """ controls if media already liked before """
    if self.follows_db_c.execute("SELECT EXISTS(SELECT 1 FROM medias WHERE media_id='"+
                                 media_id + "' LIMIT 1)").fetchone()[0] > 0:
        return 1
    return 0

def check_already_followed(self, user_id):
    """ controls if user already followed before """
    if self.follows_db_c.execute("SELECT EXISTS(SELECT 1 FROM usernames WHERE username='"+
                                 user_id + "' LIMIT 1)").fetchone()[0] > 0:
        return 1
    return 0

def insert_media(self, media_id, status):
    """ insert media to medias """
    self.follows_db_c.execute("INSERT INTO medias (media_id, status, datetime) VALUES('"+
                              media_id +"','"+ status +"','"+ str(time.time()) +"')")

def insert_username(self, user_id):
    """ insert user_id to usernames """
    self.follows_db_c.execute("INSERT INTO usernames (username) VALUES('"+user_id+"')")
