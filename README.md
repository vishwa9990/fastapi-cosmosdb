# fastapi-cosmosdb
FastAPI + Azure Cosmos DB (Async) Demo

This project demonstrates:
Async integration of Azure Cosmos DB using azure.cosmos.aio
Proper FastAPI lifecycle management
Non-blocking I/O operations
Concurrency using asyncio.gather
Clean service-layer architecture

Key Concepts Demonstrated:
Async Database Client
Cosmos async SDK is used to avoid blocking the event loop.
Connection Lifecycle
Cosmos client is initialized during startup and reused across requests.
Concurrent I/O Operations
The /items/batch endpoint demonstrates how multiple Cosmos queries can be executed concurrently using asyncio.gather.
Scalable Architecture
Designed to handle high-concurrency workloads efficiently.
