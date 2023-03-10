# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class StreamReadRequestBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    StreamReadRequestBody - a model defined in OpenAPI

        manifest: The manifest of this StreamReadRequestBody.
        stream: The stream of this StreamReadRequestBody.
        config: The config of this StreamReadRequestBody.
        state: The state of this StreamReadRequestBody [Optional].
        record_limit: The record_limit of this StreamReadRequestBody [Optional].
    """

    manifest: Dict[str, Any]
    stream: str
    config: Dict[str, Any]
    state: Optional[Dict[str, Any]] = None
    record_limit: Optional[int] = None

    @validator("record_limit")
    def record_limit_max(cls, value):
        assert value <= 1000
        return value

    @validator("record_limit")
    def record_limit_min(cls, value):
        assert value >= 1
        return value

StreamReadRequestBody.update_forward_refs()
