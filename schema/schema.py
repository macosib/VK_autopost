from typing import List
from pydantic import BaseModel

class Size(BaseModel):
    height: int
    type: str
    width: int
    url: str

class Item(BaseModel):
    id: int

class Response(BaseModel):
    count: int
    items: List[Item]

class APIResponsePostGet(BaseModel):
    response: Response

class ResponsePostIdPost(BaseModel):
    post_id: int

class APIResponseWallPost(BaseModel):
    response: ResponsePostIdPost


class APIResponseDeletePost(BaseModel):
    response: int