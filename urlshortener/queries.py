from sqlalchemy.orm import Session

from urlshortener.models import Url, UrlStats


def get_url_by_url(db: Session, url: str) -> Url:
    return db.query(Url).filter(Url.url == url).first()


def create_url(db: Session, url: str, short_url: str) -> Url:
    db_url = Url(url=url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_url_by_short_url(db: Session, short_url: str) -> Url:
    return db.query(Url).filter(Url.short_url == short_url).first()


def create_url_stat(db: Session, url_id: int) -> UrlStats:
    db_url_stat = UrlStats(url_id=url_id, visits=0)
    db.add(db_url_stat)
    db.commit()
    db.refresh(db_url_stat)
    return db_url_stat


def get_url_stat(db: Session, url_id: int) -> UrlStats:
    return db.query(UrlStats).filter(UrlStats.url_id == url_id).first()
