from rest_framework.response import Response
from typing import Any


class CustomResponse:
    def __init__(self) -> None:
        pass

    def success(self, status_code: int, data: Any, message: str):
        return Response({
            'success': True,
            'status_code': status_code,
            'data': data,
            'message': message
        }, status=status_code)
    
    def error(self, status_code: int, data: Any, message: str):
        return Response({
            'success': False,
            'status_code': status_code,
            'data': data,
            'message': message
        }, status=status_code)