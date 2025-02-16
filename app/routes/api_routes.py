from flask import Blueprint, Response, jsonify
from app.services.platform_service import PlatformService
from app.services.general_service import GeneralService

bp = Blueprint("api", __name__)


@bp.route("/")
def home() -> Response:
    return jsonify(
        {
            "name": "Davi Wiliam",
            "email": "daviwil42@gmail.com",
            "linkedin": "https://linkedin.com/in/daviwiliam",
        }
    )


@bp.route("/<platform>")
def platform_data(platform: str) -> Response:

    csv = PlatformService.get_platform_data(platform)

    if csv:
        return Response(csv, mimetype="text/csv")
    else:
        return jsonify({"error": "Nenhum dado encontrado"}), 404


@bp.route("/<platform>/resumo")
def resume_platform_data(platform: str) -> Response:

    resume = True

    csv = PlatformService.get_platform_data(platform, resume)

    if csv:
        return Response(csv, mimetype="text/csv")
    else:
        return jsonify({"error": "Nenhum dado encontrado"}), 404


@bp.route("/geral")
def geral_data() -> Response:

    csv = GeneralService.get_general_data()

    if csv:
        return Response(csv, mimetype="text/csv")
    else:
        return jsonify({"error": "Nenhum dado encontrado"}), 404


@bp.route("/geral/resumo")
def resume_geral_data() -> Response:

    resume = True

    csv = GeneralService.get_general_data(resume)

    if csv:
        return Response(csv, mimetype="text/csv")
    else:
        return jsonify({"error": "Nenhum dado encontrado"}), 404


@bp.route("/favicon.ico")
def favicon():
    return "", 204

