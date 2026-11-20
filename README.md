# Navoiyazot Logistics · Spare Parts Control API

Asset control and component lifecycle tracking system for **Navoiyazot logistics and industrial vehicles**. Prevents illicit parts requisition, premature replacements, and cross-model specification mismatches.

---

## Key Capabilities

* **Pre-Issuance Request Validation**: Evaluates component requests against vehicle history *before* the warehouse releases the part.
* **Cross-Compatibility Platform Engine**: Recognizes shared standard components between sister platforms (e.g., Damas and Labo) to eliminate false mismatch warnings.
* **Component Lifecycle Tracking**: Enforces expected operational lifespans (kilometres, operating months, engine hours, warranty limits).
* **Digital Vehicle Passport**: Maintains a comprehensive 15-node historical component passport for every vehicle in the fleet.

---

## Tech Stack

* **Language**: Python 3.12+
* **Framework**: FastAPI (REST)
* **Rules Engine**: Deterministic component compatibility matrix and life-cycle estimators
* **Database Driver**: Psycopg2-binary (PostgreSQL)

---

## Core Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/parts-control/scan` | Audit fleet for parts mismatches, early replacements, and stock leaks |
| `GET` | `/parts-control/passport` | Complete digital component lifecycle passport for a vehicle |
| `GET` | `/parts-control/check` | Pre-issue justification check for a specific part request |
| `GET` | `/parts-control/norms` | Fleet component replacement norms by model |
| `GET` | `/healthz` | Service health status |

---

## Quick Start

### 1. Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=atil_navoiyazot
DB_USER=postgres
DB_PASSWORD=your_password
```

### 3. Run Service
```bash
python main.py
# Server runs on http://localhost:8003 (Docs: http://localhost:8003/docs)
```
