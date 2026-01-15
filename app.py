from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Fordon app is running"})

@app.route("/start")
def start_vehicle_counter():
    subprocess.Popen(["python", "vehicle.py"])
    return jsonify({"message": "Vehicle counter started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
