import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def select_project(conn, project_priority=1, project_status='done'):
    selected_projects = []
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM Tasks
            WHERE priority = ? AND status = ? """, [project_priority, project_status])
    columns = [description[0] for description in cursor.description]
    result = cursor.fetchall()
    print(columns)


    for row in result:
        selected_projects.append(row['project'])
        print('Id:        ', row['id'])
        print('Priority:  ', row['priority'])
        print('Details:   ', row['details'])
        print('Status:    ', row['status'])
        print('Completed: ', row['completed'])
        print('Deadline:  ', row['deadline'])
        print('Project:   ', row['project'])
        print('\n')

    conn.close()
    print(selected_projects)


def main():
    database = "sqlite.db"
    conn = create_connection(database)
    select_project(conn)


if __name__ == '__main__':
    main()
