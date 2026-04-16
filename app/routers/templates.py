from fastapi import APIRouter
from app.templates.templates import TEMPLATES

router = APIRouter(prefix="/templates", tags=["Templates"])

@router.get("")
def list_templates():
    return [
        {
            "key": key,
            "name": key.replace("_", " ").title(),
            "canvas": tpl["canvas"],
            "element_count": len(tpl["elements"]),
        }
        for key, tpl in TEMPLATES.items()
    ]

@router.get("/{key}")
def get_template(key: str):
    if key not in TEMPLATES:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Template not found")
    return TEMPLATES[key]