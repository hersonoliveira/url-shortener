# URL Shortener

A simple API to generate short URLS

## Features

- Two endpoints: To shorten a long URL and other to retrive the long URL from a short one
- Each URL has an unique identifier, which is converted to base 62 and form the unique short URL hash
- SQLite database; URL stats table to track the number of visits


## Run locally

Create a new python virtual environment and install the dependencies

```bash
$ python -m venv venv
$ python -m pip install -r requirements.txt
```

Start the server

```bash
$ uvicorn urlshortener.main:app --reload
```

## Running Tests

To run tests, run the following command

```bash
$ python -m pytest
```

## API Reference

#### Shorten URL

```http
  POST /shorten
```

##### Request body
```
{
  "url": "www.yourlongurl.com"
}
```

#### Get long URL

```http
  GET /translate
```

| Query Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url`      | `string` | **Required**. short URL |
