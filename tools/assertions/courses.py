from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

def assert_course(actual: CourseSchema, expected: CourseSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

def assert_get_courses_response(get_courses_response: GetCoursesResponseSchema, create_course_responses: list[CreateCourseResponseSchema]):
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_responses in enumerate(create_course_responses):
        assert_course(
            get_courses_response.courses[index], create_course_responses.course
        )

def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.course.preview_file.id, request.preview_file_id, "preview_file_id")
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, "created_by_user_id")
