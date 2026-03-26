from typing import Annotated, Optional
import uuid

from api.v1.models.utils import generate_reference
from api.v1.services.utils.account import (
    generate_account_number_with_checksum,
    generate_swift_code,
)
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)
from enum import Enum
from pydantic import HttpUrl
import re


SWIFT_REGEX = re.compile(r"^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?$")


class CountryEnum(str, Enum):
    KE = "KE"
    US = "US"
    UK = "UK"


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


### PAYMENT MODELS STARTS


class CurrencyEnum(str, Enum):
    KES = "KES"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


class PaymentCreateModel(BaseModel):
    currency: CurrencyEnum = CurrencyEnum.KES
    # This id is the main account
    beneficiary_id: str
    amount: float
    reason: Annotated[str, StringConstraints(min_length=3)] = "payment"
    reference: str = Field(default_factory=generate_reference)
    unique_request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class PaymentReviewStatusEnum(str, Enum):
    IN_REVIEW = "in_review"
    PASSED = "passed"
    REJECTED = "rejected"

class PaymentRetrievalModel(BaseModel):
    # review_status: PaymentReviewStatusEnum = PaymentReviewStatusEnum.PASSED
    on_behalf_of: str | None = None
    with_deleted : bool = True





class BeneficiaryRetrievalModel(BaseModel):
    scope: TransactionScopeEnum = TransactionScopeEnum.ALL
    on_behalf_of: str | None = None
    order_asc_desc: AccountOrderFilterEnum = AccountOrderFilterEnum.ASCENDING


class BeneficiaryCreationModel(BaseModel):
    name: str = "some_unique_content"
    bank_account_holder_name: Annotated[
        str, StringConstraints(min_length=3, max_length=100)
    ]
    bank_country: CountryEnum = CountryEnum.KE
    currency: CurrencyEnum = CurrencyEnum.KES
    account_number: str = Field(default_factory=generate_account_number_with_checksum)
    on_behalf_of: str
    bic_swift: str = Field(default_factory=generate_swift_code)
    beneficiary_entity_type: AccountLegalEntityType = AccountLegalEntityType.COMPANY
    beneficiary_company_name: str | None = "Safaricom Limited"
    business_nature: str = "Finance"
    beneficiary_address: str = "Lithuli Avenue 00100 Nairobi, Kenya"
    beneficiary_city: str = "Nairobi"
    beneficiary_country: str = CountryEnum.KE

    @field_validator("bic_swift")
    @classmethod
    def validate_bic_swift(cls, value: str, info):
        value = value.upper()
        if not SWIFT_REGEX.match(value):
            raise ValueError("Invalid BIC/SWIFT format")
        swift_country = value[4:6]
        if "bank_country" in info.data:
            if swift_country != info.data["bank_country"].value:
                raise ValueError("SWIFT country does not match bank country")
        return value

    @model_validator(mode="before")
    @classmethod
    def set_default_swift(cls, data):
        if not data.get("bic_swift"):
            country = data.get("bank_country", CountryEnum.KE)
            data["bic_swift"] = generate_swift_code(country)
        return data

    @model_validator(mode="after")
    def validate_company_rules(self):
        if self.beneficiary_entity_type == AccountLegalEntityType.COMPANY:
            if not self.beneficiary_company_name:
                raise ValueError("beneficiary_company_name is required for companies")
            if self.beneficiary_company_name.isdigit():
                raise ValueError("Company name cannot consist entirely of numbers")
        elif self.beneficiary_entity_type == AccountLegalEntityType.INDIVIDUAL:
            if self.beneficiary_company_name:
                self.beneficiary_company_name = None
        return self


class BeneficiaryDeleteModel(BaseModel):
    on_behalf_of: str | None = None

