# Flask
from flask import Flask, request, jsonify

# CORS
from flask_cors import CORS

# Importing Functions
from mylogic import calculateCostOfLaptop, calculateCostOfDesktop, calculateConfig, calculateConfigLaptop
# Initialise App
app = Flask(__name__)

# For Enabling Cross Origin Requests
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API End Point [ host:port/request ]
@app.route("/getconfig", methods=['POST'])
def getConfig():    
    # Extracting The Posted JSON Data
    json = request.get_json(force=True)

    # Check If Data Is Not Missing Or In Wrong Format
    required_keys = ['givenmoney']
    if not all(key in json for key in required_keys):
        return jsonify({'errormessage': 'Bad Request', 'requeststatus': 'Failed'}), 400
    else:
        flag = calculateConfig(json['givenmoney'])
        if flag['requeststatus'] == "Success":
            return jsonify(flag), 200
        else:
            return jsonify({'errormessage': 'Error', 'requeststatus': 'Failed'}), 400
        # API End Point [ host:port/request ]


@app.route("/getconfiglaptop", methods=['POST'])
def getConfigi():
    # Extracting The Posted JSON Data
    json = request.get_json(force=True)

    # Check If Data Is Not Missing Or In Wrong Format
    required_keys = ['givenmoney']
    if not all(key in json for key in required_keys):
        return jsonify({'errormessage': 'Bad Request', 'requeststatus': 'Failed'}), 400
    else:
        flag = calculateConfigLaptop(json['givenmoney'])
        if flag['requeststatus'] == "Success":
            return jsonify(flag), 200
        else:
            return jsonify({'errormessage': 'Error', 'requeststatus': 'Failed'}), 400
        # API End Point [ host:port/request ]


@app.route("/getcostoflaptop", methods=['POST'])
def getCostOfLaptop():

    # Extracting The Posted JSON Data
    json = request.get_json(force=True)

    # Extracting The Posted JSON Data
    required_keys = ['gc', 'hdd', 'keyboard',
                     'mouse', 'processor', 'ram', 'screen']
    if not all(key in json for key in required_keys):
        return jsonify({'errormessage': 'Bad Request', 'requeststatus': 'Failed'}), 400
    else:
        flag = calculateCostOfLaptop(
            json['gc'], json['hdd'],json['keyboard'], json['mouse'], json['processor'], json['ram'], json['screen'])
        if flag['requeststatus'] == "Success":
            return jsonify(flag), 200
        else:
            return jsonify({'errormessage': 'Error', 'requeststatus': 'Failed'}), 400

        # API End Point [ host:port/request ]


@app.route("/getcostofdesktop", methods=['POST'])
def getCostOfDesktop():

    # Extracting The Posted JSON Data
    json = request.get_json(force=True)

    # Extracting The Posted JSON Data
    required_keys = ['gc', 'hdd', 'keyboard',
                     'mouse', 'processor', 'ram', 'screen']
    if not all(key in json for key in required_keys):
        return jsonify({'errormessage': 'Bad Request', 'requeststatus': 'Failed'}), 400
    else:
        flag = calculateCostOfDesktop(json['gc'], json['hdd'], json['keyboard'], json['mouse'], json['processor'], json['ram'], json['screen'])
        if flag['requeststatus'] == "Success":
            return jsonify(flag), 200
        else:
            return jsonify({'errormessage': 'Error', 'requeststatus': 'Failed'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
