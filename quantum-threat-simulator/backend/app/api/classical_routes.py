from fastapi import APIRouter
from pydantic import BaseModel

from app.crypto.rsa_demo import RSADemo
from app.crypto.ecc_demo import ECCDemo

router = APIRouter(
    prefix="/classical",
    tags=["Classical Crypto"]
)


class MessageRequest(BaseModel):
    value: int


@router.get("/rsa/keygen")
def rsa_keygen():

    rsa = RSADemo()

    return rsa.keygen()


@router.post("/rsa/encrypt")
def rsa_encrypt(payload: MessageRequest):

    rsa = RSADemo()

    return rsa.encrypt(payload.value)


@router.post("/rsa/decrypt")
def rsa_decrypt(payload: MessageRequest):

    rsa = RSADemo()

    return rsa.decrypt(payload.value)


@router.get("/ecc/exchange")
def ecc_exchange():

    ecc = ECCDemo()

    return ecc.exchange()