from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExerciseClient
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    GetExercisesResponseSchema, GetExercisesSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercises_response, assert_exercise
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercise(self, exercises_client: ExerciseClient, function_course: CourseFixture,):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert response.status_code == HTTPStatus.OK
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, exercises_client: ExerciseClient, function_exercise: ExerciseFixture):
        query = GetExercisesSchema(course_id=function_exercise.response.exercise.course_id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert response.status_code == HTTPStatus.OK
        assert_get_exercises_response(response_data, [function_exercise.response])
