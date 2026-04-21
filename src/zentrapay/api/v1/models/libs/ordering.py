from enum import Enum


from typing import Optional
from pydantic import BaseModel, Field


class OrderDirection(str, Enum):
    asc = "asc"
    desc = "desc"


class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1, description="Page number")
    per_page: int = Field(default=20, ge=1, le=100, description="Items per page")


class OrderingParams(BaseModel):
    order: Optional[str] = Field(
        default=None,
        description="Field name to sort by"
    )
    order_asc_desc: OrderDirection = Field(
        default=OrderDirection.asc,
        description="Sort direction"
    )