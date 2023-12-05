import mock
from fastapi import status


@mock.patch("main.load_builds")
@mock.patch("main.load_tasks")
def test_get_tasks(mocked_load_tasks, mocked_load_builds, client):
    mocked_load_builds.return_value = {
        "test_1": ["1", "0"]
    }
    mocked_load_tasks.return_value = {
        "0": ["5", "4"],
        "1": ["3", "4"],
        "2": ["5"],
        "3": ["2"],
        "4": [],
        "5": [],
    }
    with client:
        assert mocked_load_builds.called
        assert mocked_load_tasks.called

        response = client.post("/api/v1/builds/tasks/", json={
            "build": "build_doesnt_exist"
        })
        assert response.status_code == status.HTTP_404_NOT_FOUND

        response = client.post("/api/v1/builds/tasks/", json={
            "build": "test_1"
        })
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ["0", "1"]

        response = client.post("/api/v1/builds/tasks/", json={
            "build": "test_1",
            "full": True
        })
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ["5", "4", "0", "2", "3", "1"]
