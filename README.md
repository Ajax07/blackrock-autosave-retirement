# BlackRock AutoSave Retirement Engine
### Production-Grade Automated Retirement Micro-Investment Platform

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-framework-green)
![Docker](https://img.shields.io/badge/Docker-container-blue)

---

# Overview

A production-grade financial platform that enables **automated retirement savings** using an expense rounding strategy.

The system processes daily expenses, rounds them to the nearest multiple of 100, invests the remainder, applies temporal investment rules, and calculates long-term retirement returns.

Built for the **BlackRock Self-Saving for Retirement Hackathon**.

---

## Expense Rounding Engine
- Rounds expenses to nearest multiple of 100
- Computes remanent for investment
- Optimized for large-scale processing

## Transaction Validation
- Duplicate timestamp detection
- Negative amount rejection
- Wage-based investment constraints
- Financial data integrity enforcement

## Temporal Constraints Engine
Supports investment rules across time:

- **q periods** → fixed investment override
- **p periods** → extra investment addition
- **k periods** → investment aggregation by date range

## Investment & Returns Engine
- End-to-end investment pipeline
- National Pension Scheme (7.11%)
- Index Fund / NIFTY 50 (14.49%)
- Inflation-adjusted projections
- Compound interest calculation

## High Performance
- Handles up to 10⁶ transactions
- Runtime performance monitoring
- Memory and thread tracking

## Production Engineering
- Modular architecture
- Strong validation models
- Unit + integration tests
- Docker deployment
- CI pipeline

---

# System Architecture

## End-to-End Processing Pipeline

```mermaid
flowchart LR

Client --> API[FastAPI Service]

API --> VAL[Transaction Validator]
VAL --> ROUND[Rounding Engine]
ROUND --> TEMP[Temporal Rules Engine]
TEMP --> AGG[Aggregation Engine]
AGG --> INV[Investment Engine]
INV --> RET[Returns Calculation]

API --> PERF[Performance Monitoring]
````

---

## Request Flow

```mermaid
sequenceDiagram

Client->>API: Submit Expenses + q/p/k + wage
API->>Validator: Validate transactions
Validator-->>API: Valid + Invalid
API->>Rounding: Calculate ceiling & remanent
API->>TemporalRules: Apply q/p/k rules
API->>InvestmentEngine: Calculate total investment
InvestmentEngine->>Returns: Compute retirement value
Returns-->>Client: Investment projections
```

---

# API Endpoints

## Transaction Processing

### Parse Expenses

```
POST /blackrock/challenge/v1/transactions:parse
```

Rounds expenses and computes remanent.

---

### Transaction Validator

```
POST /blackrock/challenge/v1/transactions:validator
```

Validates transactions using:

* wage constraints
* duplicate detection
* financial rules

---

### Temporal Constraints Validator

```
POST /blackrock/challenge/v1/transactions:filter
```

Applies:

* q period rules
* p period rules
* k aggregation periods

Rejects:

* duplicate timestamps
* negative amounts

---

## Returns Calculation (Full Pipeline)

### NPS Investment Returns

```
POST /blackrock/challenge/v1/returns:nps
```

### Index Fund Returns

```
POST /blackrock/challenge/v1/returns:index
```

Executes full pipeline:

```
validate → round → temporal rules → aggregate → investment → returns
```

---

## Performance Monitoring

```
GET /blackrock/challenge/v1/performance
```

Reports:

* execution time
* memory usage
* thread count

---

# Financial Model

## Investment Formula

```
FV = P(1 + r)^n
```

Where:

* P = investment amount
* r = annual return rate
* n = years to retirement

## Inflation Adjustment

```
Real Return = FV / (1 + inflation)^n
```

---

# Project Structure

```
blackrock-autosave-retirement/
│
├── api/                # REST endpoints
├── core/               # Financial engines
│   ├── rounding_engine.py
│   ├── period_engine.py
│   ├── aggregation_engine.py
│   └── full_returns_engine.py
│
├── models/             # Data validation models
├── services/           # Financial calculations
├── utils/              # Helpers and monitoring
├── test/               # Unit & integration tests
├── load_test/          # Performance testing
│
├── Dockerfile
├── compose.yaml
└── main.py
```

---

# Local Setup

## Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run Server

```
uvicorn main:app --reload --port 5477
```

## API Docs

```
http://localhost:5477/docs
```

---

# Run with Docker

```
docker compose up --build
```

---

# Testing

Run all tests:

```
pytest
```

Test types:

* Unit tests
* Integration tests
* Load tests

---

# Performance Characteristics

* O(n log n) processing complexity
* Memory-efficient computation
* Horizontal scaling ready
* Containerized deployment

---

# Innovation — Smart Rounding (Proposed Extension)

Future enhancement:

* dynamic investment based on market volatility
* ESG investment routing
* risk-adjusted savings strategy

---

# Scalability Strategy

* container orchestration support
* Redis caching (future)
* streaming transaction ingestion
* time-series database integration

---

# Author

Ajay Chouhan
BlackRock Hackathon Submission

---

# License

MIT License
