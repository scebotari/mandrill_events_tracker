from fastapi import APIRouter, HTTPException, Request, Body, BackgroundTasks

import hashlib
import hmac
import base64
import time

from background_workers import batch_processor

router = APIRouter()

# Keeping check_signature as a Dependency allows to use it for authorizing
# all methods for current router
async def check_signature(request: Request = None):
  signature = hmac.new(
    b'test-api-key',
    bytes(str(request.url), 'UTF-8'),
    hashlib.sha1
  )
  signature = base64.b64encode(signature.digest())
  signature = signature.decode("utf-8")

  if request.headers['x-mandrill-signature'] != signature:
    raise HTTPException(status_code=400, detail="Signature check failed")

@router.post("/webhook")
async def mandrill_webhook(
  batch_worker: BackgroundTasks,
  batch: list = Body(dict)
):
  batch_worker.add_task(batch_processor.process_events, batch)
  return 'Payload accepted for background processing'
