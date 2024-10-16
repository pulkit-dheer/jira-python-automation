from flask import Flask
import json
from requests.auth import HTTPBasicAuth
import requests

app = Flask(__name__)


@app.route("/createJIRA", methods=['POST'])
def hello():

    url = "https://example.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("<email>", "<token>")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "summary": "Website is not loading to due a bug.",
            "issuetype": {
                "id": "10003"  
            },
            "project": {
                "key": "SCRUM"  
            },
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            }
        }
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))



app.run('0.0.0.0', port=3000)

