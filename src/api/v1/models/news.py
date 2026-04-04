from pydantic import BaseModel, StringConstraints, field_validator, Field
from typing import Annotated, Optional
from .choices import CountryEnum, NewsCategoryEnum, NewsFilterModelEnum


class NewsFilterModel(BaseModel):
    country: Annotated[Optional[CountryEnum], None] = None
    q: Annotated[str, StringConstraints(min_length=3)] = Field(
        description="The text to search", title="Search query",
    )
    searchIn: Annotated[
        Optional[NewsFilterModelEnum], StringConstraints(max_length=20)
    ] = Field(default_factory=lambda: str(NewsFilterModelEnum.title.value))
    pageSize: int = Field(ge=1, le=100, default=20)
    page: int = 1

    @field_validator("country")
    @classmethod
    def validate_country_field(cls, value: str):
        if value is None:
            return None
        _val = value.lower()
        if len(_val) > 2:
            raise ValueError(
                "The 2-letter ISO 3166-1 code of the country format needed."
            )
        return _val

    @field_validator("pageSize")
    @classmethod
    def validate_pageSize_field(cls, value: int):
        return int(value)


class TopNewsFilterModel(BaseModel):
    country: Annotated[CountryEnum, StringConstraints(min_length=2, max_length=2)] = (
        Field(default_factory=lambda: CountryEnum.US.value)
    )
    category: Annotated[
        Optional[NewsCategoryEnum], StringConstraints(max_length=20)
    ] = Field(default_factory=lambda: str(NewsCategoryEnum.health.value))

    q: str | None = None
    pageSize: int = Field(ge=1, le=100, default=20)
    page: int = 1

    @field_validator("country")
    @classmethod
    def validate_country_field(cls, value: str):
        _val = value.lower()
        if len(_val) > 2:
            raise ValueError(
                "The 2-letter ISO 3166-1 code of the country format needed."
            )
        return _val

    @field_validator("pageSize")
    @classmethod
    def validate_pageSize_field(cls, value: int):
        return int(value)
