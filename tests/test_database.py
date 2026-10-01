from db.database import setup_database, get_connection


def test_users_table():
    setup_database()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    connection.close()

    assert count == 3