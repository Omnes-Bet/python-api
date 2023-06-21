from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/bonusActivation", methods=['POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url_to_post = 'https://sb2bonus-integration-altenar2-stage.biahosted.com/api/Bonus/CreateBonusByDeposit/json'
            
            proxyDict = { 
                  "http"  : os.environ['QUOTAGUARDSTATIC_URL'], 
                  "https" : os.environ['QUOTAGUARDSTATIC_URL']
            }
            
            response = requests.post(url_to_post, json=data, proxies=proxyDict)
            return jsonify({"status": "success", "response": response.json()}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__=='__main__':
    app.run(port=5000, debug=True)
