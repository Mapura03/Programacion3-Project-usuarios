from fastapi import APIRouter, HTTPException, status, Depends
from model.typedoc import TypeDoc
from service.typedoc_service import TypeDocService, get_typedoc_service
from typing import List

router = APIRouter()

@router.get("/typedocs", response_model=List[TypeDoc])
def list_typedocs(service: TypeDocService = Depends(get_typedoc_service)) -> List[TypeDoc]:
    return service.get_all_typedocs()


@router.post("/typedocs", response_model=TypeDoc, status_code=status.HTTP_201_CREATED)
def create_typedoc(typedoc: TypeDoc, service: TypeDocService = Depends(get_typedoc_service)) -> TypeDoc:
    return service.create_typedoc(typedoc)