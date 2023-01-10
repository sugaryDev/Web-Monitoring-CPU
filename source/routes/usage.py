from dataclasses import asdict
from flask import Blueprint, request, jsonify
from models import Utilization
from database import UsageDAL
import cash
blueprint: Blueprint = Blueprint("usage", __name__, url_prefix="/usage")
a = aaa.acquire_connection()
database: UsageDAL = UsageDAL(a)


@blueprint.get("/<int:core>")
def core_utilization(core: int):
    per = int(request.args.get('per', default=3600))

    data = database.select(per)

    response = Utilization(
        core=core,
        usage=[list(map(float, x.usage.split())) for x in data][core - 1],
        per=per
    )
    return jsonify(asdict(response))


@blueprint.get("/all")
def all_utilization():
    per = int(request.args.get('per', default=3600))
    data = database.select(per)

    response = Utilization(
        core="all",
        usage=[list(map(float, x.usage.split())) for x in data],
        per=per
    )
    return jsonify(asdict(response))
