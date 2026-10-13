from datetime import UTC, datetime, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from config import setting

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/token")

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def creare_access_token(data: dict, expires_delta: timedelta | None = None):
    '''Create a JWT access token'''
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=setting.access_token_expire_minutes)
    to_encode.update({"exp":expire})

    encode_jwt = jwt.encode(to_encode, setting.secret_key.get_secret_value(), algorithm=setting.algorithm)

    return encode_jwt

def verify_access_token(token:str) -> str | None:
    '''Verify a JWT access token and return the subject (user id) if valid'''

    try:
        payload = jwt.decode(token, setting.secret_key.get_secret_value(),algorithms=[setting.algorithm],options={"require":["exp", "sub"]})
    except jwt.InvalidTokenError:
        return None
    else:
        return payload.get("sub")