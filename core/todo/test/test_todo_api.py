import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User

@pytest.fixture
def api_client():
    client=APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email='mehrab@mohamdi.com', password='a/@1234567')
    return user

@pytest.mark.django_db
class TestTodoApi:

    def test_get_todo_200_status_response(self,api_client):
        url = reverse('todo:api-v1:todo-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_todo_response_201_status(self,common_user,api_client):
        url = reverse('todo:api-v1:todo-list')
        data=({
            'title':'test',
            'text':'detail(hi mehrab)',
            'complete':True,
        })
        user= common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201