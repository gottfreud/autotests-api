from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: Field(alias="lastName")
    first_name: Field(alias="firstName")
    middle_name: Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: Field(alias="lastName")
    first_name: Field(alias="firstName")
    middle_name: Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: Field(alias="lastName")
    first_name: Field(alias="firstName")
    middle_name: Field(alias="middleName")

