from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette import status
from database_settings import SessionDep
from models import Missions, Cats, Targets
from schemas import CatCreateSchema
from sqlalchemy.orm import selectinload


router = APIRouter(prefix="/agency", tags=["agency"])


@router.post('/mission/create', status_code=status.HTTP_201_CREATED)
async def mission_create(schema: CatCreateSchema, session: SessionDep):
    """create a mission"""

    if schema.cat_id:
        result = await session.execute(select(Cats).options(selectinload(Cats.mission)).where(Cats.id == schema.cat_id))
        cat = result.scalar_one_or_none()

        if not cat:
            raise HTTPException(status_code=404, detail="Cat doesn't exist")

        if cat.mission:
            raise HTTPException(status_code=400, detail='The cat is already on a mission')
    
    mission = Missions(
        cat_id=schema.cat_id,
        targets=[
            Targets(
                name=target.name,
                country=target.country,
                notes=target.notes or ''
            ) for target in schema.targets
        ]
    )

    session.add(mission)
    await session.commit()

@router.delete('/mission/delete/{mission_id}', status_code=status.HTTP_204_NO_CONTENT)
async def mission_delete(mission_id: int, session: SessionDep):
    """delete mission"""

    result = await session.get(Missions, mission_id)

    if not result:
        raise HTTPException(status_code=404, detail="Mission not found")

    elif result.cat_id:
        raise HTTPException(status_code=400, detail="Mission is assigned to a cat and cannot be deleted")

    await session.delete(result)
    await session.commit()



@router.get('/mission/all', status_code=status.HTTP_200_OK)
async def all_missions(session: SessionDep):
    """get all missions"""
    result = await session.execute(select(Missions).options(selectinload(Missions.targets)))
    missions_list = result.scalars().all()
    return {"missions": [{"id": c.id, "cat_id": c.cat_id, "complete status": c.complete, "targets": [{"id": v.id, "name": v.name, "country": v.country, "notes": v.notes, "complete status": v.complete} 
          for v in c.targets]} for c in missions_list]}



@router.get('/mission/id/{mission_id}', status_code=status.HTTP_200_OK)
async def get_mission_by_id(mission_id: int, session: SessionDep):
    """get a single mission"""
    result = await session.execute(select(Missions).options(selectinload(Missions.targets)).where(Missions.id == mission_id))
    mission = result.scalar_one_or_none()
    
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    
    return {"mission": {"id": mission.id, "cat_id": mission.cat_id, "status": mission.complete, "targets": 
        [{"id": v.id, "name": v.name, "country": v.country, "notes": v.notes, "complete status": v.complete} for v in mission.targets]
        }}



@router.patch('/mission/{mission_id}/change/status', status_code=status.HTTP_200_OK)
async def change_mission_status(mission_id: int, session: SessionDep):
    """change mission status to complete"""
    result = await session.get(Missions, mission_id)

    if not result:
        raise HTTPException(status_code=404, detail="Mission not found")

    if result.complete:
        raise HTTPException(status_code=400, detail="Mission is already completed")

    result.complete = True
    await session.commit()

    return {"message": "Mission marked as complete"}