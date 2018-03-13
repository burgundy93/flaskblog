from graphqlclient import GraphQLClient
import json

access_token = "7e0118b3603a7c3a54435db7"
bearer_token = 'Bearer ' + access_token
headers = {'Authorization': bearer_token}

client = GraphQLClient("https://wip.chat/graphql")
client.inject_token(bearer_token)


result = client.execute('''

query{
  user(id: "73") {
    username
    products {
      name
      id
    }
  }
}

''')

products = json.loads(result)

for a in products['data']['user']['products']:
    name = a["name"]
    id = a['id']
    print(a)
