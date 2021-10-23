import sqlite3


def createConnection(f):
    conn = None
    try:
        conn = sqlite3.connect(f)
    except sqlite3.Error as e:
        print(e)
    return conn


def createTbl(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)


def main():
    dbFile = "create.db"

    createProjectsTblSQL = None
    createTasksTblSQL = None

    # create a database connection
    conn = createConnection(dbFile)

    # create tables
    if conn is not None:
        with open("createProjects.txt") as cpFile:
            createProjectsTblSQL = cpFile.read()
        createTbl(conn, createProjectsTblSQL)

        with open("createTasks.txt") as ctFile:
            createTasksTblSQL = ctFile.read()
        createTbl(conn, createTasksTblSQL)
    else:
        print("Error! cannot create db.")


if __name__ == '__main__':
    main()
