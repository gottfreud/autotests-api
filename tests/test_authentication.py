from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


def test_login():
    """
    Проверяет успешность авторизации пользователя через /api/v1/authentication/login.
    """

    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    user_data = CreateUserRequestSchema()
    public_users_client.create_user(user_data)

    login_data = LoginRequestSchema(email=user_data.email, password=user_data.password)
    login_response = authentication_client.login_api(login_data)
    login_response_data = LoginResponseSchema.model_validate(login_response.json())

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    LoginResponseSchema.model_validate(login_response_data)
