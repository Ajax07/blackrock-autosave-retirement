## 🏗 System Architecture

```mermaid
flowchart LR

Client[Client / User] --> API[FastAPI Service]

subgraph API_Layer
API --> TR[Transaction API]
API --> VR[Validator API]
API --> PR[Temporal Rules API]
API --> RR[Returns API]
API --> PERF[Performance API]
end

subgraph Core_Engine
TR --> RE[Rounding Engine]
VR --> VE[Validation Engine]
PR --> PE[Period Rules Engine]
PE --> AG[Aggregation Engine]
end

subgraph Financial_Services
RR --> IE[Investment Engine]
IE --> NPS[NPS Calculator]
IE --> IDX[Index Fund Calculator]
IE --> INF[Inflation Adjustment]
end

