import asyncio
from azure.cosmos import exceptions
from .database import cosmos_db


class ItemService:
    \"\"\"
    Service layer demonstrating async Cosmos operations.
    \"\"\"

    @staticmethod
    async def create_item(item: dict):
        return await cosmos_db.container.create_item(body=item)

    @staticmethod
    async def get_item(item_id: str):
        try:
            return await cosmos_db.container.read_item(
                item=item_id,
                partition_key=item_id
            )
        except exceptions.CosmosResourceNotFoundError:
            return None

    @staticmethod
    async def get_multiple_items_concurrently(item_ids: list[str]):
        \"\"\"
        Demonstrates asyncio concurrency using gather.
        \"\"\"

        tasks = [
            cosmos_db.container.read_item(
                item=item_id,
                partition_key=item_id
            )
            for item_id in item_ids
        ]

        return await asyncio.gather(*tasks, return_exceptions=True)
