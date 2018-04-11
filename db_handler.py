import psycopg2


def get_artist_details(artist_name):
    print("entered")
    conn = psycopg2.connect(database="songspedia", user="saumya",
                            password="password@123", host="127.0.0.1")

    cur = conn.cursor()

    query = '''WITH ARTISTID AS (SELECT ID FROM ARTISTS WHERE NAME='Mikey Dread') SELECT RELEASES.NAME, SONGS.TITLE FROM RELEASES INNER JOIN songs ON RELEASES.ID = SONGS.RELEASE_ID WHERE RELEASES.ARTIST_ID IN (SELECT ID FROM ARTISTID);'''
    print(query)
    cur.execute(query)


    # cur.execute(query)
    print("till here")
    rows = cur.fetchall()
    print(cur.rowcount)
    print(rows)
    for i in rows:
        print("release: ", i[0], "                 ", "song: ", i[1])
    return rows
