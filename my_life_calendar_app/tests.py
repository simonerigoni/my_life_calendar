import datetime

from django.http import HttpResponse
from django.test import Client


def test_calendar_get_renders():
    response = Client().get("/")
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200


def test_calendar_post_builds_table_for_a_short_life():
    birth = datetime.date(2000, 6, 15)
    response = Client().post(
        "/",
        {
            "submit-button": "1",
            "birth-date": birth.isoformat(),
            "life-expectancy": "1",
        },
    )
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    content = response.content.decode()
    assert "lightpink" in content or "lightgreen" in content
    assert "2000" in content
    assert "2001" in content
