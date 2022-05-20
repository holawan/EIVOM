import requests

url = "http://127.0.0.1:8000/accounts/profile_create/1"

payload={'refresh':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzY3MTkwNiwiaWF0IjoxNjUzMDY3MTA2LCJqdGkiOiJlNTI1YzBjMWY5MTU0ZmRmODAzYjkwZDRlZWJiODA1MCIsInVzZXJfaWQiOjF9.42Vcg-0Nd4YPV01zn7DmfjX_FBqkbOJNkNhe8N2N5XU'}
files=[

]
headers = {
  'X-CSRFToken': 'gFSIaDnJL28XuGI23eZediGj0ifXl1wzk696e1c9FLhzHAOV0SH51W3FiOni7hsP',
  'Cookie': 'csrftoken=gFSIaDnJL28XuGI23eZediGj0ifXl1wzk696e1c9FLhzHAOV0SH51W3FiOni7hsP'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
