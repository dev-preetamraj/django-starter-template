import logging

from rest_framework.response import Response
from rest_framework import status

from accounts.helpers.query_helpers.users_q_helper import register_user_q
from core.utils import custom_exceptions as ce
from core.utils.custom_response import CustomResponse

# Get an instance of logger
logger = logging.getLogger('accounts')

response = CustomResponse()

def register_user_fn(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if username is None:
            return response.error(status.HTTP_400_BAD_REQUEST, None, 'Username cannot be empty') # Check for any validity like if username already exists
        
        user = register_user_q(request.data)
        if user is None:
            return response.error(
                status.HTTP_400_BAD_REQUEST,
                None,
                'Something went wrong'
            )
        
        return response.success(
            status.HTTP_201_CREATED,
            None,
            'User registered successfully'
        )
    except Exception as e:
        logger.error(f'USERS FUNCTION HELPER - USERS: {e}')
        raise ce.InternalServerError