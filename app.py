from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# 🔴 DATABASE CONNECTION (EDIT PASSWORD)
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your_password",   
        database="energy_db"
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully")

except Exception as e:
    print("❌ Database connection failed:", e)


# 🟢 HOME ROUTE (for browser testing)
@app.route('/')
def home():
    return "🚀 Server is running successfully!"


# 🔵 INGEST ROUTE (MAIN API FOR DATA)
@app.route('/ingest', methods=['POST'])
def ingest():
    try:
        data = request.json

        # 🧠 Extract values safely
        device_id = data.get('device_id')
        voltage = data.get('voltage')
        current = data.get('current')
        power = data.get('power')
        energy = data.get('energy')
        frequency = data.get('frequency')
        power_factor = data.get('power_factor')

        # 🛑 Check if required data exists
        if device_id is None:
            return jsonify({"error": "device_id is required"}), 400

        query = """
        INSERT INTO energy_readings 
        (device_id, voltage, current, power, energy, frequency, power_factor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            device_id,
            voltage,
            current,
            power,
            energy,
            frequency,
            power_factor
        ))

        conn.commit()

        return jsonify({"message": "✅ Data Stored Successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🟡 OPTIONAL: GET DATA (for testing in browser)
@app.route('/data', methods=['GET'])
def get_data():
    try:
        cursor.execute("SELECT * FROM energy_readings ORDER BY timestamp DESC LIMIT 10")
        rows = cursor.fetchall()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🚀 RUN SERVER
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)