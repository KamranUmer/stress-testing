from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/login", {
            "username": "Kamran",
            "password": "qwer1234"
        })

    @task
    def test_endpoint(self):
        self.client.get("/")
    

# from locust import HttpUser, task

# class MyUser(HttpUser):
#     @task
#     def test_endpoint(self):
#         self.client.get("/")