from pydantic import BaseModel, HttpUrl, Field, ConfigDict

class ExerciseSchema(BaseModel):
    """
        Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesSchema(BaseModel):
    """
        Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """
        Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseModel):
    """
        Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
        Описание структуры ответа на создание задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
        Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str | None = None
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    order_index: int | None = Field(alias="orderIndex", default=None)
    description: str | None = None
    estimated_time: str | None = Field(alias="estimatedTime", default=None)

class UpdateExerciseResponseSchema(BaseModel):
    """
        Описание структуры ответа на обновление задания.
    """
    exercise: ExerciseSchema