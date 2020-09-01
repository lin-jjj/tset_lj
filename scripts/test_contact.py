import allure
import pytest
class TestContact:
#     @pytest.allure.severity(pytest.allure.severity_level.BlLOCKER)
    @allure.step(title="登录")
    def test_login1(self):
        allure.attach('请登录','登录登录')  #代码的描述，第二个参数是对第一个更具体的描述
        print('okokok')
        assert 1
#     @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="用户名")  #函数的描述
    def test_login2(self):
        print('okok')
        assert 1
#     @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)  #优先级，严重程度
    @allure.step(title="密码")
    def test_login3(self):
        print('ok')
        assert 1

