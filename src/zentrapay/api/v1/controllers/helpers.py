async def account_compliance_retrieve(id: str, client):
    return await client.get(f"accounts/{id}/compliance_settings")

async def account_post_action(client, id, data):
    return await client.post(f"accounts/{id}", data=data)
