from fastapi import APIRouter
from pydantic import BaseModel

from app.crypto.lwe import LWE

router = APIRouter(
    prefix="/lwe",
    tags=["LWE"]
)


class EncryptRequest(BaseModel):
    message: int


class DecryptRequest(BaseModel):
    ciphertext: int


@router.get("/status")
def status():
    return {
        "algorithm": "Learning With Errors",
        "ready": True
    }


@router.get("/keygen")
def keygen():

    lwe = LWE()

    return lwe.keygen()


@router.post("/encrypt")
def encrypt(payload: EncryptRequest):

    lwe = LWE()

    return lwe.encrypt(payload.message)


@router.post("/decrypt")
def decrypt(payload: DecryptRequest):

    lwe = LWE()

    return lwe.decrypt(payload.ciphertext)