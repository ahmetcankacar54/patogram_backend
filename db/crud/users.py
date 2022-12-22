from sqlalchemy.orm.session import Session
from db.models.users import User
from schemas.users import CreateUser

def create_new_user(user:CreateUser,db:Session):
    user = User(name=user.name,
                        lastname=user.lastname,
                        email=user.email,
                        password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
def get_all_users(db:Session):
    users = db.query(User).all()
    return users