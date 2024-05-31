from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '123456'
DB_NAME = 'bincom_test'

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

@app.route('/')
def index():
    return jsonify({'data':"Welcome, Home Page"})

@app.route('/states', methods=['GET'])
def get_users():
    try:
        connection = db.engine.connect()
        print("connected succesfully")
        # Execute the SQL query
        query= text("SELECT * FROM states")
        result = connection.execute(query)

        # Fetch all results
        states = [row for row in result]
        print(states)
        connection.close()
        return jsonify("done"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/polling-unit-results/<unit>', methods=['GET'])
def get_polling_results(unit):
    try:
        connection = db.engine.connect()
        print("connected succesfully")
        # Execute the SQL query
        query= ('''select party_abbreviation, party_score from announced_pu_results where polling_unit_uniqueid={unit} order by party_score desc'''.format(unit=unit))
        result = connection.execute(text(query))

        # Fetch all results
        result_list = [{'party_abbreviation': row[0], 'party_score': row[1]} for row in result]
        print(result_list)
        connection.close()
        return jsonify(result_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/local-government-results/<unit>', methods=['GET'])
def get_local_government_results(unit):
    try:
        connection = db.engine.connect()
        print("connected succesfully")
        # Execute the SQL query
        query= ('''select party_abbreviation, party_score
from announced_lga_results
where lga_name = {unit}
order by party_score desc'''.format(unit=unit))
        result = connection.execute(text(query))

        # Fetch all results
        result_list = [{'party_abbreviation': row[0], 'party_score': row[1]} for row in result]
        print(result_list)
        connection.close()
        return jsonify(result_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    


if __name__ == '__main__':
    app.run(debug=True)