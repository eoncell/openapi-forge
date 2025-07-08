# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from contracts.apis.health_api_base import BaseHealthApi
import contracts.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from contracts.models.extra_models import TokenModel  # noqa: F401
from contracts.models.error import Error
from contracts.models.get_health_status200_response import GetHealthStatus200Response


router = APIRouter()

ns_pkg = contracts.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/health",
    responses={
        200: {"model": GetHealthStatus200Response, "description": "Service is healthy"},
        500: {"model": Error, "description": "Internal server error"},
    },
    tags=["Health"],
    summary="Health check",
    response_model_by_alias=True,
)
async def get_health_status(
) -> GetHealthStatus200Response:
    """Check API health status"""
    if not BaseHealthApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseHealthApi.subclasses[0]().get_health_status()
