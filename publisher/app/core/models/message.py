from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    name: str
    description: Optional[str] = None
