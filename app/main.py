from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import mail, map, payment,phonepe,phonepepy

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify allowed origins like ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Or specify like ["GET", "POST"]
    allow_headers=["*"],
)
# Include routers
app.include_router(mail.router, prefix="/api", tags=["Mail"])
app.include_router(map.router, prefix="/api", tags=["Map"])
# app.include_router(payment.router, prefix="/api", tags=["Payment"])
# app.include_router(phonepe.router, prefix="/api", tags=["Phonepe"])
# app.include_router(phonepepy.router, prefix="/api", tags=["Phonepepayment"])

@app.get("/")
async def root():
    return {"message": "Welcome to the combined FastAPI app"}
