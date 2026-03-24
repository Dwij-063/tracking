from flask import Flask, request, jsonify

app = Flask(__name__)

# Store latest location
robot_location = {"lat": 0, "lon": 0}

@app.route('/gps')
def gps():
    global robot_location

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    robot_location["lat"] = lat
    robot_location["lon"] = lon

    print("Updated Location:", robot_location)

    return "OK"

@app.route('/location')
def location():
    return jsonify(robot_location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)