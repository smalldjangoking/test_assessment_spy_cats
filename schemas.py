from pydantic import BaseModel, Field
from typing import Optional, Annotated, List


class CatSchema(BaseModel):
    name: str
    experience: int
    breed: str
    salary: float


class CatSalaryShema(BaseModel):
    salary: float


class TargetCreateSchema(BaseModel):
    name: str
    country: str
    notes: Optional[str] = ""


class CatCreateSchema(BaseModel):
    cat_id: Optional[int] = None
    targets: Annotated[List[TargetCreateSchema], Field(min_length=1, max_length=3)]


class MissionTargetPatchSchema(BaseModel):
    note: Optional[str] = None
    complete: Optional[bool] = False