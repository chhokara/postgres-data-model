# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id SERIAL PRIMARY KEY, 
        start_time timestamp NOT NULL, 
        user_id int NOT NULL, 
        level varchar, 
        song_id varchar, 
        artist_id varchar, 
        session_id int NOT NULL, 
        location varchar, 
        user_agent varchar,
        FOREIGN KEY (start_time) REFERENCES time (start_time),
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (song_id) REFERENCES songs (song_id),
        FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
    )
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id int PRIMARY KEY, 
        first_name varchar, 
        last_name varchar, 
        gender varchar, 
        level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id varchar PRIMARY KEY, 
        title varchar NOT NULL, 
        artist_id varchar, 
        year int, 
        duration numeric NOT NULL
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id varchar PRIMARY KEY, 
        name varchar NOT NULL, 
        location varchar, 
        latitude double precision, 
        longitude double precision
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time timestamp PRIMARY KEY, 
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday varchar
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level) 
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE
    SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) 
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id
    FROM songs
    INNER JOIN artists ON songs.artist_id = artists.artist_id
    WHERE title = %s AND name = %s AND duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
