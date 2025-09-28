from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette import status

from database_settings import SessionDep
from models import Cats, Targets, Missions
from schemas import MissionTargetPatchSchema
from services import breeds_validation
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/spies", tags=["spies"])


@router.patch('/{cat_id}/target/{target_id}', status_code=status.HTTP_200_OK)
async def spy_update_target(schema: MissionTargetPatchSchema, cat_id: int, target_id: int, session: SessionDep):
    """Update notes & Update complete status"""
    
    result = await session.execute(
        select(Targets)
        .options(selectinload(Targets.mission))
        .join(Missions)
        .join(Cats)
        .where(Targets.id == target_id)
        .where(Cats.id == cat_id)
    )
    target = result.scalar_one_or_none()
    

    if not target:
        raise HTTPException(status_code=404, detail=f"Target for cat id:{cat_id} not found")

    if target.mission.complete:
        raise HTTPException(status_code=400, detail="Mission is already completed")

    if target.complete:
        raise HTTPException(status_code=400, detail="Target is already completed")


    if schema.note:
        target.notes = schema.note

    if schema.complete:
        target.complete = schema.complete

    await session.commit()

    return {"message": "Target updated successfully"}




