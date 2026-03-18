from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExercisesResponseSchema, GetExercisesSchema, UpdateExerciseRequestSchema, \
    UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure

@allure.step("Check create exercise response")
def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.order_index, expected.order_index, "order_index")

@allure.step("Check get exercise response")
def assert_get_exercise_response(get_exercises_response: GetExercisesResponseSchema, create_exercise_responses: CreateExerciseResponseSchema):
    assert_exercise(get_exercises_response.exercise, create_exercise_responses.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(response: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(expected, response)

@allure.step("Check get exercises response")
def assert_get_exercises_response(get_exercises_response: GetExercisesResponseSchema, create_exercise_responses: list[CreateExerciseResponseSchema]):
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")
    for index, create_exercise_responses in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_responses.exercise)