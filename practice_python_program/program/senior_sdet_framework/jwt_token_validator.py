"""
JWT Token Payload Extractor & Expiry Validator
Senior SDET Context: Decodes Base64-encoded JWT authorization tokens to validate user claims and check expiration times without third-party dependencies.
"""

import base64
import json
import time

def decode_jwt_payload(token: str) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT token format")
    payload_b64 = parts[1]
    padding = "=" * (4 - len(payload_b64) % 4)
    decoded_bytes = base64.urlsafe_b64decode(payload_b64 + padding)
    return json.loads(decoded_bytes.decode("utf-8"))

def is_token_expired(payload: dict) -> bool:
    exp = payload.get("exp")
    if not exp:
        return False
    return time.time() >= exp

if __name__ == "__main__":
    sample_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjMiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE4MDAwMDAwMDB9.signature"
    payload = decode_jwt_payload(sample_token)
    print("Decoded JWT Payload:", payload)
    print("Is Token Expired?", is_token_expired(payload))
