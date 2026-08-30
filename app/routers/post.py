from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List,Optional
from .. import models, schemas,oauth2
from .. database import get_db
from sqlalchemy import func
router=APIRouter(
     prefix="/posts",
     tags=['Posts']
)

@router.get("/",response_model=List[schemas.Post])
async def our_posts(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts=cursor.fetchall()
    posts=db.query(models.Post).first(models.Post.owner_id==current_user.id).all()
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
async def create_post(post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #post_dict=post.model_dump() #it is the brand new posts that we are adding
    #post_dict['id']=randrange(0,1000000)
    #my_posts.append(post_dict)
    #INSERTING A NEW POST INTO OUR DATABASE
    #######################we were basically writing the sequel query and then running it but below now we will use SQLALCHEMY
    # cursor.execute(
    # """INSERT INTO posts(title, content, published)
    #    VALUES(%s, %s, %s)
    #    RETURNING *""",
    # (post.title, post.content, post.published)
    # )
    # new_post=cursor.fetchone()
    # conn.commit()
    ########**********always make sure that you commit the query**********
    #print(**post.dic()) ###########ear;ier we were basically doinog post.title and post.contetnt but what if there are hundreds of them , to make life easier we use this
    print(current_user.email)
    new_post=models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/",response_model=List[schemas.PostOut])
def get_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user),Limit:int=10,skip:int =0,search: Optional[str]=""): 
    posts=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    return posts


@router.get("/{id}",response_model=schemas.PostOut) #this id represents the path parameter 
def get_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):  #validates and it automatically converts it into an integer
#i know want that the user should basiicaly get options of which post they want to see
    # cursor.execute(""" SELECT * FROM posts WHERE id=%s""",(str(id),)) #we can add this comma to avoid any type of error sir was also not sure abiut this#over here we need to convert this into string as we will need that, but we cann't do id:str but that will create an error as user can type anything
    # test_post=cursor.fetchone()
    # print(test_post)
    # print(Limit)
    post=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    ##default is left inner joint
    #post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id={id} was not found")
        #repsonses.status_code=status.HTTP_404_NOT_FOUND
        #return {'message':f"post with id={id} was not found"} this was a bit sloppy so we will use something better

    return {"post_detail":post}


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #find the index in the array that  ha s the require id
    #my_post.pop(index)
    # cursor.execute(""" DELETE FROM posts WHERE id=%s RETURNING *""",(str(id),))
    # delete_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id).first()
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} doesn't exists")
    if post.owner_id!=oauth2.current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    post_query.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)#whenever we are using 204 it expects us to not send any data back, so we had to delete our returning message tht the post has been deleted

    
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title=%s , content=%s , published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,(str(id))))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} doesn't exists")
    if post.owner_id!=oauth2.current_user.id:
             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()
