# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class HttpResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    HttpResponse - a model defined in OpenAPI

        status: The status of this HttpResponse.
        body: The body of this HttpResponse [Optional].
        headers: The headers of this HttpResponse [Optional].
    """

    status: int
    body: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, Any]] = None

HttpResponse.update_forward_refs()
