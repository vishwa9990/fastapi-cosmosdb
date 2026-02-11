from fastapi import FastAPI, HTTPException
from .database import cosmos_db
from .models import Item
from .services import ItemService

app = FastAPI(
    title="FastAPI Cosmos Async Demo",
    description="Demonstrates async Cosmos DB integration with FastAPI",
)


@app.on_event(\"startup\")
async def startup():
    await cosmos_db.connect()


@app.on_event(\"shutdown\")
async def shutdown():
    await cosmos_db.close()


@app.get(\"/\")
async def health_check():
    return {\"status\": \"running\"}


@app.post(\"/items\")
async def create_item(item: Item):
    return await ItemService.create_item(item.dict())


@app.get(\"/items/{item_id}\")
async def get_item(item_id: str):
    item = await ItemService.get_item(item_id)

    if not item:
        raise HTTPException(status_code=404, detail=\"Item not found\")

    return item


@app.post(\"/items/batch\")
async def get_items_batch(item_ids: list[str]):
    \"\"\"
    Demonstrates concurrent I/O operations with asyncio.gather.
    \"\"\"
    return await ItemService.get_multiple_items_concurrently(item_ids)
