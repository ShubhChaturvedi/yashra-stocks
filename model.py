from pydantic import BaseModel
from typing import Optional


class Service(BaseModel):
    service_name: str
    service_description: Optional[str] = None

    class Config:
        orm_mode = True

