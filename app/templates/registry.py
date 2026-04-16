"""Template registry - thin wrapper used by routers."""
from app.templates.templates import TEMPLATES

def get_template_list():
    return [
        {
            "key": key,
            "name": key.replace("_", " ").title(),
            "canvas": tpl["canvas"],
            "preview_elements": tpl["elements"][:2],
        }
        for key, tpl in TEMPLATES.items()
    ]

def get_template(key: str):
    return TEMPLATES.get(key)