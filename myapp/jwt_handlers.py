def jwt_response_payload_handler(token, user=None, request=None):
    if user.is_superuser:
        user_type = 'admin'
    elif user.is_staff:
        user_type = 'staff'
    else:
        user_type = None
    return {
        'token': token,
        'user_type': user_type
    }