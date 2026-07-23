# 🚀 Quick Start Guide

## Prerequisites
- **Docker** and **Docker Compose** installed
- Git (to clone the repo)

## 1️⃣ Clone & Navigate
```bash
git clone https://github.com/ibrahimmangu9-glitch/Eipsyc-5-.git
cd Eipsyc-5-
```

## 2️⃣ Start Services with Docker Compose
```bash
docker-compose up --build
```

This will start:
- **PostgreSQL** (port 5432)
- **Redis** (port 6379)
- **FastAPI Backend** (port 8000)
- **React Frontend** (port 3000)

## 3️⃣ Access the Application

| Service | URL |
|---------|-----|
| **Frontend (React)** | http://localhost:3000 |
| **Backend API** | http://localhost:8000 |
| **API Docs (Swagger)** | http://localhost:8000/docs |
| **ReDoc** | http://localhost:8000/redoc |
| **Health Check** | http://localhost:8000/health |

## 4️⃣ Check Status

### Backend is Ready When:
```bash
curl http://localhost:8000/health
# Response: {"status":"healthy","timestamp":"...","service":"EIPSYC5 AFRICA Backend"}
```

### Frontend is Ready When:
- Navigate to http://localhost:3000
- You should see the application homepage

## 5️⃣ Next Steps

### Seed Database (Optional)
Once backend is running, you can add sample data:
```bash
docker-compose exec backend python scripts/seed_data.py
```

### Run Tests (Optional)
```bash
# Backend tests
docker-compose exec backend pytest tests/ --cov=app

# Frontend tests
docker-compose exec frontend npm run test:coverage
```

## 🛑 Stop Services
```bash
docker-compose down
```

**To remove data volumes too:**
```bash
docker-compose down -v
```

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check logs
docker-compose logs backend

# Verify database connection
docker-compose exec backend python -c "from app.database import engine; print(engine)"
```

### Frontend won't start
```bash
# Check logs
docker-compose logs frontend

# Verify Node.js dependencies
docker-compose exec frontend npm install
```

### Database permission error
```bash
# Ensure postgres container is healthy
docker-compose logs postgres

# Try restarting postgres
docker-compose restart postgres
```

### Port already in use
Edit `docker-compose.yml` and change port mappings:
```yaml
ports:
  - "3001:3000"  # Frontend on 3001 instead
  - "8001:8000"  # Backend on 8001 instead
```

## 📝 Environment Variables

Edit `.env` file to customize:
- `DATABASE_URL` — PostgreSQL connection string
- `REDIS_URL` — Redis connection string
- `JWT_SECRET` — Your JWT signing secret
- `CORS_ORIGINS` — Allowed frontend origins
- API keys for Google Maps, Stripe, Flutterwave

---

**Still stuck?** Check `docker-compose logs` or see [ARCHITECTURE.md](ARCHITECTURE.md) for detailed setup.
