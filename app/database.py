import os
from azure.cosmos.aio import CosmosClient

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME", "demo-db")
CONTAINER_NAME = os.getenv("CONTAINER_NAME", "items")


class CosmosDB:
    \"\"\"
    Handles Cosmos DB async connection lifecycle.
    \"\"\"

    def __init__(self):
        self.client: CosmosClient | None = None
        self.container = None

    async def connect(self):
        if not COSMOS_URL or not COSMOS_KEY:
            raise ValueError("COSMOS_URL and COSMOS_KEY must be set")

        self.client = CosmosClient(COSMOS_URL, COSMOS_KEY)
        database = self.client.get_database_client(DATABASE_NAME)
        self.container = database.get_container_client(CONTAINER_NAME)

    async def close(self):
        if self.client:
            await self.client.close()


cosmos_db = CosmosDB()
