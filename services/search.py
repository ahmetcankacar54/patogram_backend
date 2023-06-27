from fastapi import Depends, HTTPException, status
from requests import Session
from database.configuration import get_db
from models.disease_name import DiseaseName
from models.user import User


async def search(keyword: str, db: Session = Depends(get_db)):
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
        # print(name)
        nameSearchList.append(name)
    resultsList = checkKeyword(keyword, diseaseSearchList, nameSearchList)

    return resultsList


def checkKeyword(keyword: str, diseaseList, nameList):
    resultList = []
    for i, words in enumerate(diseaseList):
        if keyword.lower() in diseaseList[i].lower():
            print(words)
            resultList.append(words)
    for i, words in enumerate(nameList):
        print(nameList[i])
        if keyword.lower() in nameList[i].lower():
            resultList.append(words)

    return resultList
