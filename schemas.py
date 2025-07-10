from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class ApplicationData(BaseModel):
    id: Any
    data_type: str
    content: str
    created_at: Any


class ReadApplicationData(BaseModel):
    id: Any
    data_type: str
    content: str
    created_at: Any
    class Config:
        from_attributes = True


