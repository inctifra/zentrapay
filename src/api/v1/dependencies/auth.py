from fastapi import  Header, HTTPException, status

async def authorize_user(authorization: str = Header(...)):
    """
    Simple JWT validator: expects header 'Authorization: Bearer <token>'.
    """
    print("Raw header received:", authorization)
    _authorization = authorization.strip()
    if not _authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header",
        )

    token = _authorization.split(" ")[1]
    print("Token extracted:", token)

    if token != "my-valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    # Return user info (example)
    return {"user_id": "123", "role": "admin"}