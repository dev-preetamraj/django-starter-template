import logging

from rest_framework.views import APIView
from rest_framework.versioning import NamespaceVersioning
from rest_framework.permissions import AllowAny

from accounts.helpers.function_helpers.users_fn_helper import register_user_fn
from core.utils import custom_exceptions as ce
from core.utils.custom_validators import CustomValidator

from core.common import messages as global_msg

from accounts.common import messages as app_msg

# Get an instance of logger
logger = logging.getLogger('accounts')

# Get an instance of Validator
c_validator = CustomValidator({}, allow_unknown = True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class Users(APIView):
    items_per_page = 10
    versioning_class = VersioningConfig
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            if request.version != 'v1':
                raise ce.VersionNotSupported
            
            schema = {
                'username': {
                    'required': True,
                    'empty': False,
                    'type' : 'string',
                },
                'email': {
                    'required': True,
                    'empty': False,
                    'type' : 'string',
                    'isemail': True
                },
                'password': {
                    'required': True,
                    'empty': False,
                    'type' : 'string',
                    'minlength': 8
                }
                
            }
            is_valid = c_validator.validate(request.data, schema)
            if not is_valid:
                raise ce.ValidationFailed({
                    'message': global_msg.VALIDATION_FAILED,
                    'data': c_validator.errors
                })
            
            result = register_user_fn(request)
            return result

        except ce.ValidationFailed as vf:
            logger.error(f'REGISTER USER API VIEW - POST : {vf}')
            raise

        except ce.VersionNotSupported as vns:
            logger.error(f'REGISTER USER API VIEW - POST : {vns}')
            raise

        except Exception as e:
            logger.error(f'REGISTER USER API VIEW - POST : {e}')
            raise ce.InternalServerError