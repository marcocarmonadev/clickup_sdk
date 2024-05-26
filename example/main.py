import asyncio

import httpx

from clickup_sdk import ClickUpClient


async def main():
    async with httpx.AsyncClient(
        timeout=None,
    ) as http_client:
        clickup_client = ClickUpClient(http_client)


if __name__ == "__main__":
    asyncio.run(main())
