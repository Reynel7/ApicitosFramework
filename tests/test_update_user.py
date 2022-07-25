import os
import requests
from assertpy.assertpy import assert_that
from pprint import pprint
from dotenv import load_dotenv
from crud_users import CrudUser

load_dotenv()
URL = os.getenv('BASE_URL')
TOKEN = os.getenv('ACCESS_TOKEN')


def test_update_posts():

    crud_users = CrudUser()
    response = crud_users.update_user(URL, TOKEN, 'IVAN', 'Ivancito@gmail.com', 'aaa123', '3')
    pprint(response.as_dict)
    pprint(response.text)
    pprint(response.status_code)
    pprint(response.headers)
    assert_that(response.status_code).is_equal_to(200)
