import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def allTasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def taskByPriority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    database = "create.db"
    conn = create_connection(database)
    with conn:
        print("Tasks by priority:")
        taskByPriority(conn, 1)

        print("2. Query all tasks")
        allTasks(conn)


if __name__ == '__main__':
    main()
