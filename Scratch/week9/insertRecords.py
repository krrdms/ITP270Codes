import sqlite3
from sqlite3 import Error


def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def createProject(conn, project):
    with open("insertProjects.txt") as cpFile:
        insertProjectSQL = cpFile.read()
    cur = conn.cursor()
    cur.execute(insertProjectSQL, project)
    conn.commit()
    return cur.lastrowid


def createTask(conn, task):
    insertTskSQL = None
    with open("insertTasks.txt") as ctFile:
        insertTskSQL = ctFile.read()
    cur = conn.cursor()
    cur.execute(insertTskSQL, task)
    conn.commit()
    return cur.lastrowid


def main():
    database = "create.db"
    conn = createConnection(database)
    with conn:
        project = (1, 'Class Project', 'Final Exam Course Project Assignment',
                   'Write code that does x, y, and z.');
        projectID = createProject(conn, project)
        task_1 = (1, 'Analyze the requirements of the app',
                  1, '2021-11-01', '2021-11-02', projectID)
        task_2 = (2, 'Confirm with user about the top requirements',
                  1, '2021-11-03', '2015-11-05', projectID)
        taskIDs = (createTask(conn, task_1),
                   createTask(conn, task_2))
        print("tasks: ", taskIDs)


if __name__ == '__main__':
    main()
