# EIPSYC5 AFRICA - Database Schema

## Overview

PostgreSQL 15+ database with 54 African countries and comprehensive tourism data.

## Core Tables

### Users

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone VARCHAR(20),
  role VARCHAR(50) NOT NULL,
  is_verified BOOLEAN DEFAULT false,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Countries

```sql
CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  code VARCHAR(3) UNIQUE NOT NULL,
  capital VARCHAR(100),
  region VARCHAR(100),
  currency VARCHAR(10),
  language VARCHAR(100),
  flag_url VARCHAR(500),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Destinations

```sql
CREATE TABLE destinations (
  id SERIAL PRIMARY KEY,
  country_id INTEGER NOT NULL REFERENCES countries(id),
  name VARCHAR(100) NOT NULL,
  description TEXT,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  type VARCHAR(50),
  best_season VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Accommodations

```sql
CREATE TABLE accommodations (
  id SERIAL PRIMARY KEY,
  destination_id INTEGER NOT NULL REFERENCES destinations(id),
  operator_id UUID REFERENCES users(id),
  name VARCHAR(200) NOT NULL,
  type VARCHAR(50),
  description TEXT,
  price_per_night DECIMAL(10, 2),
  currency VARCHAR(3),
  rooms_available INTEGER,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  rating DECIMAL(3, 2),
  is_verified BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Bookings

```sql
CREATE TABLE bookings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  accommodation_id INTEGER NOT NULL REFERENCES accommodations(id),
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  number_of_guests INTEGER NOT NULL,
  total_price DECIMAL(10, 2),
  currency VARCHAR(3),
  status VARCHAR(50) DEFAULT 'pending',
  special_requests TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Payments

```sql
CREATE TABLE payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  booking_id UUID NOT NULL REFERENCES bookings(id),
  amount DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3),
  status VARCHAR(50) DEFAULT 'pending',
  payment_method VARCHAR(50),
  stripe_charge_id VARCHAR(255),
  receipt_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Commissions

```sql
CREATE TABLE commissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payment_id UUID NOT NULL REFERENCES payments(id),
  accommodation_id INTEGER NOT NULL REFERENCES accommodations(id),
  provider_id UUID NOT NULL REFERENCES users(id),
  commission_rate DECIMAL(5, 2),
  commission_amount DECIMAL(10, 2),
  status VARCHAR(50) DEFAULT 'pending',
  settled_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Reviews

```sql
CREATE TABLE reviews (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  entity_type VARCHAR(50),
  entity_id INTEGER,
  rating INTEGER CHECK (rating >= 1 AND rating <= 5),
  comment TEXT,
  is_verified BOOLEAN DEFAULT false,
  helpful_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Attractions

```sql
CREATE TABLE attractions (
  id SERIAL PRIMARY KEY,
  destination_id INTEGER NOT NULL REFERENCES destinations(id),
  name VARCHAR(200) NOT NULL,
  type VARCHAR(50),
  description TEXT,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  entry_fee DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Operators

```sql
CREATE TABLE operators (
  id UUID PRIMARY KEY REFERENCES users(id),
  company_name VARCHAR(200) NOT NULL,
  registration_number VARCHAR(100),
  description TEXT,
  website VARCHAR(500),
  phone VARCHAR(20),
  rating DECIMAL(3, 2),
  is_verified BOOLEAN DEFAULT false,
  specialties VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Indexes

```sql
-- Performance indexes
CREATE INDEX idx_countries_code ON countries(code);
CREATE INDEX idx_destinations_country_id ON destinations(country_id);
CREATE INDEX idx_accommodations_destination_id ON accommodations(destination_id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);
CREATE INDEX idx_commissions_provider_id ON commissions(provider_id);
CREATE INDEX idx_reviews_entity ON reviews(entity_type, entity_id);
CREATE INDEX idx_attractions_destination_id ON attractions(destination_id);
```

## Data Integrity

- Foreign key constraints on all related tables
- NOT NULL constraints on required fields
- UNIQUE constraints on identifiers (email, country code, etc.)
- CHECK constraints on numeric ranges (ratings 1-5, etc.)

## Backup Strategy

- Cloud SQL automated daily backups (35-day retention)
- Transaction logs for point-in-time recovery
- Multi-region replication available for production
