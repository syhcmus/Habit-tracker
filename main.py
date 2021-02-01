import requests
from datetime import datetime

USERNAME = 'syhcmus'
TOKEN = 'syhcmus2000'
GRAPH_ID = 'graph2'

pixel_endpoint = 'https://pixe.la/v1/users'
pixel_params = {
    'token': 'syhcmus2000',
    'username': 'syhcmus',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixel_endpoint, json=pixel_params)
# print(response)

graph_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs'
graph_params = {
    'id': 'graph2',
    'name': 'Coding Graph',
    'unit': 'hour',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response)

today = datetime.now()


pixel_creation_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_creation_data = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input('how many hours have you spent in coding today? '),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_data, headers=headers)
print(response)

print(f'Browser: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID} to check out !!!')
