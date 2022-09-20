from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from ..repository import blog

# Set the url prefix and tag for the blog related api calls
router = APIRouter(prefix="/blog", tags=["blogs"])


# Get all blogs
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# Create a new blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)


# Update an existing blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)


# Get a specific blog with it's Id
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    return blog.show(id, response, db)
