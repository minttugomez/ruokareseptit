import db

def get_all_recipes():
    sql = "SELECT * FROM recipes"
    return db.query(sql)

def add_new_recipe(user_id, title, description, ingredients, instructions):
    sql = """
        INSERT INTO recipes (user_id, title, description, ingredients, instructions)
        VALUES (?, ?, ?, ?, ?)
    """
    db.execute(sql, [user_id, title, description, ingredients, instructions])
