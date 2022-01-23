from django.test import (
    TestCase,
    Client
)

# Create your tests here.
client = Client()

class userTest(TestCase):
    def test_auth(self):
        empty_data = {
            'username' : '',
            'password' : ''
        }
        data = {
            'username' : 'test_username',
            'password' : 'test_password',
        }
        response = client.post('/api/user/sign_up/', empty_data)
        self.assertEqual(response.status_code, 404, "데이터 부족")
        response = client.post('/api/user/sign_up/', data)
        self.assertEqual(response.status_code, 201, "회원가입 완료")
        response = client.post('/api/user/sign_up/', data)
        self.assertEqual(response.status_code, 200, "이미 가입 되어있음")
        response = client.get('/api/user/sign_in/?username=&password=')
        self.assertEqual(response.status_code, 404, "로그인 실패")
        response = client.get('/api/user/sign_in/?username=test_username&password=test_password')
        self.assertEqual(response.status_code, 200, "로그인 완료")
