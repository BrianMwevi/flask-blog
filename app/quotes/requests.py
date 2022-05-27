import urllib.request
import json


def get_quotes():
    """Send request to quotes.stormsconsultuncy api and returns a random quote as json response"""
    api_url = "http://quotes.stormconsultancy.co.uk/random.json"
    with urllib.request.urlopen(api_url) as data:
        return json.loads(data.read())
