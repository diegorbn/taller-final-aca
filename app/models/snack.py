from pydantic import BaseModel, Field


class SnackCreate(BaseModel):
    """
    Data required to create a new snack.
    """

    name: str = Field(
        min_length=2,
        max_length=50,
        examples=["Moon Cheese"]
    )
    price: float = Field(
        gt=0,
        examples=[4.99]
    )
    planet_of_origin: str = Field(
        min_length=2,
        max_length=50,
        examples=["The Moon"]
    )
    is_radioactive: bool = False


class Snack(SnackCreate):
    """
    Complete snack representation, including its identifier.
    """

    id: int