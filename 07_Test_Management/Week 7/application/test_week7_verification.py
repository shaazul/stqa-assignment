"""New verification procedures. No execution is claimed by including this file."""
import pytest
import app as module

@pytest.fixture
def isolated_app(tmp_path, monkeypatch):
    monkeypatch.setattr(module, "DATABASE", str(tmp_path / "week7.db"))
    monkeypatch.setitem(module.app.config, "TESTING", True)
    module.init_db()
    return module.app

def account(client, username):
    response = client.post("/api/register", json={"username": username, "password": "Week7Pass123!"})
    assert response.status_code == 201
    response = client.post("/api/login", json={"username": username, "password": "Week7Pass123!"})
    assert response.status_code == 200

def test_clean_session_task_access_is_denied(isolated_app):
    client = isolated_app.test_client()
    response = client.get("/api/tasks")
    assert response.status_code == 401
    assert response.get_json()["error"] == "authentication required"

def test_cross_user_get_is_denied(isolated_app):
    owner, other = isolated_app.test_client(), isolated_app.test_client()
    account(owner, "w7owner")
    created = owner.post("/api/tasks", json={"title": "W7 owner only"})
    assert created.status_code == 201
    task_id = created.get_json()["id"]
    account(other, "w7other")
    assert other.get(f"/api/tasks/{task_id}").status_code in (403, 404)
    assert owner.get(f"/api/tasks/{task_id}").status_code == 200

def test_cross_user_delete_is_denied_and_owner_task_survives(isolated_app):
    owner, other = isolated_app.test_client(), isolated_app.test_client()
    account(owner, "w7owner")
    created = owner.post("/api/tasks", json={"title": "W7 preserve owner task"})
    assert created.status_code == 201
    task_id = created.get_json()["id"]
    before = owner.get(f"/api/tasks/{task_id}").get_json()
    account(other, "w7other")
    response = other.delete(f"/api/tasks/{task_id}")
    after = owner.get(f"/api/tasks/{task_id}")
    assert (response.status_code in (403, 404) and after.status_code == 200
            and after.get_json() == before), (response.status_code, after.status_code)
