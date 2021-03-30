
import sqlite3
import json

#DEALS WITH THE FAMILY SYSTEM

class FamilyDB:

    def __init__(self):
        pass

    def create_connection(self):
        db_file = 'profiles.db'
        conn = sqlite3.connect(db_file)
        return conn

    def check_married(self, guildid, user):
        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")

        if c.fetchone()[3] == 'None':
            self.close_connection(conn)
            return False
        else:
            self.close_connection(conn)
            return True

    def marry(self, guildid, user, target):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")

        if not self.check_married(guildid, user):
            c.execute(f"UPDATE profiles SET marriage = {target} WHERE id = {user} and guildid = {guildid}")

            c.execute(f"UPDATE profiles SET marriage = {user} WHERE id = {target} and guildid = {guildid}")

            self.close_connection(conn)

            return False
        else:

            self.close_connection(conn)

            return True

    def divorce(self, guildid, user):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")

        if not self.check_married:
            self.close_connection(conn)

            return False
        else:
            c.execute(f"SELECT * FROM profiles WHERE guildid = '{guildid}' AND marriage = '{user}'")

            divorce_id = c.fetchone()[1]

            c.execute(f"UPDATE profiles SET marriage = 'None' WHERE id = {user} and guildid = {guildid}")

            c.execute(f"UPDATE profiles SET marriage = 'None' WHERE id = {divorce_id} and guildid = {guildid}")

            self.close_connection(conn)

            return True

    def check_family(self, guildid, user):

        conn = self.create_connection()
        c = conn.cursor()

        if self.check_married(guildid, user):
            c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")

            partner_id = c.fetchone()[3]

            self.close_connection(conn)

            return partner_id
        else:
            return 'None'
            


    def close_connection(self, conn):

        conn.commit()

        conn.close()