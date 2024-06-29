import logging


# Get an instance of logger
logger = logging.getLogger('accounts')

def register_user_q(data):
    try:
        user = None # do some query
        return user
    except Exception as e:
        logger.error(f'USERS QUERY HELPER REGISTER USER QUERY: {e}')
        return None