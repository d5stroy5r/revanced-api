"""
This module provides a blueprint for the donations endpoint.

Routes:
    - GET /donations: Get ReVanced donation links and wallets.
"""

from sanic import Blueprint, Request
from sanic.response import JSONResponse, json
from sanic_ext import openapi

from api.models.donations import DonationsResponseModel
from config import wallets, links
from api.utils.versioning import get_version

module_name = "donations"
donations: Blueprint = Blueprint(module_name, version=get_version(module_name))


@donations.get("/donations")
@openapi.definition(
    summary="Get ReVanced donation links and wallets",
    response=[DonationsResponseModel],
)
async def root(request: Request) -> JSONResponse:
    """
    Returns a JSONResponse with a dictionary containing ReVanced donation links and wallets.

    **Returns:**
        - JSONResponse: A Sanic JSONResponse instance containing a dictionary with the donation links and wallets.
    """
    data: dict[str, dict] = {
        "donations": {
            "wallets": wallets,
            "links": links,
        }
    }
    return json(data, status=200)
