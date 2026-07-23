# EIPSYC5 AFRICA

**ONE AFRICA. ONE PLATFORM. INFINITE JOURNEYS.**

A comprehensive digital ecosystem connecting the entire African tourism industry with travelers worldwide.

## Overview

EIPSYC5 AFRICA is a production-ready, scalable web platform + Progressive Web App + Mobile applications (Android/iOS) that serves as the primary digital gateway for African tourism.

The platform connects:
- **Travelers** → Countries, Destinations, Attractions, National Parks, Wildlife
- **Accommodation** → Hotels, Lodges, Camps, Resorts, Villas, Homestays
- **Transport** → Flights, Airports, Airlines, Car Rentals, Trains, Buses, Boats
- **Experiences** → Tour Operators, Guides, Activities, Events, Festivals
- **Commerce** → Booking Engine, Payment System, Commission Tracking, Analytics

## Tech Stack

- **Frontend:** React 18.x, TypeScript, Tailwind CSS, Redux Toolkit, React Query
- **Backend:** Python 3.11, FastAPI, SQLAlchemy ORM
- **Database:** PostgreSQL 15+
- **Hosting:** Google Cloud Platform (Cloud Run, Cloud SQL, Cloud Storage)
- **Authentication:** JWT + OAuth 2.0
- **Payments:** Stripe, Flutterwave, PayPal integration
- **Maps:** Google Maps API, Mapbox
- **Real-time:** WebSockets for live notifications

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- PostgreSQL 15+

### Local Development with Docker

```bash
# Clone the repository
git clone https://github.com/ibrahimmangu9-glitch/Eipsyc-5-.git
cd Eipsyc-5-

# Start all services
docker-compose up

# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Features (MVP - Phase 1)

### Foundation
- [ ] User authentication (traveler, operator, admin)
- [ ] 54 African countries database
- [ ] Destination discovery and search
- [ ] Hotel and accommodation listings
- [ ] Basic booking system
- [ ] Payment integration (Stripe/Flutterwave)
- [ ] Commission tracking
- [ ] Review and rating system

### Phase 2
- [ ] Tour operator marketplace
- [ ] Advanced itinerary builder
- [ ] Multi-country trip planning
- [ ] Flight integration (Amadeis API)
- [ ] Operator SaaS dashboard
- [ ] Auto Safari Planner

### Phase 3
- [ ] Tourism analytics dashboard
- [ ] AI-powered recommendations
- [ ] Affiliate system
- [ ] Creator hub
- [ ] Community tourism
- [ ] Travel wallet

## Project Structure

```
Eipsyc-5-/
├── frontend/               # React.js application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # 50+ page screens
│   │   ├── services/       # API client services
│   │   ├── store/          # Redux state management
│   │   ├── hooks/          # Custom React hooks
│   │   ├── utils/          # Helper functions
│   │   ├── types/          # TypeScript interfaces
│   │   └── App.tsx         # Main app component
│   ├── public/             # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── backend/                # Python FastAPI application
│   ├── app/
│   │   ├── main.py         # FastAPI app entry point
│   │   ├── api/            # Route handlers
│   │   ├── models/         # SQLAlchemy ORM models
│   │   ├── schemas/        # Pydantic request/response schemas
│   │   ├── services/       # Business logic
│   │   ├── database.py     # Database configuration
│   │   └── config.py       # App configuration
│   ├── migrations/         # Alembic database migrations
│   ├── tests/              # Pytest test suite
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── docs/                   # Documentation
│   ├── API.md              # API documentation
│   ├── ARCHITECTURE.md     # System architecture
│   └── DATABASE.md         # Database design
│
├── docker-compose.yml      # Local development setup
├── .gitignore
├── LICENSE
└── README.md
```

## Security

### Critical: Owner Payout Account
The owner's payout bank account is stored **ONLY in secure backend**:
- ✅ Backend environment variables only
- ✅ Google Secret Manager in production
- ✅ Never in code or frontend
- ✅ Environment variable: `EIPSYC5_OWNER_PAYOUT_ACCOUNT`

### Authentication & Authorization
- JWT tokens with refresh mechanism
- Secure HttpOnly cookies
- Role-based access control (RBAC)
- Two-factor authentication ready
- OAuth 2.0 integration ready

### Data Protection
- HTTPS/TLS 1.3 for all data in transit
- Encrypted sensitive data at rest
- SQL injection prevention (SQLAlchemy ORM)
- Rate limiting per IP/user
- CORS configuration
- Audit logging for financial transactions

## API Endpoints (v1)

```
GET    /api/v1/countries
GET    /api/v1/countries/{id}
GET    /api/v1/destinations
GET    /api/v1/accommodations
POST   /api/v1/bookings
GET    /api/v1/bookings/{id}
POST   /api/v1/payments
GET    /api/v1/operators
POST   /api/v1/reviews
```

Full API documentation at `/api/v1/docs` (Swagger UI)

## Commission System

Default commission rates:
- **Hotels:** 10%
- **Tour Operators:** 15%
- **Accommodations:** 15%
- **Activities:** 5%

## Deployment to Google Cloud

### Backend (Cloud Run)
```bash
cd backend
gcloud run deploy eipsyc5-backend \
  --source . \
  --platform managed \
  --region us-central1
```

### Database (Cloud SQL)
```bash
gcloud sql instances create eipsyc5-db \
  --database-version POSTGRES_15 \
  --region us-central1
```

### Frontend (Cloud Storage + CDN)
```bash
cd frontend
npm run build
gsutil -m cp -r dist/* gs://eipsyc5-frontend/
```

See `docs/DEPLOYMENT.md` for detailed instructions.

## Contributing

See `CONTRIBUTING.md` for guidelines on code style, testing, and pull requests.

## License

MIT License - See `LICENSE` file.

## Support

For questions or issues:
1. Check the `docs/` directory
2. Create a GitHub issue
3. Start a discussion

---

**Made with ❤️ for African Tourism**
