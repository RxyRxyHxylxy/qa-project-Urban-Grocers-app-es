import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def get_new_user_token():
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    v_auth_token = new_user.json()['authToken']
    auth_token_test = data.headers.copy()
    auth_token_test["Authorization"] = "Bearer " + v_auth_token
    return auth_token_test



def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name


def negative_assert(kit_name):
    if kit_name != {}:
        kit_body = get_kit_body(kit_name)
    else:
        kit_body = kit_name
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400



def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.test_one_character)


def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.test_five_hundred_eleven_character)


def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert(data.test_zero_character)


def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(data.test_five_hundred_twelve_character)


def test_create_kit_special_caracter_in_name_get_success_response():
    positive_assert(data.test_special_character)


def test_create_kit_space_caracter_in_name_get_success_response():
    positive_assert(data.test_space_character)


def test_create_kit_number_caracter_in_name_get_success_response():
    positive_assert(data.test_number_character)


def test_create_kit_no_parameter_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop(data.test_empty_parameter)
    negative_assert(kit_body)


def test_create_kit_number_type_name_get_error_response():
    negative_assert(data.test_wrong_type_parameter)

