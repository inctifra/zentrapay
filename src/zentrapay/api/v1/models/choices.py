from enum import Enum


class CountryEnum(str, Enum):
    KE = "KE"
    US = "US"
    UK = "UK"


class AccountLegalEntityType(Enum):
    COMPANY = "company"
    INDIVIDUAL = "individual"

class CustomerRiskEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    

class AccountOrderFilterEnum(str, Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class AccountStatusFilterEnum(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    ENABLED_NO_TRADING = "enabled_no_trading"


class ContactStatusEnum(str, Enum):
    ENABLED = "enabled"
    DISABLED = "not_enabled"

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

class CurrencyEnum(str, Enum):
    KES = "KES"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"

class PaymentReviewStatusEnum(str, Enum):
    IN_REVIEW = "in_review"
    PASSED = "passed"
    REJECTED = "rejected"




class NewsCategoryEnum(str, Enum):
    business = "business"
    entertainment = "entertainment"
    general = "general"
    health = "health"
    science = "science"
    sports = "sports"
    technology = "technology"


class NewsFilterModelEnum(str, Enum):
    title = "title"
    description = "description"
    content = "content"

class FEchangeEnum(str, Enum):
    BUY="buy"
    SELL="sell"