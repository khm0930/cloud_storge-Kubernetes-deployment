from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def my_task(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)
