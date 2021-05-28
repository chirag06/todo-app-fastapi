from typing import Optional
from pydantic import BaseModel

class Create_Item(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False


class Item(Create_Item):
    id: int
    status: bool
