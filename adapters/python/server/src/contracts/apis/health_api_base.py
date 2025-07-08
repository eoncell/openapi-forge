# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from contracts.models.error import Error
from contracts.models.get_health_status200_response import GetHealthStatus200Response


class BaseHealthApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseHealthApi.subclasses = BaseHealthApi.subclasses + (cls,)
    async def get_health_status(
        self,
    ) -> GetHealthStatus200Response:
        """Check API health status"""
        ...
