from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import urlshortener.models
from urlshortener.database import SessionLocal, engine
from urlshortener.queries import (create_url, create_url_stat,
                                  get_url_by_short_url, get_url_by_url,
                                  get_url_stat)
from urlshortener.schemas import UrlSchema
from urlshortener.utils import generate_short_url

# Create db tables
urlshortener.models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener"
)


# db session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten")
def shorten_url(request: UrlSchema, db: Session = Depends(get_db)):
    """
    Path operation to generate a short url
    """
    # Look if url is in db table
    url_query = get_url_by_url(db, request.url)

    if url_query is not None:
        return url_query.short_url

    # Add url to db, generate short url
    new_url = create_url(db, request.url, "")
    short_url = generate_short_url(new_url.id)
    new_url.short_url = short_url
    db.commit()
    
    # Create entry on stats table
    create_url_stat(db, new_url.id)

    return new_url.short_url


@app.get("/translate")
def get_long_url(url: str, db: Session = Depends(get_db)):
    """
    Retrieves the long url of a given short url
    """
    url_query = get_url_by_short_url(db, url)

    if url_query is None:
        raise HTTPException(status_code=404, detail="Url not found")
    
    # Increment number of visits for url
    url_stat = get_url_stat(db, url_query.id)
    url_stat.visits += 1
    db.commit()

    return url_query.url
