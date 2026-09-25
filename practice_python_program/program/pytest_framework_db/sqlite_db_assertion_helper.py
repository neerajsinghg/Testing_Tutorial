"""
Interview Question: How do you perform SQL Database verification in Python automation frameworks?

Interview Explanation:
"I use Python's built-in `sqlite3` (or `pymysql`/`psycopg2` for MySQL/PostgreSQL).
I write a reusable DB helper class to execute SQL queries, fetch records as dictionaries (`sqlite3.Row`),
and assert database state against API or UI test inputs."
"""

import sqlite3

class DatabaseAssertionHelper:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_demo_schema()

    def _init_demo_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE users (id INT PRIMARY KEY, username TEXT, email TEXT, status TEXT);")
        cursor.execute("INSERT INTO users VALUES (101, 'neeraj', 'neeraj@test.com', 'ACTIVE');")
        self.conn.commit()

    def fetch_user_by_id(self, user_id: int) -> dict | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = DatabaseAssertionHelper()
    user = db.fetch_user_by_id(101)
    print("Fetched DB Record:", user)

    assert user["username"] == "neeraj"
    assert user["status"] == "ACTIVE"
    print("Database assertion passed successfully!")
    db.close()
