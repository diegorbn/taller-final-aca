from fastapi import APIRouter, HTTPException, Query, status

from app.data.snacks import snacks_db
from app.models.snack import Snack, SnackCreate

router = APIRouter(
    prefix="/snacks",
    tags=["Snacks"],
)


@router.get("/", response_model=list[Snack])
def get_snacks(
    radioactive: bool | None = Query(
        default=None,
        description="Filter snacks by radioactive status."
    )
):
    """
    Return all available snacks.

    Optionally, filter them according to whether they are radioactive.
    """
    if radioactive is None:
        return snacks_db

    return [
        snack
        for snack in snacks_db
        if snack["is_radioactive"] == radioactive
    ]


@router.get("/{snack_id}", response_model=Snack)
def get_snack(snack_id: int):
    """
    Return a snack by its identifier.
    """
    for snack in snacks_db:
        if snack["id"] == snack_id:
            return snack

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Snack not found. An alien may have eaten it.",
    )


@router.post(
    "/",
    response_model=Snack,
    status_code=status.HTTP_201_CREATED,
)
def create_snack(snack: SnackCreate):
    """
    Create a new intergalactic snack.
    """
    new_id = max(
        (existing_snack["id"] for existing_snack in snacks_db),
        default=0,
    ) + 1

    new_snack = {
        "id": new_id,
        **snack.model_dump(),
    }

    snacks_db.append(new_snack)

    return new_snack


@router.put("/{snack_id}", response_model=Snack)
def update_snack(snack_id: int, updated_snack: SnackCreate):
    """
    Replace the information of an existing snack.
    """
    for index, snack in enumerate(snacks_db):
        if snack["id"] == snack_id:
            snack_data = {
                "id": snack_id,
                **updated_snack.model_dump(),
            }

            snacks_db[index] = snack_data
            return snack_data

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Snack not found. It may be orbiting another planet.",
    )


@router.delete("/{snack_id}")
def delete_snack(snack_id: int):
    """
    Delete a snack by its identifier.
    """
    for index, snack in enumerate(snacks_db):
        if snack["id"] == snack_id:
            deleted_snack = snacks_db.pop(index)

            return {
                "message": f"{deleted_snack['name']} was launched into space."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Snack not found. Nothing was launched.",
    )