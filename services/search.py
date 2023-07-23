from fastapi import Depends
from requests import Session
from database.configuration import get_db
from models.disease import Disease
from models.post import Post
from models.user import User
from models.user_follow import UserFollow
from services.post import get_posts_mainpage


async def searchMainpage(keyword: str, userId: int, db: Session = Depends(get_db)):
    followsQuerry = db.query(UserFollow).filter(UserFollow.user_id == userId).all()
    diseaseSearchList = []
    nameSearchList = []
    postList = await get_posts_mainpage(userId, db)

    for item in postList:
        diseaseId = item.disease_type.id
        diseaseNameAndIdTr = {
            "id": diseaseId,
            "disease_name": item.disease_type.disease_tr,
        }
        diseaseNameAndIdEn = {
            "id": diseaseId,
            "disease_name": item.disease_type.disease_en,
        }
        diseaseSearchList.append(diseaseNameAndIdTr)
        diseaseSearchList.append(diseaseNameAndIdEn)

    for item in followsQuerry:
        userQuerry = db.query(User).filter(User.id == item.follows_id).first()
        user_id = userQuerry.id
        user_name = userQuerry.full_name
        user = {"id": user_id, "full_name": user_name}
        nameSearchList.append(user)

    resultsList = checkKeyword(keyword, diseaseSearchList, nameSearchList)

    return resultsList


async def searchDiscover(keyword: str, db: Session = Depends(get_db)):
    postQuerry = db.query(Post.disease_type).all()
    userQuerry = db.query(User.id, User.full_name).all()
    diseaseList = []
    userList = []
    diseaseList = postQuerry
    userList = userQuerry
    diseaseSearchList = []
    nameSearchList = []

    for item in diseaseList:
        diseaseId = item[0]
        diseaseQuerry = db.query(Disease).filter(Disease.id == diseaseId).first()
        if diseaseQuerry:
            diseaseNameAndIdTr = {
                "id": diseaseId,
                "disease_name": diseaseQuerry.disease_tr,
            }
            diseaseNameAndIdEn = {
                "id": diseaseId,
                "disease_name": diseaseQuerry.disease_en,
            }
            diseaseSearchList.append(diseaseNameAndIdTr)
            diseaseSearchList.append(diseaseNameAndIdEn)
        else:
            pass

    for item in userList:
        userId = item.id
        userName = item.full_name
        user = {"id": userId, "full_name": userName}
        nameSearchList.append(user)

    resultsList = checkKeyword(keyword, diseaseSearchList, nameSearchList)

    return resultsList


async def searchOnlyDisease(keyword: str, db: Session = Depends(get_db)):
    diseaseQuerry = db.query(Disease).all()
    diseaseList = []
    diseaseList = diseaseQuerry
    diseaseSearchList = []

    for item in diseaseList:
        diseaseId = item.id
        diseaseNameAndIdTr = {"id": diseaseId, "disease_name": item.disease_tr}
        diseaseNameAndIdEn = {"id": diseaseId, "disease_name": item.disease_en}
        diseaseSearchList.append(diseaseNameAndIdTr)
        diseaseSearchList.append(diseaseNameAndIdEn)

    resultsList = checkKeyword(keyword, diseaseSearchList)

    return resultsList


def checkKeyword(keyword, diseaseList, nameList=None):
    resultList = []

    for disease in diseaseList:
        if keyword.lower() in disease["disease_name"].lower():
            resultList.append(disease)

    if nameList != None:
        for names in nameList:
            if keyword.lower() in names["full_name"].lower():
                resultList.append(names)
    else:
        pass

    return resultList
