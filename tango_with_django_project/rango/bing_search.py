import json
import urllib

def read_bing_key():
    bing_api_key = None

    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise BlockingIOError('bing.key file not found')
    return bing_api_key

def run_query(search_terms):

    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError("Bing Key Not Found")

    root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    service = 'Web'
