"""
Corrects documentation
"""
from fastapi.openapi.utils import get_openapi


def custom_openapi(app):
    """
    Change the produced documentation
    :param app:
    :return: the openapi doc
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Iris Dataset Exploration API',
        description='',
        routes=app.routes,
        version='1.0'
    )
    openapi_schema["components"]["lower"].update({'example': {"sepal_length": 5.0, "sepal_width": 3.0}})
    app.openapi_schema = openapi_schema
    return app.openapi_schema
