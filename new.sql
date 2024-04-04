IMPORT mysql.connevtor

config = {
    'user': 'root',
    'password': 'm14s7d5@MySQL',
    'host': 'localhost'
}
db = mysql.connrctor.connect(**config)
CURSOR = db.CURSOR()
