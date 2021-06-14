from pydantic import BaseModel


class UrlSchema(BaseModel):
    """
    URL schema to be used as request body
    """
    url: str
