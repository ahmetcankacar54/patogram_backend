from fastapi import Depends, HTTPException, status
from requests import Session
from database.configuration import get_db
from models.disease_name import DiseaseName
from models.user import User


async def searchMainpage(keyword: str, db: Session = Depends(get_db)):
    diseaseQuerry = db.query(DiseaseName).all()
    userQuerry = db.query(User.full_name).all()
    diseaseSearchList = []
    nameSearchList = []

    for item in diseaseQuerry:
        name_tr = item.disease_tr
        name_en = item.disease_en
        diseaseSearchList.append(name_tr)
        diseaseSearchList.append(name_en)

    for item in userQuerry:
        name = item.full_name
        nameSearchList.append(name)

    resultsList = checkKeyword(keyword, diseaseSearchList, nameSearchList)

    return resultsList


async def searchDiscover(keyword: str, db: Session = Depends(get_db)):
    diseaseQuerry = db.query(DiseaseName).all()
    userQuerry = db.query(User.id, User.full_name).all()
    diseaseList = []
    userList = []
    diseaseList = diseaseQuerry
    userList = userQuerry
    diseaseSearchList = []
    nameSearchList = []

    for item in diseaseList:
        disaseId = item.id
        diseaseNameAndIdTr = item.id, item.disease_tr
        diseaseNameAndIdEn = disaseId, item.disease_en
        diseaseSearchList.append(diseaseNameAndIdTr)
        diseaseSearchList.append(diseaseNameAndIdEn)

    for item in userList:
        userId = item.id
        userName = item.full_name
        user = userId, userName
        nameSearchList.append(user)
    resultsList = checkKeyword(keyword, diseaseSearchList, nameSearchList)

    return resultsList


def checkKeyword(keyword, diseaseList, nameList):
    resultList = []

    for disease in diseaseList:
        if keyword.lower() in disease[1].lower():
            resultList.append(disease)

    for names in nameList:
        if keyword.lower() in names[1].lower():
            resultList.append(names)

    return resultList
