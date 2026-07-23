# EIPSYC5 AFRICA - System Architecture

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │  React Web App   │  │  Mobile App      │  │  Admin Panel │  │
│  │  (SPA)           │  │  (React Native)  │  │  (React)     │  │
│  └────────┬─────────┘  └────────┬─────────┘  └──────┬───────┘  │
└───────────┼──────────────────────┼───────────────────┼──────────┘
            │                      │                   │
            └──────────────────────┼───────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   API Gateway / Load       │
                    │   Balancer (Cloud Load)    │
                    └──────────────┬──────────────┘
                                   │
┌─────────────────────────────────▼──────────────────────────────┐
│                      APPLICATION LAYER                          │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              FastAPI Backend (Python)                    │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │  API Routes (v1)                                 │   │  │
│  │  │  - Auth endpoints                               │   │  │
│  │  │  - Countries & Destinations                     │   │  │
│  │  │  - Accommodations & Bookings                    │   │  │
│  │  │  - Payments & Commissions                       │   │  │
│  │  │  - Operators & Tours                            │   │  │
│  │  │  - Reviews & Ratings                            │   │  │
│  │  │  - Admin endpoints                              │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │  Service Layer (Business Logic)                  │   │  │
│  │  │  - AuthService                                   │   │  │
│  │  │  - BookingService                                │   │  │
│  │  │  - PaymentService                                │   │  │
│  │  │  - CommissionService                             │   │  │
│  │  │  - NotificationService                           │   │  │
│  │  │  - SearchService                                 │   │  │
│  │  │  - AnalyticsService                              │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │  Middleware                                      │   │  │
│  │  │  - JWT Authentication                            │   │  │
│  │  │  - CORS                                          │   │  │
│  │  │  - Rate Limiting                                 │   │  │
│  │  │  - Error Handling                                │   │  │
│  │  │  - Logging                                       │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────────┐  ┌──────────▼────────────┐  ┌─────────▼────┐
│   PostgreSQL       │  │   External APIs      │  │   Cloud      │
│   Database         │  │   - Google Maps      │  │   Storage    │
│   (Cloud SQL)      │  │   - Stripe           │  │   (Images)   │
│                    │  │   - Flutterwave      │  │              │
│   Tables:          │  │   - Amadeus          │  │   S3-like    │
│   - users          │  │   - Twilio           │  │   bucket     │
│   - countries      │  │   - SendGrid         │  │              │
│   - destinations   │  │                      │  └──────────────┘
│   - attractions    │  └──────────────────────┘
│   - accommodations │
│   - bookings       │
│   - payments       │
│   - commissions    │
│   - operators      │
│   - reviews        │
└────────────────────┘
```

## Technology Stack Details

### Frontend (React)
- **Framework:** React 18 with TypeScript
- **State Management:** Redux Toolkit + Redux Persist
- **Data Fetching:** React Query (TanStack Query)
- **Styling:** Tailwind CSS + Styled Components
- **UI Components:** Shadcn/ui + Radix UI
- **Forms:** React Hook Form + Zod validation
- **Maps:** Google Maps React + Mapbox GL
- **Charts:** Recharts + Chart.js
- **Auth:** JWT stored in secure HttpOnly cookies
- **Build:** Vite
- **Testing:** Vitest + React Testing Library

### Backend (Python/FastAPI)
- **Framework:** FastAPI (ASGI)
- **ORM:** SQLAlchemy 2.0
- **Database Driver:** psycopg2-binary
- **Validation:** Pydantic v2
- **Authentication:** python-jose + passlib
- **Async:** asyncio + httpx
- **Task Queue:** Celery + Redis (for background jobs)
- **Caching:** Redis
- **Email:** python-dotenv + aiosmtplib
- **Payments:** stripe + flutterwave SDKs
- **Testing:** pytest + pytest-asyncio
- **Logging:** Python logging + structlog

### Database (PostgreSQL)
- **Version:** 15+
- **Connection Pool:** pgbouncer (via Cloud SQL Proxy)
- **Extensions:** PostGIS (for geospatial queries), UUID
- **Backups:** Cloud SQL automated backups

### Infrastructure (Google Cloud)
- **Compute:** Cloud Run (serverless containers)
- **Database:** Cloud SQL (PostgreSQL managed service)
- **Storage:** Cloud Storage (images, documents)
- **Cache:** Cloud Memorystore (Redis)
- **CDN:** Cloud CDN + Cloud Armor
- **Secrets:** Secret Manager
- **Monitoring:** Cloud Logging + Cloud Monitoring
- **CI/CD:** Cloud Build + GitHub Actions

## Data Flow

### Booking Flow
```
1. Traveler searches → Frontend queries /api/v1/accommodations
2. Backend queries PostgreSQL for matching accommodations
3. Results returned to frontend
4. Traveler selects and initiates booking → POST /api/v1/bookings
5. Backend creates booking record (status: pending)
6. Frontend redirects to payment page → POST /api/v1/payments
7. Payment processor (Stripe/Flutterwave) processes transaction
8. Webhook from payment provider → Backend updates booking status
9. Backend calculates commission and records in commissions table
10. Notification sent to traveler and operator
11. Booking confirmation returned to frontend
```

### Commission Flow
```
1. Booking completed with payment
2. CommissionService calculates commission based on provider type:
   - Hotel: 10% of booking amount
   - Tour Operator: 15%
   - Accommodation: 15%
   - Activities: 5%
