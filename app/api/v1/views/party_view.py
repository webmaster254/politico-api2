from flask import Blueprint, jsonify, request
from app.api.v1.models.party_model import PParties

B = Blueprint("v1_base", __name__, url_prefix="/api/v1")


@B.route("/parties", methods=["POST"])
def parties():
    """
        Create a political party - POST
    """
    custom_response = None
    if request.method == "POST":
        party_reg_data = request.get_json(force=True)
        sample_party = PParties(party_reg_data)
        if len(party_reg_data) > 4:
            custom_response = jsonify({
                "status": "404",
                "error": "More data fields than expected"
            }), 400
        elif len(party_reg_data) < 4:
            custom_response = jsonify({
                "status": "404",
                "error": "Fewer data fields than expected"
            }), 400
        elif sample_party.check_for_expected_value_types() is False:
            custom_response = jsonify({
                "status": "404",
                "error": "Invalid value in data field"
            }), 422
        elif sample_party.check_for_any_empty_fields() is False:
            custom_response = jsonify({
                "status": "404",
                "error": "Empty data field"
            }), 422
            else:
                custom_response = jsonify(sample_party.create_party()), 201

    elif request.method == "GET":
        custom_response = jsonify(PParties.get_all_parties())

    else:
        pass

    return custom_response


@B.route("/parties/<int:pid>", methods=["GET"])
def party(pid):
    """
    GET -> Fetch political party by ID
    """
    custom_response = None

    if request.method == "GET":

        if isinstance(pid, int) and pid >= 1:
            if PParties.check_id_exists(pid) is True:
                custom_response = jsonify({
                    "status": 200,
                    "data": PParties.fetch_a_party(pid)
                }), 200
            else:
                custom_response = jsonify({
                    "status": 416,
                    "error": "ID out of range. Requested Range Not Satisfiable"
                }), 416
        elif pid < 1:
            custom_response = jsonify({
                "status": "Failed",
                "error": "ID cannot be zero or negative"
            }), 400
    else:
        pass

    return custom_response


@B.route("/parties/<int:pid>/name", methods=["PATCH"])
def party_Admin(pid):
    """ Edit politcal party  name by ID"""
    custom_response = None
    party_updates = request.get_json(force=True)

    if "name" not in party_updates or len(party_updates) != 1:
        custom_response = jsonify({
            "status": 400,
            "error": "Bad Query - More data fields than expected"
        }), 400
    elif pid < 1:
        custom_response = jsonify({
            "status": "Failed",
            "error": "ID cannot be zero"
        }), 400
    elif PParties.check_id_exists(pid) is False:
        custom_response = jsonify({
            "status": 416,
            "error": "ID out of range. Requested Range Not Satisfiable"
        }), 416

    elif PParties.check_for_valid_party_name(party_updates["name"]):
        custom_response = jsonify({
            "status": 422,
            "error": "Name cannot be empty/space or 1 letter",
            }), 422

    else:
        custom_response = jsonify({
            "status": 200,
            "data": PParties.edit_party(party_updates, pid)
            }), 200

    return custom_response