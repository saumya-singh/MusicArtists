import re
import csv
import psycopg2


conn = psycopg2.connect(database="songspedia", user="saumya",
                        password="password@123", host="127.0.0.1")
conn.autocommit = True
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS ARTISTS
      (POPULARITY    TEXT       NOT NULL,
      ID CHAR(50) PRIMARY KEY   NOT NULL,
      NAME           TEXT       NOT NULL,
      LATITUDE       TEXT       NOT NULL,
      LONGITUDE      TEXT       NOT NULL);''')
print("Table1 created successfully")


cur.execute('''CREATE TABLE IF NOT EXISTS RELEASES
      (ID CHAR(50) PRIMARY KEY     NOT NULL,
      ARTIST_ID CHAR(50)  REFERENCES ARTISTS(ID),
      NAME           TEXT          NOT NULL);''')
print("Table2 created successfully")


cur.execute('''CREATE TABLE IF NOT EXISTS SONGS
     (ID CHAR(50) PRIMARY KEY  NOT NULL,
     TEMPO        TEXT         NOT NULL,
     TERMS        TEXT     NOT NULL,
     TITLE        TEXT     NOT NULL,
     RELEASE_ID   CHAR(50)  REFERENCES RELEASES(ID),
     YEAR         TEXT);''')
print("Table3 created successfully")



def clean_code(row):
    regex = re.compile('[^-a-zA-Z0-9_.!/() ]')
    clean_data = []
    for each_detail in row:
        clean_data.append(regex.sub('', each_detail))
    return clean_data



def data_entry(for_table):
    spamReader = csv.reader(open('music.csv'), delimiter='\n')
    first_line = next(spamReader)
    for row in spamReader:
        raw_details = row[0].split(",")
        details = clean_code(raw_details)

        if for_table == "artists":
            query = "INSERT INTO ARTISTS (ID,NAME,POPULARITY,LATITUDE,LONGITUDE) \
                  VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')".format(
                  details[1], details[2], details[0], details[3], details[4])

        if for_table == "releases":
            query = "INSERT INTO RELEASES (ID,NAME,ARTIST_ID) \
                  VALUES (\'{0}\', \'{1}\', \'{2}\')".format(
                  details[5], details[6], details[1])

        if for_table == "songs":
            query = "INSERT INTO SONGS (ID,TITLE,TEMPO,TERMS,RELEASE_ID,YEAR) \
                  VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\')".format(details[7], details[10], details[8], details[9], details[5], details[11])

        try:
            cur.execute(query)
        except Exception as e:
            print(for_table)
            print(e)


data_entry("artists")
data_entry("releases")
data_entry("songs")


conn.commit()
conn.close()
