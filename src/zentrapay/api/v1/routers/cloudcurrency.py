
from fastapi import APIRouter
from .currencycloud import (
    account_router,
    balances_router,
    contacts_router,
    beneficiaries_router,
    transactions_router,
    payments_router,
    transfers_router,
    references_router,
    fx_router,
    funding_router
)


router = APIRouter(prefix="/currencycloud")

## ------------------------------------------------------
### ACCOUNT RELATED PATHS
## ------------------------------------------------------
router.include_router(account_router, tags=["Accounts"])

## ------------------------------------------------------
### BALANCE RELATED PATHS
## ------------------------------------------------------
router.include_router(balances_router, tags=["Balances"])


## ------------------------------------------------------
### CONTACT MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(contacts_router, tags=["Contacts"])


## ------------------------------------------------------
### Beneficiary MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(beneficiaries_router, tags=["Beneficiaries"])

## ------------------------------------------------------
### TRANSACTION MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(transactions_router, tags=["Transactions"])


## ------------------------------------------------------
### FUNDING HANDLING PATHS
## ------------------------------------------------------
router.include_router(funding_router, tags=["Funding"])

## ------------------------------------------------------
### PAYMENT MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(payments_router, tags=["Payments"])

## ------------------------------------------------------
### TRANSFERS MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(transfers_router, tags=["Transfers"])


## ------------------------------------------------------
### REFERENCES MANAGEMENT PATHS
## ------------------------------------------------------
router.include_router(references_router, tags=["References"])

## ------------------------------------------------------
### Foreign Exchange Rates PATHS
## ------------------------------------------------------
router.include_router(fx_router, tags=["Foreign Exchange Rates"])

