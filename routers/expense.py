from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
import database,schemas,models
import oauth
router = APIRouter(prefix = "/expenses",tags=['Expenses'])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Expense)
def create_expenses(expense: schemas.Expense,db: Session= Depends(database.get_db),current_user: int = Depends(oauth.get_current_user)):
    
    new_expense = models.Expense(user_id = current_user.id,**expense.dict())
   
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

@router.get("/{id}",response_model=schemas.Expense)
def get_expense(id: int, db: Session = Depends(database.get_db),current_user: int = Depends(oauth.get_current_user)):

    expense = db.query(models.Expense).filter(models.Expense.id == id).first()

    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Expense {id} not found")
    return expense


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(id: int, db: Session = Depends(database.get_db),current_user: int = Depends(oauth.get_current_user)):

    query = db.query(models.Expense).filter(models.Expense.id == id)
    expense = query.first()
    
    if expense == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Expense {id} not found") 


    if expense.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")


    query.delete(synchronize_session= False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Expense)
def update_expense(id: int, updated_expense: schemas.Expense,db: Session = Depends(database.get_db),current_user: int = Depends(oauth.get_current_user)):

    query = db.query(models.Expense).filter(models.Expense.id == id)
    
    expense = query.first()

    if expense == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Expense {id} not found")
    
    if expense.user_id != current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    query.update(updated_expense.dict(),synchronize_session=False)

    db.commit()

    return expense