3. Commission record created in commissions table
4. Provider settlement amount calculated
5. Monthly batch job processes settlements
6. Payout initiated to provider bank account
7. EIPSYC5 owner commission deposited to secure backend account
   (EIPSYC5_OWNER_PAYOUT_ACCOUNT - never exposed in code)
8. Transaction logged with full audit trail
```

## Authentication & Authorization

### JWT Flow
```
1. User login → POST /api/v1/auth/login
2. Backend validates credentials
3. Generate JWT (access_token) + refresh_token
4. Tokens returned to frontend
5. Access token stored in secure HttpOnly cookie
6. Refresh token stored in secure HttpOnly cookie
7. All subsequent requests include JWT in Authorization header
8. Middleware verifies JWT on every protected route
9. Token refresh endpoint refreshes expired tokens
```

### Role-Based Access Control (RBAC)
- **traveler** - Can search, book, review
- **guide** - Can manage profile, accept bookings
- **operator** - Can manage tours, packages, bookings (requires SaaS subscription)
- **accommodations_provider** - Can manage property listings
- **admin** - Can manage countries, destinations, moderate reviews
- **super_admin** - Full platform access, financial controls

## Caching Strategy

- **Static data** (countries, destinations): Redis cache + 24-hour TTL
- **User data**: Session cache + 1-hour TTL
- **Search results**: Query-specific cache + 30-minute TTL
- **Operator SaaS data**: Real-time, no caching

## Security Architecture

### Secret Management
- Database credentials: Google Secret Manager
- API keys (Stripe, Google Maps): Secret Manager
- JWT secret: Secret Manager
- Owner payout account: Secret Manager (backend only)
- Environment variables loaded at runtime, never committed

### Data Protection
- All data in transit: HTTPS/TLS 1.3
- Sensitive fields encrypted at rest (e.g., payment tokens)
- PII fields masked in logs
- Rate limiting per IP/user
- SQL injection prevention: SQLAlchemy ORM parameterized queries

### Audit Logging
- All financial transactions logged
- User actions tracked with timestamp
- Booking changes recorded with before/after state
- Admin actions require approval for sensitive operations

## Scalability Considerations

- **Horizontal scaling:** Cloud Run auto-scales containers
- **Database scaling:** Cloud SQL read replicas for reporting queries
- **Caching:** Redis for session and frequently accessed data
- **CDN:** Static assets (JS, CSS, images) served from Cloud CDN
- **Async jobs:** Celery workers for email, notifications, batch processing
- **Search:** Elasticsearch integration for advanced destination/attraction search (Phase 2)

## Monitoring & Observability

- **Logging:** Cloud Logging for all application events
- **Metrics:** Cloud Monitoring for performance tracking
- **Tracing:** Cloud Trace for request flow analysis
- **Alerts:** Uptime checks, error rate thresholds, database performance
- **Dashboards:** Real-time operational dashboards

## Disaster Recovery

- **Backups:** Cloud SQL automated daily backups (35-day retention)
- **Replication:** Multi-region Cloud SQL replication available
- **RTO/RPO:** Aim for <1 hour recovery time, <15 min data loss
- **Testing:** Quarterly backup restoration tests
