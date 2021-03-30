
import sqlite3
import discord

class ProfileDB:

    def __init__(self):

        pass

    def create_connection(self):
        db_file = 'profiles.db'
        conn = sqlite3.connect(db_file)
        return conn

    def open_account(self, user):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT id FROM profiles WHERE id = '{str(user)}'")
    
        if c.fetchone() == None:
            c.execute(f"""INSERT INTO profiles VALUES ('{str(user)}', '500')""")

        self.close_connection(conn)


    def get_bank_data(self, user):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"SELECT * FROM profiles WHERE id = '{str(user)}'")

        return c.fetchone()[1]

    def change_money(self, user, delta_money):

        conn = self.create_connection()

        c = conn.cursor()

        c.execute(f"UPDATE profiles SET money = money + {delta_money} WHERE id = {user}")

        self.close_connection(conn)

        return


    def close_connection(self, conn):

        conn.commit()

        conn.close()