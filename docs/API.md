# EIPSYC5 AFRICA - API Documentation

## Base URL

- Development: `http://localhost:8000/api/v1`
- Production: `https://eipsyc5-backend.run.app/api/v1`

## Authentication

All protected endpoints require JWT token in Authorization header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Countries

```
GET /countries
GET /countries/{id}
GET /countries/{id}/destinations
GET /countries/{id}/accommodations
GET /countries/{id}/attractions
GET /countries/{id}/operators
```

### Destinations

```
GET /destinations
GET /destinations/{id}
GET /destinations/{id}/accommodations
GET /destinations/{id}/attractions
GET /destinations/{id}/activities
```

### Accommodations

```
GET /accommodations
GET /accommodations/{id}
POST /accommodations (operator only)
PUT /accommodations/{id} (operator only)
DELETE /accommodations/{id} (operator only)
```

### Bookings

```
GET /bookings (user's bookings)
GET /bookings/{id}
POST /bookings
PUT /bookings/{id} (operator only)
GET /bookings/{id}/invoice
```

### Payments

```
POST /payments/initiate
GET /payments/{id}
POST /payments/webhook (stripe)
```

### Operators

```
GET /operators
GET /operators/{id}
GET /operators/{id}/tours
GET /operators/{id}/reviews
POST /operators (registration)
PUT /operators/{id} (own operator only)
```

### Reviews

```
GET /reviews
GET /reviews?entity_type=accommodation&entity_id={id}
POST /reviews
PUT /reviews/{id} (own review only)
DELETE /reviews/{id} (own review only)
```

### Authentication

```
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout
POST /auth/verify-email
POST /auth/forgot-password
POST /auth/reset-password
```

### Admin

```
GET /admin/dashboard
GET /admin/users
GET /admin/bookings
GET /admin/payments
GET /admin/commissions
GET /admin/analytics
POST /admin/countries
PUT /admin/countries/{id}
```

## Response Format

All responses are JSON:

```json
{
  "success": true,
  "data": {},
  "message": "Success message",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

Error response:

```json
{
  "success": false,
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": {}
}
```

## Status Codes

- 200: OK
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 500: Server Error

## Rate Limiting

- 100 requests per minute per IP
- 1000 requests per hour per user

## Pagination

Use `limit` and `offset` query parameters:

```
GET /accommodations?limit=20&offset=0
```

## Filtering & Searching

```
GET /accommodations?destination_id=123&min_price=100&max_price=500
GET /destinations?country_id=1&search=beach
```

## Swagger Documentation

Interactive API docs available at:
- Development: `http://localhost:8000/docs`
- Production: `https://eipsyc5-backend.run.app/docs`
