from django.test import RequestFactory

from hello_world_app.views import hello_world


def test_hello_world_view_renders():
    response = hello_world(RequestFactory().get("/hello_world/"))
    assert response.status_code == 200
