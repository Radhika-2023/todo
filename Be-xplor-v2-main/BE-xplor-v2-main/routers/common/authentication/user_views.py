# from fastapi import APIRouter, Depends, status
# from fastapi.responses import JSONResponse
# from sqlalchemy.orm import Session
# from typing import Annotated
# from uuid import uuid4
#
# from app.database import get_db_session
# from app.models import XplorUser
# from app.schemas.common.UserSchemas import UserAuth
# from app.common.utils import (
#     get_hashed_password,
#     create_access_token,
#     create_refresh_token,
#     verify_password
# )
#
# router = APIRouter(tags=['UserViews'])
#
# db_dependency = Annotated[Session, Depends(get_db_session)]
#
# @router.post('/register', summary="Register new user")
# async def create_user(data: UserAuth, db: db_dependency):
#     try:
#         # querying database to check if user already exist
#         db_user = db.query(XplorUser).filter(XplorUser.username==data.username).first()
#         if db_user is not None:
#                 return JSONResponse(content={
#                     "success": False,
#                     "response": "User Already Exists",
#                     "details": {
#                         "message": "A user with this username already exists!"
#                     }
#                 }, status_code=status.HTTP_400_BAD_REQUEST)
#
#         new_user = XplorUser(id=str(uuid4()),username=data.username,password=get_hashed_password(data.password))
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#
#         return JSONResponse(content={
#                 "success": True,
#                 "response": {
#                      "access_token": create_access_token(new_user.username),
#                      "refresh_token": create_refresh_token(new_user.username)
#                 },
#                 "details": {
#                     "message": "User registered successfully!"
#                 }
#             }, status_code=status.HTTP_200_OK)
#
#     except Exception as e:
#         print(e)
#
#         return JSONResponse(content={
#             "success": False,
#             "response": "User Registration Failed",
#             "details": {
#                 "message": "Something went wrong!"
#             }
#         }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @router.post('/login', summary="User Login")
# async def user_login(data: UserAuth, db: db_dependency):
#      try:
#           db_user = db.query(XplorUser).filter(XplorUser.username==data.username).first()
#
#           if db_user is None:
#                return JSONResponse(content={
#                     "success": True,
#                     "response": "Invalid User",
#                     "details": {
#                         "message": "User doesn't exist!"
#                     }
#                 }, status_code=status.HTTP_400_BAD_REQUEST)
#
#           if not verify_password(data.password, db_user.password):
#                return JSONResponse(content={
#                     "success": True,
#                     "response": "Invalid Credentials",
#                     "details": {
#                         "message": "User login failed!"
#                     }
#                 }, status_code=status.HTTP_400_BAD_REQUEST)
#
#           return JSONResponse(content={
#                 "success": True,
#                 "response": {
#                         "access_token": create_access_token(db_user.username),
#                         "refresh_token": create_refresh_token(db_user.username)
#                 },
#                 "details": {
#                     "message": "User login successful!"
#                 }
#             }, status_code=status.HTTP_200_OK)
#
#      except Exception as e:
#           print(e)
#           return JSONResponse(content={
#             "success": False,
#             "response": "User Registration Failed",
#             "details": {
#                 "message": "Something went wrong!"
#             }
#         }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)