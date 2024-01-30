from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pytest import Item, Session
from sqlalchemy.orm import Session
from jose import JWTBearer
from database import get_db_session


router = APIRouter(tags=['Items'])
db_dependency = Annotated[Session, Depends(get_db_session)]


@router.get("/auth/sendotp/{number}")
def sendOtp(number):
    print("Input number for otp : {}", number)


@router.get("/auth/validateotp")
def sendOtp(number):
    print("Input number for otp : {}", number)

@router.get("/get-items/", dependencies=[Depends(JWTBearer())])
async def get_items(db: db_dependency):
    try:
        db_items = db.query(Item).all()
        items = []

        for item in db_items:
            dict = {}
            dict["id"] = item.id
            dict["name"] = item.name
            dict["count"] = item.count
            dict["additional_info"] = item.additional_info

            items.append(dict)

        return JSONResponse(content={
            "success": True,
            "response": items,
            "details": {
                "message": "All items returned"
            }
        }, status_code=status.HTTP_200_OK)

    except:
        return JSONResponse(content={
            "success": False,
            "response": "Get Item Failed",
            "details": {
                "message": "Something went wrong !"
            }
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
