from flask import Flask, jsonify, request
import sqlite3

# ##### CONSTANTS #####
DATABASE_NAME = 'plates.db'

# ##### Object initialization #####
flask_api = Flask(__name__)


# ##### Function definitions #####
def add_plate_to_db(s):
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO plates (plate) VALUES (?)", (s,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # This error occurs if the plate already exists in the database
        return False
    finally:
        conn.close()

def db_initialize():
    conn = sqlite3.connect('plates.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_registered_plates():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute("SELECT plate FROM plates")
    plates = [row[0] for row in cur.fetchall()]
    conn.close()
    return plates

def is_valid(s):
    if(len(s) < 2 or len(s) > 6):
        # The length of the plate must be between 2 and 6 characters
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        # The first two characters must be letters
        return False
    if not check_number_position(s):
        # The numbers must be at the end of the plate and cannot start with 0
        return False
    if not s.isalnum():
        # The plate must only contain letters and numbers 
        return False
    
    # Return True if all conditions are satisfied
    return True

def check_number_position(s):
    numbers_started = False

    for char in s:
        if char.isdigit():
            if char == "0" and not numbers_started:
                return False
            numbers_started = True
            continue

        if char.isalpha() and numbers_started:
            return False

    return numbers_started

# ##### Define the API endpoints #####
@flask_api.get("/")
def index():
    return jsonify({"message": "Vanity plate API is running"})


@flask_api.post("/validate")
def validate_plate():
    # Get the JSON data from the request.
    data = request.get_json(silent=True) or {}
    plate = data.get("plate", "")

    if not isinstance(plate, str):
        return jsonify({"error": "'plate' must be a string"}), 400

    return jsonify({
        "plate": plate,
        "valid": is_valid(plate)
    })

@flask_api.post("/register")
def register_plate():
    # Get the JSON data from the request.
    data = request.get_json(silent=True) or {}
    plate = data.get("plate", "")

    if not isinstance(plate, str):
        return jsonify({"error": "'plate' must be a string"}), 400

    if not is_valid(plate):
        return jsonify({
            "plate": plate,
            "inserted": False,
            "reason": "Invalid plate format"
        }), 400
    
    if not add_plate_to_db(plate):
        return jsonify({
            "plate": plate,
            "inserted": False,
            "reason": "Plate already registered"
        }), 400
    
    return jsonify({
        "plate": plate,
        "inserted": True
    })

@flask_api.get("/plates")
def list_plates():
    return jsonify({"plates": get_registered_plates()})


# ##### Main execution #####
if __name__ == "__main__":
    db_initialize()
    flask_api.run(debug=True)