import uuid
import copy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.project import Project
from app.models.user import User
from app.templates.templates import TEMPLATES

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("")
def list_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return all projects for the authenticated user, newest first."""
    projects = (
        db.query(Project)
        .filter(Project.user_id == current_user.id)
        .order_by(Project.updated_at.desc())
        .all()
    )
    return [
        {
            "id": str(p.id),
            "name": p.name,
            "template_id": p.template_id,
            "is_active": p.is_active,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "updated_at": p.updated_at.isoformat() if p.updated_at else None,
        }
        for p in projects
    ]


@router.get("/{project_id}")
def get_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "id": str(project.id),
        "name": project.name,
        "template_id": project.template_id,
        "data": project.design_data,
        "is_active": project.is_active,
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
    }


@router.post("")
def create_project(
    payload: dict,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    template_id = payload.get("template_id")
    name = payload.get("name", "Untitled Invitation")

    if template_id not in TEMPLATES:
        raise HTTPException(status_code=400, detail=f"Invalid template '{template_id}'")

    project = Project(
        id=uuid.uuid4(),
        user_id=user.id,
        template_id=template_id,
        name=name,
        design_data=copy.deepcopy(TEMPLATES[template_id]),
        is_active=False,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return {
        "project_id": str(project.id),
        "name": project.name,
        "template_id": project.template_id,
    }


@router.put("/{project_id}")
def save_project(
    project_id: UUID,
    payload: dict,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == user.id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if "data" in payload:
        project.design_data = payload["data"]
    if "name" in payload:
        project.name = payload["name"]

    db.commit()
    db.refresh(project)
    return {
        "status": "saved",
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
    }


@router.delete("/{project_id}")
def delete_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == user.id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"status": "deleted"}


@router.post("/{project_id}/duplicate")
def duplicate_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Duplicate an existing project."""
    source = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == user.id)
        .first()
    )
    if not source:
        raise HTTPException(status_code=404, detail="Project not found")

    new_project = Project(
        id=uuid.uuid4(),
        user_id=user.id,
        template_id=source.template_id,
        name=f"{source.name} (Copy)",
        design_data=copy.deepcopy(source.design_data),
        is_active=False,
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return {"project_id": str(new_project.id), "name": new_project.name}