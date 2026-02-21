

# **Complete API Testing Guide**

---

```markdown
# BlackRock AutoSave — API Testing Guide

Base URL:

```

[http://localhost:5477](http://localhost:5477)

```

Start server:

```

uvicorn main:app --reload --port 5477

```

---

# Transaction Parsing

## Endpoint
```

POST /blackrock/challenge/v1/transactions:parse

````

## Description
Rounds expenses to nearest multiple of 100 and computes remanent.

## Request

```bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/transactions:parse" \
-H "Content-Type: application/json" \
-d '[
  {"date": "2023-10-12T20:15:30", "amount": 250},
  {"date": "2023-02-28T15:49:20", "amount": 375},
  {"date": "2023-07-01T21:59:00", "amount": 620}
]'
````

## Expected

* ceiling = next multiple of 100
* remanent = difference

---

# Transaction Validator

## Endpoint

```
POST /blackrock/challenge/v1/transactions:validator
```

## Description

Validates transactions using:

* wage constraints
* duplicate timestamp detection
* negative amount rejection

## Request

```bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/transactions:validator" \
-H "Content-Type: application/json" \
-d '{
  "wage": 50000,
  "transactions": [
    {
      "timestamp": "2023-01-15T10:30:00",
      "amount": 2000,
      "ceiling": 2100,
      "remanent": 100
    },
    {
      "timestamp": "2023-01-15T10:30:00",
      "amount": 2000,
      "ceiling": 2100,
      "remanent": 100
    },
    {
      "timestamp": "2023-03-20T14:45:00",
      "amount": -200,
      "ceiling": 300,
      "remanent": 50
    }
  ]
}'
```

## Expected

* duplicate → invalid
* negative → invalid
* valid transactions returned

---

# Temporal Constraints Validator (q / p / k)

## Endpoint

```
POST /blackrock/challenge/v1/transactions:filter
```

## Description

Applies:

* q period fixed override
* p period extra investment
* k period aggregation
* rejects duplicate dates and negative amounts

## Request

```bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/transactions:filter" \
-H "Content-Type: application/json" \
-d '{
  "wage": 50000,
  "transactions": [
    {"date": "2023-02-28T15:49:20", "amount": 375},
    {"date": "2023-07-15T10:30:00", "amount": 620},
    {"date": "2023-10-12T20:15:30", "amount": 250},
    {"date": "2023-10-12T20:15:30", "amount": 250},
    {"date": "2023-12-17T08:09:45", "amount": -480}
  ],
  "q": [
    {
      "fixed": 0,
      "start": "2023-07-01T00:00:00",
      "end": "2023-07-31T23:59:59"
    }
  ],
  "p": [
    {
      "extra": 30,
      "start": "2023-10-01T00:00:00",
      "end": "2023-12-31T23:59:59"
    }
  ],
  "k": [
    {
      "start": "2023-01-01T00:00:00",
      "end": "2023-12-31T23:59:59"
    }
  ]
}'
```

## Expected

* valid_transactions
* invalid_transactions
* savings_by_period

---

#  Full Returns Calculation — NPS

## Endpoint

```
POST /blackrock/challenge/v1/returns:nps
```

## Description

Runs full pipeline:

```
validate → round → temporal rules → aggregate → investment → returns
```

Uses NPS rate = 7.11%.

## Request

```bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/returns:nps" \
-H "Content-Type: application/json" \
-d '{
  "age": 29,
  "wage": 50000,
  "inflation": 5.5,
  "transactions": [
    {"date": "2023-02-28T15:49:20", "amount": 375},
    {"date": "2023-07-01T21:59:00", "amount": 620},
    {"date": "2023-10-12T20:15:30", "amount": 250},
    {"date": "2023-12-17T08:09:45", "amount": 480}
  ],
  "q": [],
  "p": [],
  "k": []
}'
```

## Expected

* total investment
* future value
* inflation adjusted value

---

# Full Returns Calculation — Index Fund

## Endpoint

```
POST /blackrock/challenge/v1/returns:index
```

## Description

Same pipeline using Index return rate = 14.49%.

## Request

```bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/returns:index" \
-H "Content-Type: application/json" \
-d '{
  "age": 29,
  "wage": 50000,
  "inflation": 5.5,
  "transactions": [
    {"date": "2023-02-28T15:49:20", "amount": 375},
    {"date": "2023-07-01T21:59:00", "amount": 620},
    {"date": "2023-10-12T20:15:30", "amount": 250},
    {"date": "2023-12-17T08:09:45", "amount": 480}
  ],
  "q": [],
  "p": [],
  "k": []
}'
```

## Expected

* higher return than NPS

---

# Performance Report

## Endpoint

```
GET /blackrock/challenge/v1/performance
```

## Description

Reports runtime metrics.

## Request

```bash
curl http://localhost:5477/blackrock/challenge/v1/performance
```

## Expected Output

```
{
  "time_ms": <execution_time>,
  "memory_mb": <memory_usage>,
  "threads": <thread_count>
}
```

---

# Recommended Testing Order

1. transactions:parse
2. transactions:validator
3. transactions:filter
4. returns:index / returns:nps
5. performance


