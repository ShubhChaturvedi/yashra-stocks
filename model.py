from pydantic import BaseModel
from typing import Optional


class Service(BaseModel):
    service_name: str
    service_description: Optional[str] = None

    class Config:
        orm_mode = True

class Platform(BaseModel):
    platform_name: str
    platform_description: Optional[str] = None

    class Config:
        orm_mode = True

class ServicePlatform(BaseModel):
    serive = Service
    platform = Platform

    class Config:
        orm_mode = True

class CorporateBond(BaseModel):
    bond_name: str
    min_investment: float
    coupon_rate: float
    maturity_date: str
    rating: str
    bond_type: str
    payment_terms: str
    bond_description: Optional[str] = None

    class Config:
        orm_mode = True

class CorporateBondPlatform(BaseModel):
    corporate_bond = CorporateBond
    platform = Platform

    class Config:
        orm_mode = True

class CreditCard(BaseModel):
    card_name: str
    card_type: str
    card_description: Optional[str] = None
    card_limit: float
    card_annual_fee: float
    card_interest_rate: float

    class Config:
        orm_mode = True

class CreditCardPlatform(BaseModel):
    credit_card = CreditCard
    platform = Platform

    class Config:
        orm_mode = True


class HomeLoan(BaseModel):
    loan_name: str
    loan_description: Optional[str] = None
    loan_type: str
    loan_interest_rate: float
    loan_max_amount: float
    loan_tenure: int

    class Config:
        orm_mode = True

class HomeLoanPlatform(BaseModel):
    home_loan = HomeLoan
    platform = Platform

    class Config:
        orm_mode = True

class CarLoan(BaseModel):
    loan_name: str
    loan_description: Optional[str] = None
    loan_type: str
    loan_interest_rate: float
    loan_max_amount: float
    loan_tenure: int

    class Config:
        orm_mode = True

class CarLoanPlatform(BaseModel):
    car_loan = CarLoan
    platform = Platform

    class Config:
        orm_mode = True


class PersonalLoan(BaseModel):
    loan_name: str
    loan_description: Optional[str] = None
    loan_type: str
    loan_interest_rate: float
    loan_max_amount: float
    loan_tenure: int

    class Config:
        orm_mode = True

class PersonalLoanPlatform(BaseModel):

    personal_loan = PersonalLoan
    platform = Platform

    class Config:
        orm_mode = True

class GoldLoan(BaseModel):
    loan_name: str
    loan_description: Optional[str] = None
    loan_type: str
    loan_interest_rate: float
    loan_max_amount: float
    loan_tenure: int

    class Config:
        orm_mode = True

class GoldLoanPlatform(BaseModel):
    gold_loan = GoldLoan
    platform = Platform

    class Config:
        orm_mode = True

class StockBrokerage(BaseModel):
    broker_name: str
    broker_description: Optional[str] = None
    broker_type: str
    broker_account_opening_fee: float
    broker_transaction_fee: float
    broker_annual_fee: float

    class Config:
        orm_mode = True

class StockBrokeragePlatform(BaseModel):
    stock_brokerage = StockBrokerage
    platform = Platform

    class Config:
        orm_mode = True

class MutualFund(BaseModel):
    fund_name: str
    fund_description: Optional[str] = None
    fund_type: str
    fund_min_investment: float
    fund_risk: str
    fund_return: float

    class Config:
        orm_mode = True

class MutualFundPlatform(BaseModel):
    mutual_fund = MutualFund
    platform = Platform

    class Config:
        orm_mode = True
