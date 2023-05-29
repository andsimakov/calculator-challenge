# Calculator Challenge project

## Requirements
* Python 3.11.2
* FastAPI
* uvicorn
* pytest
* httpx

* See also `api/requirements.txt`.

## Client

The client page is in `client/index.html`.

## API Documentation

API documentation is available at http://127.0.0.1:8000/docs#/.

## API Request Examples

API endpoint `calculations` valid request body examples:
```json
{
    "operands": [3, 4],
    "operators": ["+"]
}
```

```json
{
     "operands": [3, 4, 2, 1, 5, 2],
     "operators": ["+", "-", "/", "+", "*"]
}
```

## Colored Response

To get a color coding in a response please add to request headers `pass-color: True`.
