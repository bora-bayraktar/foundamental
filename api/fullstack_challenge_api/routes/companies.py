from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from sqlalchemy.orm import Session
from fullstack_challenge_api.models.company import Company
from fullstack_challenge_api.models.deal import Deal
from datetime import datetime

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
    companies = db.query(Company).all()
    return companies


@router.get("/deals")
async def get_deals(db: Session = Depends(get_db)):
    deals = db.query(Deal).all()
    for deal in deals:
        timestamp_sec = deal.date // 1000
        deal.date = datetime.fromtimestamp(timestamp_sec)
    return deals