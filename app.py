from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/getOutboundIP", methods=['GET'])
def index():
    try:
        proxyDict = { 
            "http"  : os.environ['QUOTAGUARDSTATIC_URL'], 
            "https" : os.environ['QUOTAGUARDSTATIC_URL']
        }
        
        response = requests.get('https://api.ipify.org?format=json', proxies=proxyDict)
        return jsonify({"status": "success", "response": response.json()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=='__main__':
    app.run(port=5000, debug=True)
