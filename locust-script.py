from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://220.69.203.87:30088"  # 프로토콜을 포함한 올바른 URL
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def login(self):
        # 1. 로그인 URL에 이메일을 포함하여 GET 요청을 보냄
        login_url = "/cloudapp/login/?email=asd000930@naver.com"
        response = self.client.get(login_url)
        
        # 2. 로그인 페이지로 접속한 후, 비밀번호를 입력하여 로그인
        if response and response.status_code == 200:
            login_data = {
                "email": "asd000930@naver.com",  # 이메일 (이미 URL에 포함되어 있으므로 굳이 필요는 없음)
                "password": "password123",  # 가상의 비밀번호
            }
            login_response = self.client.post("/cloudapp/login/", data=login_data)
            
            # 3. 로그인 요청의 성공 여부 확인
            if login_response and login_response.status_code == 200:
                print("Login successful!")
            else:
                print(f"Login request failed with status code: {login_response.status_code if login_response else 'No Response'}")
        else:
            print(f"Failed to access login page. Status code: {response.status_code if response else 'No Response'}")
