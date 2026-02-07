from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Mock Data
MOCK_FLIGHTS = {
    "AA123": {
        "flight_number": "AA123",
        "start_time": "08:00 AM",
        "end_time": "11:30 AM",
        "start_location": "New York (JFK)",
        "end_location": "Los Angeles (LAX)",
        "time_zone_start": "EST",
        "time_zone_end": "PST"
    },
    "DL456": {
        "flight_number": "DL456",
        "start_time": "02:00 PM",
        "end_time": "05:00 PM",
        "start_location": "Atlanta (ATL)",
        "end_location": "Chicago (ORD)",
        "time_zone_start": "EST",
        "time_zone_end": "CST"
    },
    "UA789": {
        "flight_number": "UA789",
        "start_time": "06:00 AM",
        "end_time": "09:00 AM",
        "start_location": "San Francisco (SFO)",
        "end_location": "Denver (DEN)",
        "time_zone_start": "PST",
        "time_zone_end": "MST"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/flight/<flight_number>', methods=['GET'])
def get_flight(flight_number):
    flight = MOCK_FLIGHTS.get(flight_number.upper())
    if flight:
        return jsonify(flight)
    else:
        return jsonify({"error": "Flight not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
