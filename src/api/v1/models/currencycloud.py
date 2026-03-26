from typing import Annotated, Optional

from pydantic import BaseModel, EmailStr, StringConstraints, constr
from typing import List
from enum import Enum
from pydantic import HttpUrl
from datetime import datetime as dt


class AccountLegalEntityType(Enum):
    COMPANY = "company"
    INDIVIDUAL = "individual"


class AccountCreateModel(BaseModel):
    account_name: str = "jeckonia"
    legal_entity_type: AccountLegalEntityType = AccountLegalEntityType.COMPANY
    street: str = "Lithuli Avenue 00100 Nairobi"
    city: str = "Nairobi"
    country: str = "KE"


class AccountUpdateModel(BaseModel):
    account_name: Optional[str] = "timothy"
    street: Optional[str] = "Lithuli Avenue 00100 Nairobi"
    city: Optional[str] = "Nairobi"


class CustomerRiskEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class CompanyComplianceAccountModel(BaseModel):
    industry_type: str = "General"
    # trading_address_street: str = "Lithuli Avenue"
    business_website_url: HttpUrl = "https://pkenya.co.ke"
    # date_of_incorporation: str = dt.today().isoformat()
    # business_website_url: Optional[HttpUrl] = None
    # expected_transaction_countries: List[str] = ["KE"]
    # expected_transaction_currencies: List[str] = ["KES"]
    # expected_monthly_activity_volume: int = 0
    # expected_monthly_activity_value: float = 0.0
    # tax_identification: Optional[str] = None
    # customer_risk: CustomerRiskEnum = CustomerRiskEnum.MEDIUM


class AccountOrderFilterEnum(str, Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class AccountStatusFilterEnum(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    ENABLED_NO_TRADING = "enabled_no_trading"


class AccountFilterModel(BaseModel):
    order_asc_desc: AccountOrderFilterEnum = AccountOrderFilterEnum.ASCENDING
    status: AccountStatusFilterEnum | None = AccountStatusFilterEnum.ENABLED_NO_TRADING
    account_name: str | None = None


### CONTACT MODELS STARTS


class ContactStatusEnum(str, Enum):
    ENABLED = "enabled"
    DISABLED = "not_enabled"


class ContactCreateModel(BaseModel):
    account_id: str
    first_name: Annotated[str, StringConstraints(min_length=3)] = "jeckonia"
    last_name: Annotated[str, StringConstraints(min_length=3)] = "kwasa"
    email_address: EmailStr = "pauline@zentrapay.com"
    phone_number: Annotated[str, StringConstraints(pattern=r"^\+?[1-9]\d{7,14}$")] = (
        "+254745547755"
    )
    status: ContactStatusEnum = ContactStatusEnum.ENABLED


class ContactUpdateModel(BaseModel):
    first_name: Annotated[str, StringConstraints(min_length=3)] = "jeckonia"
    status: ContactStatusEnum = ContactStatusEnum.ENABLED


### TRANSACTION MODELS STARTS


class TransactionActionEnum(str, Enum):
    CONVERSION = "conversion"
    CONVERSION_DEPOSIT = "conversion_deposit"
    DEPOSIT_REFUND = "deposit_refund"
    FUNDING = "funding"
    MARGIN = "margin"
    MANUAL_TRANSACTION = "manual_transaction"
    PAYMENT = "payment"
    PAYMENT_FAILURE = "payment_failure"
    PAYMENT_FEE = "payment_fee"
    PAYMENT_UNRELEASE = "payment_unrelease"
    TRANSFER = "transfer"


class TransactionTypeEnum(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class TransactionStatusEnum(str, Enum):
    COMPLETED = "completed"
    DELETED = "deleted"
    PENDING = "pending"


class TransactionScopeEnum(str, Enum):
    ALL = "all"
    CLIENTS = "clients"
    OWN = "own"


class TransactionQueryModel(BaseModel):
    # action: TransactionActionEnum = TransactionActionEnum.PAYMENT
    # type: TransactionTypeEnum = TransactionTypeEnum.CREDIT
    # status: TransactionStatusEnum = TransactionStatusEnum.COMPLETED
    # scope: TransactionScopeEnum = TransactionScopeEnum.ALL
    # order_asc_desc: AccountOrderFilterEnum = AccountOrderFilterEnum.ASCENDING
    on_behalf_of: str
    # currency: str | None = "KES"
