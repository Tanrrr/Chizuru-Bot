
import sqlite3
import discord

# DEALS WITH ACCOUNT CREATION AND MONEY

class ProfileDB:

    def __init__(self):

        pass

    def create_connection(self):
        db_file = 'profiles.db'
        conn = sqlite3.connect(db_file)
        return conn

    def open_account(self, guildid, user):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT id FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")
    
        if c.fetchone() == None:
            c.execute(f"""INSERT INTO profiles VALUES ('{str(guildid)}','{str(user)}', '500', 'None','None')""")

        self.close_connection(conn)


    def get_bank_data(self, guildid, user):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}' AND guildid = '{str(guildid)}'")

        return c.fetchone()[2]

    def change_money(self, guildid, user, delta_money):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"UPDATE profiles SET money = money + {delta_money} WHERE id = {user} AND guildid = {guildid}")

        self.close_connection(conn)

        return


    def close_connection(self, conn):

        conn.commit()

        conn.close()