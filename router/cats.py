from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette import status

from database_settings import SessionDep
from models import Cats, Targets, Missions
from schemas import CatSchema, CatSalaryShema, MissionTargetPatchSchema
from services import breeds_validation

router = APIRouter(prefix="/cats", tags=["cats"])

@router.get('/all', status_code=status.HTTP_200_OK)
async def all_cats(session: SessionDep):
    """get all cats"""
    result = await session.execute(select(Cats))
    cats_list = result.scalars().all()
    return {"cats": [{"name": c.name, "experience": c.experience, "breed": c.breed, "salary": c.salary} for c in cats_list]}



@router.get('/check/name/{cat_name}', status_code=status.HTTP_200_OK)
async def get_by_name(session: SessionDep, cat_name: str):
    """Get cats by name (can return multiple)"""

    result = await session.execute(select(Cats).where(Cats.name == cat_name))
    cats_list = result.scalars().all()

    if not cats_list:
        raise HTTPException(status_code=404, detail="No cats found with this name")

    return {"cats": [{"id": c.id, "name": c.name, "experience": c.experience, "breed": c.breed, "salary": c.salary} for c in cats_list]}


@router.get('/check/id/{cat_id}', status_code=status.HTTP_200_OK)
async def get_by_id(session: SessionDep, cat_id: int):
    """Get cat by ID (returns single cat)"""

    result = await session.execute(select(Cats).where(Cats.id == cat_id))
    cat = result.scalar_one_or_none()

    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    return {"cat": {"id": cat.id, "name": cat.name, "experience": cat.experience, "breed": cat.breed, "salary": cat.salary}}



@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_cat(schema: CatSchema, session: SessionDep):
    """create a new cat"""
    try:
        if await breeds_validation(schema.breed) is True:
            new_cat = Cats(**schema.dict())
            session.add(new_cat)
            await session.commit()
            return {"message": 'success'}

        raise HTTPException(status_code=400, detail="Breed doesnt exists. Look docs to choose from.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.delete('/delete/{cat_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cat(session: SessionDep, cat_id: int):
    """Deletes cat by Id"""

    result = await session.execute(select(Cats).where(Cats.id == cat_id))
    cat = result.scalar_one_or_none()

    if not cat:
        raise HTTPException(status_code=404, detail='Cat not found')
    
    await session.delete(cat)
    await session.commit()
    return None



@router.patch('/update-salary/{cat_id}', status_code=status.HTTP_200_OK)
async def patch_cat(schema: CatSalaryShema, cat_id: int, session:SessionDep):
    """Updates field: salary """
    cat = await session.get(Cats, cat_id)

    if not cat:
        raise HTTPException(status_code=404, detail='Cat not found')


    cat.salary = schema.salary
    await session.commit()
    return {"message": "success"}