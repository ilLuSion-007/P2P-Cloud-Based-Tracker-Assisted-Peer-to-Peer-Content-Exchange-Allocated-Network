import MySQLdb as mysql

class Database:
    'Class for database connection to mysql'
    db = None

    @staticmethod
    def getCursor(server = '3.212.78.155', port=3306, user ='root', password ='peer2peer', database = 'peer'):
        if Database.db is None:
            Database.db = mysql.connect("3.212.78.155", "root", "peer2peer", "peer")
        return Database.db.cursor()

    @staticmethod
    def commit():
        Database.db.commit()

    