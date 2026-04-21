from decimal import Decimal
from typing import Annotated, Optional
import uuid

from zentrapay.api.v1.models.libs.ordering import OrderingParams, PaginationParams
from zentrapay.api.v1.models.utils import generate_reference
from zentrapay.api.v1.services.utils.account import (
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
from pydantic import HttpUrl
import re
from faker import Faker

from .choices import (
    AccountOrderFilterEnum,
    AccountStatusFilterEnum,
    ContactStatusEnum,
    CountryEnum,
    AccountLegalEntityType,
    CurrencyEnum,
    FEchangeEnum,
    FundingAction,
    PaymentType,
    TransactionScopeEnum,
)

faker = Faker()

SWIFT_REGEX = re.compile(r"^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?$")


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


class CompanyComplianceAccountModel(BaseModel):
    industry_type: str = "General"
    # trading_address_street: str = "Lithuli Avenue"
    country_of_incorporation: str = "KE"
    business_website_url: HttpUrl = "https://pkenya.co.ke"
    # date_of_incorporation: str = dt.today().isoformat()
    # business_website_url: Optional[HttpUrl] = None
    # expected_transaction_countries: List[str] = ["KE"]
    # expected_transaction_currencies: List[str] = ["KES"]
    # expected_monthly_activity_volume: int = 0
    # expected_monthly_activity_value: float = 0.0
    # tax_identification: Optional[str] = None
    # customer_risk: CustomerRiskEnum = CustomerRiskEnum.MEDIUM


class AccountFilterModel(BaseModel):
    order_asc_desc: AccountOrderFilterEnum = AccountOrderFilterEnum.ASCENDING
    status: AccountStatusFilterEnum | None = AccountStatusFilterEnum.ENABLED_NO_TRADING
    account_name: str | None = None


### CONTACT MODELS STARTS


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


class TransactionQueryModel(BaseModel):
    # action: TransactionActionEnum = TransactionActionEnum.PAYMENT
    # type: TransactionTypeEnum = TransactionTypeEnum.CREDIT
    # status: TransactionStatusEnum = TransactionStatusEnum.COMPLETED
    # scope: TransactionScopeEnum = TransactionScopeEnum.ALL
    # order_asc_desc: AccountOrderFilterEnum = AccountOrderFilterEnum.ASCENDING
    # on_behalf_of: Annotated[uuid.UUID, StringConstraints(min_length=10)] = Field(
    #     description="A contact UUID for the sub-account you're acting on behalf of.",
    #     example="28ddfb19-7a33-45fd-ba96-2ccb6e298769",
    # )
    on_behalf_of: uuid.UUID | None = Field(
        description="A contact UUID for the sub-account you're acting on behalf of.",
        example="28ddfb19-7a33-45fd-ba96-2ccb6e298769",
        default=None,
    )
    # currency: str | None = "KES"


### PAYMENT MODELS STARTS


class PaymentCreateModel(BaseModel):
    currency: CurrencyEnum = CurrencyEnum.KES
    # This id is the main account
    beneficiary_id: str
    amount: float
    reason: Annotated[str, StringConstraints(min_length=3)] = "payment"
    reference: str = Field(default_factory=generate_reference)
    unique_request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class PaymentRetrievalModel(BaseModel):
    # review_status: PaymentReviewStatusEnum = PaymentReviewStatusEnum.PASSED
    on_behalf_of: str | None = None
    with_deleted: bool = True


class PaymentAuthorizeModel(BaseModel):
    payment_ids: list[str]


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


### TRANSFERS MODELS STARTS


class TransferCreationModel(BaseModel):
    source_account_id: str
    destination_account_id: str
    currency: CurrencyEnum = CurrencyEnum.KES
    amount: float
    reason: str = Field(default_factory=lambda: faker.sentence(nb_words=10))
    unique_request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))


### REFERENCE MODELS STARTS
class BeneficiaryPaymentRequirementModel(BaseModel):
    currency: str = CurrencyEnum.KES
    bank_account_country: Annotated[
        str, StringConstraints(min_length=2, max_length=2)
    ] = Field(default_factory=lambda: CountryEnum.KE)
    on_behalf_of: str | None = None
    beneficiary_country: Annotated[
        str, StringConstraints(min_length=2, max_length=2)
    ] = Field(default_factory=lambda: CountryEnum.US)

    @field_validator("bank_account_country")
    @classmethod
    def validate_bank_account_country(cls, value: str, info):
        return value.upper()

    @field_validator("beneficiary_country")
    @classmethod
    def validate_beneficiary_country(cls, value: str, info):
        return value.upper()


### FOREIGN EXCHANGE STARTS
class FEchangeQueryModal(BaseModel):
    buy_currency: Annotated[str, StringConstraints(min_length=3, max_length=3)]
    sell_currency: Annotated[str, StringConstraints(min_length=3, max_length=3)]
    amount: Decimal
    fixed_side: FEchangeEnum = FEchangeEnum.BUY

    @field_validator("buy_currency")
    @classmethod
    def validate_buy_currency(cls, value: str, info):
        return value.upper()

    @field_validator("sell_currency")
    @classmethod
    def validate_sell_currency(cls, value: str, info):
        return value.upper()


class SSIFundingAccountQueryParams(PaginationParams, OrderingParams):
    payment_type: Optional[PaymentType] = Field(
        default_factory=PaymentType.regular,
        description="priority (Swift) or regular (local). None returns all.",
    )

    currency: Annotated[
        CurrencyEnum,
        StringConstraints(
            max_length=3, min_length=3, strip_whitespace=True, to_upper=True
        ),
    ] = Field(default=CurrencyEnum.KES, description="ISO 4217 currency code")

    account_id: Optional[str] = None
    on_behalf_of: Optional[str] = None


class InboundFundingRequest(BaseModel):
    id: uuid.UUID = Field(default=uuid.uuid4, description="Transaction id")
    receiver_account_number: str = Field(
        ..., description="Client virtual or sub-account number"
    )
    amount: float = Field(..., gt=0, description="Transaction amount")
    currency: Annotated[
        CurrencyEnum,
        StringConstraints(
            max_length=3, min_length=3, strip_whitespace=True, to_upper=True
        ),
    ] = Field(default=CurrencyEnum.KES, description="ISO 4217 currency code")

    sender_name: Optional[str] = Field(None, description="Sender's name")
    sender_address: Optional[str] = Field(None, description="Sender's address")
    sender_country: Annotated[
        CountryEnum,
        StringConstraints(
            max_length=2, min_length=2, strip_whitespace=True, to_upper=True
        ),
    ] = Field(default=CountryEnum.KE, description="ISO 2-letter country code")

    sender_reference: Optional[str] = Field(None, description="Sender reference")
    sender_account_number: Optional[str] = Field(
        None, description="Sender account number"
    )
    sender_routing_code: Optional[str] = Field(None, description="Sender routing code")

    receiver_routing_code: Optional[str] = Field(
        None, description="Receiver routing code"
    )

    action: Optional[FundingAction] = Field(
        None, description="Approve or reject emulated transaction"
    )
    on_behalf_of: uuid.UUID = Field(
        ..., description="Contact UUID when acting on behalf of sub-account"
    )

