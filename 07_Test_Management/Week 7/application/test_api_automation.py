
import pytest
import app as app_module
from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a separate temporary database for every test.
    test_database = tmp_path / "test_pytodo_pro.db"
    monkeypatch.setattr(app_module, "DATABASE", str(test_database))

    app.config["TESTING"] = True
    app_module.init_db()

    with app.test_client() as test_client:
        yield test_client


def test_unauthenticated_user_cannot_access_tasks(client):
    response = client.get("/api/tasks")

    assert response.status_code == 401
    assert response.get_json()["error"] == "authentication required"


def test_unauthenticated_user_cannot_access_dashboard(client):
    response = client.get("/api/dashboard")

    assert response.status_code == 401
    assert response.get_json()["error"] == "authentication required"


def test_blank_title_request_without_login_is_rejected(client):
    response = client.post(
        "/api/tasks",
        json={"title": ""}
    )

    assert response.status_code == 401
    assert response.get_json()["error"] == "authentication required"


def test_registration_with_valid_details(client):
    response = client.post(
        "/api/register",
        json={
            "username": "validnewuser",
            "password": "ValidPass123!"
        }
    )

    assert response.status_code == 201


def test_api_login_with_valid_credentials(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "week6tester",
            "password": "Week6Pass123!"
        }
    )
    assert registration.status_code == 201

    # Clear the session so the login endpoint is tested independently.
    client.get("/logout")

    response = client.post(
        "/api/login",
        json={
            "username": "week6tester",
            "password": "Week6Pass123!"
        }
    )

    assert response.status_code == 200
    assert response.get_json()["username"] == "week6tester"


def test_authenticated_user_cannot_create_task_with_blank_title(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "week6tester",
            "password": "Week6Pass123!"
        }
    )
    assert registration.status_code == 201

    # The registration endpoint logs the test user in.
    response = client.post(
        "/api/tasks",
        json={"title": "   "}
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "title is required"



def test_api_login_rejects_incorrect_password(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "wrongpass_tester",
            "password": "CorrectPass123!"
        }
    )
    assert registration.status_code == 201

    # Log out so the login endpoint is tested independently.
    client.get("/logout")

    response = client.post(
        "/api/login",
        json={
            "username": "wrongpass_tester",
            "password": "WrongPassword123"
        }
    )

    assert response.status_code == 401
    assert response.get_json()["error"] == "invalid credentials"


def test_authenticated_user_can_create_task(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "taskcreator",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    response = client.post(
        "/api/tasks",
        json={
            "title": "Week 6 automated task",
            "description": "Temporary task created by pytest"
        }
    )

    assert response.status_code == 201

    task = response.get_json()
    assert task["title"] == "Week 6 automated task"
    assert "id" in task
    assert "urgency" in task


def test_authenticated_user_can_update_task(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "taskupdater",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    # Create a task to update.
    creation = client.post(
        "/api/tasks",
        json={
            "title": "Original task title",
            "description": "Task created for update testing"
        }
    )
    assert creation.status_code == 201

    task_id = creation.get_json()["id"]

    # Update the task title.
    response = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "Updated task title"}
    )

    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated task title"


def test_authenticated_user_can_complete_task(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "taskcompleter",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    # Create a task to complete.
    creation = client.post(
        "/api/tasks",
        json={
            "title": "Task to complete",
            "description": "Temporary completion test"
        }
    )
    assert creation.status_code == 201

    task_id = creation.get_json()["id"]

    # Mark the task as completed.
    response = client.put(
        f"/api/tasks/{task_id}",
        json={"done": True}
    )

    assert response.status_code == 200
    assert response.get_json()["done"] is True


def test_authenticated_user_can_delete_task(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "taskdeleter",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    # Create a task to delete.
    creation = client.post(
        "/api/tasks",
        json={
            "title": "Task to delete",
            "description": "Temporary deletion test"
        }
    )
    assert creation.status_code == 201

    task_id = creation.get_json()["id"]

    # Delete the task.
    response = client.delete(f"/api/tasks/{task_id}")

    assert response.status_code in (200, 204)

    # Verify that the task no longer exists.
    check = client.get(f"/api/tasks/{task_id}")
    assert check.status_code == 404


def test_duplicate_registration_is_rejected(client):
    # Register the username for the first time.
    first_registration = client.post(
        "/api/register",
        json={
            "username": "duplicateuser",
            "password": "TaskPass123!"
        }
    )
    assert first_registration.status_code == 201

    # Try registering the same username again.
    second_registration = client.post(
        "/api/register",
        json={
            "username": "duplicateuser",
            "password": "AnotherPass123!"
        }
    )

    # Duplicate registration should be rejected.
    assert second_registration.status_code in (400, 409)


def test_registration_rejects_username_below_minimum_length(client):
    response = client.post(
        "/api/register",
        json={
            "username": "a",
            "password": "TaskPass123!"
        }
    )

    assert response.status_code in (400, 422)


def test_registration_rejects_short_password(client):
    response = client.post(
        "/api/register",
        json={
            "username": "shortpassuser",
            "password": "1"
        }
    )

    assert response.status_code in (400, 422)


def test_authenticated_user_can_search_tasks_by_title(client):
    registration = client.post(
        "/api/register",
        json={
            "username": "tasksearcher",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    # Create two tasks with different titles.
    first_task = client.post(
        "/api/tasks",
        json={"title": "STQA Search Target"}
    )
    second_task = client.post(
        "/api/tasks",
        json={"title": "Unrelated Assignment"}
    )

    assert first_task.status_code == 201
    assert second_task.status_code == 201

    # Search for the target task.
    response = client.get("/api/tasks?q=Search%20Target")

    assert response.status_code == 200

    tasks = response.get_json()
    titles = [task["title"] for task in tasks]

    assert "STQA Search Target" in titles
    assert "Unrelated Assignment" not in titles


def test_api_rejects_invalid_category_id(client):
    # Register and authenticate a test user.
    registration = client.post(
        "/api/register",
        json={
            "username": "invalidcategoryuser",
            "password": "TaskPass123!"
        }
    )
    assert registration.status_code == 201

    # Try creating a task with a category ID that does not exist.
    response = client.post(
        "/api/tasks",
        json={
            "title": "Invalid category test",
            "category_id": 99999
        }
    )

    # The API should reject a nonexistent category ID.
    assert response.status_code == 400
