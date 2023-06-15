import sqlite3

conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
    INSERT INTO login(login_email,login_password) VALUES (?,?)
""",
    ["admin", "admin"],
)

conn.commit()
