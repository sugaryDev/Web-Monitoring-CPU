import flask
from flask import Blueprint, abort, request
from service.monitoring_service import MonitoringService
from database.database import Database as db

blueprint: Blueprint = Blueprint("server", __name__)

database: db = db("test.db")


@blueprint.get("/usage/<core>")
def core_utilization(core: str):
    per = request.args.get('per', default=3600)
    if core == "all":
        return database.select(per)
    if 1 <= int(core) <= MonitoringService.NUMBER_OF_CORES:
        return "1234"
    abort(400, "Bad Request")
