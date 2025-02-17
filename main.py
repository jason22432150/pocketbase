from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
# import requests

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'  # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m'  # called to return to standard terminal text color


# client = PocketBase('https://pocketbase.miku-izayoi.uk')


def get_token(client):
  # authenticate as regular user
  user_data = client.collection("users").auth_with_password(
    "user@example.com", "4ZQ50ZFoABO-nNR")
  # check if user token is valid
  # user_data.is_valid
  return user_data.token


def license_verify(client, license):
  token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJwYmNfMzE0MjYzNTgyMyIsImV4cCI6MTczOTg2NjM4MiwiaWQiOiI3MDc0OWJsMDBvaXk3MjgiLCJyZWZyZXNoYWJsZSI6ZmFsc2UsInR5cGUiOiJhdXRoIn0.HaUAiuz3dyPrC0N0zSuGUvmsaK1Vv3CxnZ-C79x83dI"
  client.auth_store.save(token, None)
  license_verify_res = client.collection("License").get_list(1, 30, {
    filter: f'License = {license}'})  # Changed to get_first_list_item and using filter parameter
  return dir(license_verify_res.items.index)


# def HTTP_request():
#   url = 'https://pocketbase.miku-izayoi.uk/api/collections/users/auth-with-password'
#   headers = {
#     'Content-Type': 'application/json',
#     'Authorization': '',
#   }
#   data = {'identity': 'user@example.com', 'password': '4ZQ50ZFoABO-nNR'}
#   try:
#     response = requests.post(url, headers=headers, data=data)
#     response.raise_for_status()
#     data = response.json()
#     print(data)
#   except requests.exceptions.RequestException as error:
#     print(f"Error: {error}")


def authenticate_admin(client):
  # authenticate as admin
  admin_data = client.admins.auth_with_password("test@example.com", "0123456789")
  return admin_data


def create_record_with_file_upload(client):
  # create record and upload file to image field
  result = client.collection("example").create(
    {
      "status": "true",
      "image": FileUpload(("image.png", open("image.png", "rb"))),
    })
  return result
  
  # admin_data.is_valid


def list_and_filter_example_records(client):
  # list and filter "example" collection records
  result = client.collection("example").get_list(
    1, 20, {"filter": 'status = true && created > "2022-08-01 10:00:00"'})
  return result


def create_example_record(client):
  # create record and upload file to image field
  result = client.collection("example").create(
    {
      "status": "true",
      "image": FileUpload(("image.png", open("image.png", "rb"))),
    })
  return result
  
  # and much more...


if __name__ == "__main__":
  client = PocketBase('https://pocketbase.miku-izayoi.uk')
  # token = get_token(client)
  # print(res)
  print(license_verify(client, "I3848-7D07X-0881B-XGAC1"))
  print(license_verify(client, "I3848-7D07X-0881B-XGAC21"))
