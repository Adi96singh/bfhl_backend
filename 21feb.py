from flask import Flask, request, jsonify

app = Flask(__name__)

# User details
USER_ID = "aditya_singh_17012004"
EMAIL_ID = "22bcs14973@cuchd.in"
ROLL_NUMBER = "22bcs14973"

@app.route("/bfhl", methods=["POST"])
def process_data():
    try:
        data = request.get_json()
        
        if not data or "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        input_list = data["data"]
        numbers = [x for x in input_list if x.isdigit()]
        alphabets = [x for x in input_list if x.isalpha()]
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL_ID,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


@app.route("/bfhl", methods=["GET"])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200


if __name__ == "__main__":
    app.run(debug=True)
