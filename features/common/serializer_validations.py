from rest_framework.response import Response
from rest_framework import status

class SerializerValidations:
    def __init__(self, serializer=None, exec_func=None):
        self.serializer = serializer
        self.exec_func = exec_func

    def validate(self, func):
        def wrapper(*args, **kwargs):
            request = args[0]  # the request object
            if self.serializer:
                serializer_instance = self.serializer(data=getattr(request, 'data', {}))
                serializer_instance.is_valid(raise_exception=True)
                request.params = serializer_instance.save() if hasattr(serializer_instance, 'save') else serializer_instance.validated_data
            else:
                request.params = getattr(request, 'data', {})
            # exec_func can be used later if needed
            return func(*args, **kwargs)
        return wrapper
