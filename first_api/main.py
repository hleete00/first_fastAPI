from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# URL and function to get 10 published blogs
@app.get('/blog')
# Set parameters equal to values to set their default if nothing is passed
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog list'}
    else:
        return {'data': f'{limit} blog list'}


# URL and function to get all unpublished blogs
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


# URL and function to get specific blog
@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


# URL and function to get comments for specific blogs
@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return limit
    return {'data': {'1', '2', '3'}}


# Create a model to hold blog information
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# URL and function to post new blog


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}
