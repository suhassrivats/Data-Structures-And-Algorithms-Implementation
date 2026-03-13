# Python API Client Tutorial (Headers, Bearer Tokens, Error Handling)

This guide explains how to call APIs in Python using the `GET` method, handle headers and authentication, understand HTTP status codes, and implement robust error handling.

It is intended as a practical reference for developers learning how to interact with REST APIs in production systems.

---

# 1. What Is an API Call?

An API call is an HTTP request sent from a client to a server.

Example request:

```
GET https://api.example.com/users/123
```

Structure of an HTTP request:

```
METHOD  URL
Headers
Body (optional)
```

Example response returned by the server:

```
Status Code
Headers
Body (usually JSON)
```

Example JSON response:

```json
{
  "id": 123,
  "name": "Alice"
}
```

---

# 2. HTTP Methods

APIs use HTTP methods to indicate the type of operation being performed.

| Method | Purpose          | Example        |
| ------ | ---------------- | -------------- |
| GET    | Retrieve data    | Fetch user     |
| POST   | Create resource  | Create payment |
| PUT    | Replace resource | Update user    |
| PATCH  | Partial update   | Update email   |
| DELETE | Remove resource  | Delete user    |

Example endpoints:

```
GET /users/123
POST /payments
DELETE /users/123
```

---

# 3. Headers

Headers provide metadata about the request.

Example request with headers:

```
GET /users/123
Host: api.example.com
Authorization: Bearer TOKEN
Content-Type: application/json
Accept: application/json
```

Common headers:

| Header        | Purpose                    |
| ------------- | -------------------------- |
| Authorization | Authentication credentials |
| Content-Type  | Format of request body     |
| Accept        | Expected response format   |
| User-Agent    | Client identifier          |
| X-Request-ID  | Request tracing            |

---

# 4. Bearer Token Authentication

Many APIs use **Bearer tokens** for authentication.

Format:

```
Authorization: Bearer <token>
```

Example:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Typical flow:

```
Client → Authenticate → Receive Token → Send Token in API requests
```

Example authenticated request:

```
GET /transactions
Authorization: Bearer abc123
```

---

# 5. Query Parameters

Query parameters allow filtering or pagination.

Example:

```
GET /transactions?limit=10&status=completed
```

Common uses:

| Parameter | Purpose           |
| --------- | ----------------- |
| page      | Pagination        |
| limit     | Number of results |
| sort      | Ordering results  |
| filter    | Filtering results |

Example:

```
GET /users?page=2&limit=50
```

---

# 6. Request Body

Used with `POST`, `PUT`, or `PATCH`.

Example request:

```
POST /users
```

Body:

```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

Required header:

```
Content-Type: application/json
```

---

# 7. HTTP Status Codes

Status codes indicate the result of the request.

## 2xx — Success

| Code | Meaning    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

Example:

```
POST /users → 201 Created
```

---

## 3xx — Redirects

| Code | Meaning            |
| ---- | ------------------ |
| 301  | Permanent redirect |
| 302  | Temporary redirect |

Rare in API usage.

---

## 4xx — Client Errors

These occur when the client sends an invalid request.

| Code | Meaning           | Example             |
| ---- | ----------------- | ------------------- |
| 400  | Bad Request       | Invalid JSON        |
| 401  | Unauthorized      | Missing token       |
| 403  | Forbidden         | Permission denied   |
| 404  | Not Found         | Resource missing    |
| 429  | Too Many Requests | Rate limit exceeded |

Example:

```
401 Unauthorized
```

---

## 5xx — Server Errors

Server failed to process the request.

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal server error |
| 502  | Bad gateway           |
| 503  | Service unavailable   |
| 504  | Gateway timeout       |

These are usually **safe to retry**.

---

# 8. Example Python GET Request

Below is a production-style Python example demonstrating:

* headers
* bearer token
* query parameters
* timeouts
* status code handling

```python
import requests

def get_users(page=1, limit=10):

    url = "https://api.example.com/users"

    headers = {
        "Authorization": "Bearer YOUR_TOKEN_HERE",
        "Accept": "application/json"
    }

    params = {
        "page": page,
        "limit": limit
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise Exception("Unauthorized - invalid token")

        elif response.status_code == 404:
            raise Exception("Resource not found")

        elif response.status_code >= 500:
            raise Exception("Server error")

        else:
            raise Exception(f"Unexpected status: {response.status_code}")

    except requests.exceptions.Timeout:
        raise Exception("Request timed out")

    except requests.exceptions.ConnectionError:
        raise Exception("Network connection error")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
```

---

# 9. Example Usage

```python
users = get_users(page=1, limit=5)

for user in users["data"]:
    print(user["name"])
```

---

# 10. Retry Logic

Retries should only occur for **safe failures** such as server errors or timeouts.

Example retry implementation:

```python
import requests
import time

def call_api(url, retries=3):

    for attempt in range(retries):

        try:
            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                return r.json()

            if r.status_code >= 500:
                time.sleep(2)
                continue

            raise Exception("Client error")

        except requests.exceptions.RequestException:
            time.sleep(2)

    raise Exception("API failed after retries")
```

---

# 11. Rate Limiting

Many APIs limit the number of requests.

Example response:

```
429 Too Many Requests
```

Typical headers returned:

```
X-RateLimit-Remaining: 0
Retry-After: 60
```

Clients should wait before retrying.

---

# 12. Pagination

Large datasets are usually paginated.

Example request:

```
GET /transactions?page=2&limit=50
```

Example response:

```json
{
  "data": [...],
  "next_page": 3
}
```

Client continues fetching until `next_page` is null.

---

# 13. API Debugging Tools

### Command Line

```
curl -H "Authorization: Bearer TOKEN" https://api.example.com/users
```

### GUI Tools

* Postman
* Insomnia

These tools allow you to test APIs interactively.

---

# 14. Best Practices

| Practice            | Why                      |
| ------------------- | ------------------------ |
| Always use timeouts | Prevent hanging requests |
| Handle status codes | Avoid silent failures    |
| Implement retries   | Improve reliability      |
| Log requests        | Easier debugging         |
| Use pagination      | Efficient data retrieval |

---

# 15. Key Takeaways

When implementing API calls in production code always include:

* headers and authentication
* query parameters
* timeout handling
* status code validation
* retries for server errors
* proper exception handling

These practices help build **reliable and maintainable API clients**.
