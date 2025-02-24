from azure.cosmos import CosmosClient

def store_url_in_db(url, content):
    """Stores webpage content in Azure CosmosDB."""
    client = CosmosClient("YOUR_COSMOSDB_ENDPOINT", credential="YOUR_COSMOSDB_KEY")
    database = client.get_database_client("YOUR_DATABASE")
    container = database.get_container_client("YOUR_CONTAINER")

    document = {
        "id": url,
        "content": content,
        "source": url
    }

    container.upsert_item(document)
    print(f"Stored in DB: {url}")
