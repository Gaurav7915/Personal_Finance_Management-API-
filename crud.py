from sqlalchemy.orm import Session
from models import Expense
from schemas import Expense as ExpenseSchema


def create_expense(db: Session, expense: ExpenseSchema):
    db_expense = Expense(name=expense.name, amount=expense.amount, category=expense.category)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(Expense).all()


def get_expense_by_id(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()


def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense
