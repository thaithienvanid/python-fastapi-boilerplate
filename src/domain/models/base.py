from typing import Any

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declared_attr, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass
