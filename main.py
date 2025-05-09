from fastapi import FastAPI
from controller.location_controller import location_router, set_location_service
from service.location_service import LocationService

app = FastAPI()

# Initialize location service with CSV data
location_service = LocationService(csv_path="CSV/DIVIPOLA.csv")
set_location_service(location_service)

# Include routers
app.include_router(location_router)