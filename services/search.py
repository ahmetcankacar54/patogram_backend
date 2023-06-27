from fastapi import Depends, HTTPException, status
from requests import Session
from database.configuration import get_db
from models.disease_name import DiseaseName
from models.user import User


diseaseSearchList = []
nameSearchList = []


async def search(keyword: str, db: Session = Depends(get_db)):
    diseaseQuerry = db.query(DiseaseName).all()
    userQuerry = db.query(User.full_name).all()

    for item in diseaseQuerry:
        name_tr = item.disease_tr
        name_en = item.disease_en
        diseaseSearchList.append(name_tr)
        diseaseSearchList.append(name_en)

    for item in userQuerry:
        name = item.full_name
        nameSearchList.append(name)
    resultsList = checkKeyword(keyword)

    return resultsList


def checkKeyword(keyword: str):
    resultList = []
    for i, words in enumerate(diseaseSearchList):
        if keyword.lower() in diseaseSearchList[i].lower():
            print(words)
            resultList.append(words)
    for i, words in enumerate(nameSearchList):
        if keyword.lower() in nameSearchList[i].lower():
            resultList.append(words)

    return resultList
