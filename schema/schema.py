from typing import List
from pydantic import BaseModel

class Size(BaseModel):
    height: int
    type: str
    width: int
    url: str

class Photo(BaseModel):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: str
    post_id: int | None
    sizes: List[Size]
    text: str
    user_id: int | None
    has_tags: bool

class Attachment(BaseModel):
    type: str
    photo: Photo | None

class Comments(BaseModel):
    can_post: int
    count: int
    groups_can_post: bool

class Likes(BaseModel):
    can_like: int
    count: int
    user_likes: int
    can_publish: int
    repost_disabled: bool

class Reposts(BaseModel):
    count: int
    user_reposted: int

class PostSource(BaseModel):
    platform: str | None
    type: str

class Item(BaseModel):
    donut: dict
    comments: Comments
    marked_as_ads: int
    short_text_rate: float
    hash: str
    type: str
    attachments: List[Attachment] | None
    date: int
    from_id: int
    id: int
    is_favorite: bool
    likes: Likes
    owner_id: int
    post_source: PostSource | None
    post_type: str
    reposts: Reposts
    text: str

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