from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from tests.utils.task import create_random_task


def test_create_task(
    client: TestClient, db: Session
) -> None:
    data = {
        "title": "random title for test",
        "task_date": "2021-09-29",
        "start_time": "09:00:00",
        "end_time": "10:00:00",
        "duration": 3600
    }
    response = client.post(
        f"{settings.API_V1_STR}/tasks/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["task_date"] == data["task_date"]
    assert content["start_time"] == data["start_time"]
    assert content["end_time"] == data["end_time"]
    assert content["duration"] == data["duration"]
    assert "id" in content


def test_read_task(
    client: TestClient, db: Session
) -> None:
    task = create_random_task(db)
    response = client.get(
        f"{settings.API_V1_STR}/tasks/{task.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == task.title
    assert content["task_date"] == task.task_date.strftime("%Y-%m-%d")
    assert content["start_time"] == task.start_time.strftime("%H:%M:00")
    assert content["end_time"] == task.end_time.strftime("%H:%M:00")
    assert content["duration"] == task.duration
    assert content["id"] == task.id
