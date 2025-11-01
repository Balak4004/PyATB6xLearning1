


def validate_status_code(response_code):
    if response_code == 200:
        print("Request is successful")
    else:
        print("Error")

validate_status_code(404)
validate_status_code(200)

