from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'Whatme017!?'
app.config['MYSQL_DB'] = 'favsongs'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Root route
@app.route("/")
def home():
    return "<p>FAVORITE SONGS!</p>"

# Data retrieval
def fetch_data(query):
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

# GET METHOD FOR ALL CONTENT
@app.route("/favsongs", methods=['GET'])
def get_songs():
    try:
        data = fetch_data("SELECT * FROM poppunksongs")
        fmt = request.args.get('format')
        response = make_response(jsonify(data))
        if fmt.lower() == 'xml':
            response.mimetype = 'application/xml'
        else:
            response.mimetype = 'application/json'
        return response
    except Exception as error:
        print(error)
        return make_response(jsonify({"message": "An error occurred"}), 500)


# GET METHOD W/ PARAMETER SONG_ID
@app.route("/favsongs/<int:song>", methods=["GET"])
def get_song_by_id(song):
    try:
        data = fetch_data("""SELECT * FROM PopPunkSongs WHERE song = {}""".format(song))
        fmt = request.args.get('format')
        response = make_response(jsonify(data))
        if fmt.lower() == 'xml':
            response.mimetype = 'application/xml'
        else:
            response.mimetype = 'application/json'
        return response
    except Exception as error:
        print(error)

# POST METHOD
@app.route("/favsongs", methods=['POST'])
def add_song():
    try:
        cursor = mysql.connection.cursor()
        json_data = request.get_json(force=True)
        title = json_data["title"]
        artist = json_data["artist"]
        album = json_data["album"]
        cursor.execute("INSERT INTO poppunksongs (title, artist, album) VALUES (%s, %s, %s)", (title, artist, album))
        mysql.connection.commit()
        cursor.close()
        response = jsonify("ADDED TO THE LIST")
        response.status_code = 200
        return response
    except Exception as error:
        print(error)

# PUT METHOD MODIFY OR UPDATE
@app.route("/favsongs/<int:song>", methods=["PUT"])
def update_song_by_id(song):
    try:
        cursor = mysql.connection.cursor()
        json_data = request.get_json(force=True)
        title = json_data["title"]
        artist = json_data["artist"]
        album = json_data["album"]
        query = " UPDATE poppunksongs SET title = %s, artist = %s, album = %s WHERE song = %s "
        binded = [title, artist, album, song]
        cursor.execute(query, binded)
        mysql.connection.commit()
        response = jsonify("MODIFY SUCCESSFUL")
        response.status_code = 200
        return response
    except Exception as error:
        print(error)
        return make_response(jsonify({"message": "An error occurred", "error": str(error)}), 500)
    finally:
        cursor.close()


# DELETE METHOD
@app.route("/favsongs/<int:song>", methods=["DELETE"])
def delete_song_by_id(song):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""DELETE FROM PopPunkSongs WHERE song=%s""", (song,))
        mysql.connection.commit()
        cursor.close()
        return make_response(jsonify({"message": "DELETED SUCCESSFULLY!"}), 200)
    except Exception as error:
        print(error)

# RUN
if __name__ == "__main__":
    app.run(debug=True)
