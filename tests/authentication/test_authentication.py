from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
import pytest
import allure
from allure_commons.types import Severity


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        """
        Проверяет успешность авторизации пользователя через /api/v1/authentication/login.
        """

        login_data = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(login_data)
        response_data = LoginResponseSchema.model_validate(response.json())

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        LoginResponseSchema.model_validate(response_data)