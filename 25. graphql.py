import requests
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from graphqlclient import GraphQLClient
import json

URL = "add_your_hygraph_url_here"
TOKEN = "add_your_hygraph_token_here"
QUERY = '''
  query getUsers {
  products {
    name
    price
    image {
      url
      fileName
    }
  }
}
'''

def fetch_data_with_requests():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(URL, json={'query': QUERY}, headers=headers)
    return response.json()

def fetch_data_with_gql():  
    transport = AIOHTTPTransport(url=URL, headers={"Authorization": f"Bearer {TOKEN}"})
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql(QUERY)
    result = client.execute(query)
    return result

def fetch_data_with_graphqlclient():
    client = GraphQLClient(URL)
    client.inject_token(TOKEN)
    result = json.loads(client.execute(QUERY))
    return result