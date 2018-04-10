#!usr/bin/env python3
from flask import Flask, request
import db_handler


app = Flask(__name__)


@app.route('/artists', methods=['GET'])
def upload():
    artist_name = request.args.get('artist')
    db_handler.get_artist_details(artist_name)
    print(artist_name)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)

# select artists.name, count(artists.name) from releases inner join artists on artists.id = releases.artist_id group by artists.name having count(artists.name)>1;
# with names as (select name from artists group by name having count(name)>1) select id, name from artists where name in (select name from names);
# select releases.name, songs.title from releases inner join songs on releases.id = songs.release_id where releases.artist_id='AR78ZID1187B9B31ED';
# with artistid as (select id from artists where name='Mikey Dread') select releases.name, songs.title from releases inner join songs on releases.id = songs.release_id where releases.artist_id in (select id from artistid);
