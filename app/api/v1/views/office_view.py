from flask import Blueprint, jsonify, request
from app.api.v1.model_office import POffices

OF = Blueprint("v1_office", __name__, url_prefix="/api/v1")


@OF.route("/offices", methods=["POST"])
def offices():
    """ Create a political party - POST """
    custom_response = None
    if request.method == "POST":
        office_reg_data = request.get_json(force=True)
        sample_office = POffices(office_reg_data)
        # Check for no. of dict items
        if len(office_reg_data) > 2:
            custom_response = jsonify({
                "status": 400,
                "error": "Bad Query - More data fields than expected"
            }), 400
        elif len(office_reg_data) < 2:
            custom_response = jsonify({
                "status": 400,
                "error": "Bad Query - Fewer data fields than expected"
            }), 400

        elif sample_office.check_for_expected_keys_present(
                ["name", "type"]) is False:
            custom_response = jsonify({
                "status": 422,
                "error": "Unprocessable Entity - Invalid value in data field"
            }), 422
        elif sample_office.check_for_expected_type_of_office(
                ["Federal", "Legislative", "State", "Local Government"]
                ) is False:
            custom_response = jsonify({
                "status": 422,
                "error": "Unprocessable Entity - Invalid value in data field"
            }), 422
        elif sample_office.check_any_for_empty_fields() is False:
            custom_response = jsonify({
                "status": 422,
                "error": "Unprocessable Entity - Invalid value in data field"
            }), 422
        elif sample_office.check_whether_office_exists(
                office_reg_data["name"]) is True:
            custom_response = jsonify({
                "status": 409,
                "error": "Conflict - Office already exists"
            }), 409
        else:
            custom_response = jsonify(sample_office.create_office()), 201

    else:
        pass

    return custom_response