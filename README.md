# blackrock-autosave-retirement


```markdown
# Architecture

(## 🏗 System Architecture

```mermaid
flowchart LR

Client[Client / User] --> API[FastAPI Service]

subgraph API Layer
API --> TR[Transaction API]
API --> VR[Validator API]
API --> PR[Temporal Rules API]
API --> RR[Returns API]
API --> PERF[Performance API]
end

subgraph Core Engine
TR --> RE[Rounding Engine]
VR --> VE[Validation Engine]
PR --> PE[Period Rules Engine]
PE --> AG[Aggregation Engine]
end

subgraph Financial Services
RR --> IE[Investment Engine]
IE --> NPS[NPS Calculator]
IE --> IDX[Index Fund Calculator]
IE --> INF[Inflation Adjustment]
end

subgraph Storage & Monitoring
API --> DB[(Transaction Storage)]
API --> MON[Performance Monitoring]
end


# Request Flow

```markdown
### 🔄 Request Processing Flow

```mermaid
sequenceDiagram

participant Client
participant API
participant Validator
participant Rounding
participant PeriodRules
participant Returns

Client->>API: Submit Expenses
API->>Validator: Validate Transactions
Validator-->>API: Valid Transactions
API->>Rounding: Calculate Ceiling & Remanent
Rounding-->>API: Processed Transactions
API->>PeriodRules: Apply q/p/k Rules
PeriodRules-->>API: Aggregated Savings
API->>Returns: Calculate Investment Returns
Returns-->>Client: Retirement Projection

# Component Architecture

```markdown
### 🧩 Component Architecture

```mermaid
flowchart TB

main[main.py - FastAPI Entry]

main --> api[API Layer]
main --> core[Core Business Logic]
main --> services[Financial Services]
main --> models[Data Models]
main --> utils[Utilities]

api --> transactions[transactions.py]
api --> validator[validator.py]
api --> temporal[temporal_rules.py]
api --> returns[returns.py]

core --> rounding[rounding_engine.py]
core --> period[period_engine.py]
core --> aggregation[aggregation_engine.py]

services --> projection[projection_service.py]
services --> tax[tax_service.py]
