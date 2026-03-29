from fastapi import Header, HTTPException, status

async def authorize_user(
    x_authorization: str | None = Header(None, alias="X-Authorization"),
):
    if not x_authorization:
        raise HTTPException(401, "No X-Authorization header received")

    _authorization = x_authorization.strip()
    if not _authorization.startswith("X-ZP-KEY "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid X-Authorization header",
        )

    token = _authorization.split(" ")[1]

    if token != "my-valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    return {"user_id": "123", "role": "admin"}