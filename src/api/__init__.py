from __future__ import annotations

from flask import Blueprint

api = Blueprint("api", __name__)

from . import inference  # noqa
