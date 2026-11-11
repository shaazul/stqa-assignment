
from locust import HttpUser, task, between


class PyTodoUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        response = self.client.post(
            "/api/login",
            json={
                "username": "farish01",
                "password": "TestPass123",
            },
        )

        if response.status_code != 200:
            print("Login failed. Check your test account and credentials.")

    @task
    def get_tasks(self):
        with self.client.get(
            "/api/tasks",
            name="GET /api/tasks",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status: {response.status_code}")
