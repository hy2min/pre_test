import pytest
from rest_framework.test import APIClient
# from django.contrib.auth import get_user_model
from accounts.models import User

@pytest.mark.django_db
def test_account_create_api_view():
    client = APIClient()
    payload = {
        "username": "user5",
        "password": "password1234!",
        "nickname": "user5"
    }
    response = client.post('/api/accounts/signup/', payload, format='json')
    print(response.data)
    assert response.status_code == 201
    assert response.data['username'] == "user5"
    assert response.data['nickname'] == "user5"
    assert response.data['roles'] == [{"role": "USER"}]

@pytest.mark.django_db
def test_custom_token_obtain_pair_view():
    client = APIClient()
    user = User.objects.create_user(username="user1", password="password1234")
    
    payload = {
        "username": "user1",
        "password": "password1234"
    }
    response = client.post('/api/accounts/login/', payload, format='json')
    
    assert response.status_code == 200
    assert 'token' in response.data
