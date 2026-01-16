from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Fordon app is running"})

@app.route("/start")
def start_vehicle_counter():
    # Start vehicle.py in background
    subprocess.Popen(["python", "vehicle.py"])
    return jsonify({"message": "Vehicle counter started"})

@app.route("/count")
def get_vehicle_count():
    # Read count from file written by vehicle.py
    if os.path.exists("vehicle_count.txt"):
        with open("vehicle_count.txt", "r") as f:
            count = f.read().strip()
    else:
        count = "0"

    return jsonify({"vehicle_count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
