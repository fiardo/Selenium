from locust import HttpUser, task

class perfom(HttpUser):
    @task
    def perMethod(self):
        self.client.get("https://www.universityliving.com/")