from sqlalchemy import Column, Integer, String, ForeignKey
from urlshortener.database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    short_url = Column(String, unique=True, index=True)


class UrlStats(Base):
    __tablename__ = "urlstats"

    id = Column(Integer, primary_key=True, index=True)
    url_id = Column(Integer, ForeignKey("urls.id"), index=True)
    visits = Column(Integer)
