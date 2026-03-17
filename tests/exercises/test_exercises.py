from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExerciseClient
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from fixtures.courses import CourseFixture
from tools.assertions.exercises import assert_create_exercise_response


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercise(self, exercises_client: ExerciseClient, function_course: CourseFixture,):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert response.status_code == HTTPStatus.OK
        assert_create_exercise_response(request, response_data)
        CreateExerciseResponseSchema.model_validate_json(response.text)