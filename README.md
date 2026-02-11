# FastAPI + Azure Cosmos Async Demo

This project demonstrates how to integrate Azure Cosmos DB asynchronously with FastAPI using the zure.cosmos.aio SDK.

## Features

- Async Cosmos DB client
- Proper FastAPI startup/shutdown lifecycle
- Service layer architecture
- Non-blocking I/O operations
- Concurrency using syncio.gather
- Batch endpoint to demonstrate parallel database reads

## Run

uvicorn app.main:app --reload
