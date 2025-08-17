import db

def get_all_recipes():
    sql = "SELECT * FROM recipes"
    db.query(sql)
