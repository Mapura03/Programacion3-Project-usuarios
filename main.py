from fastapi import FastAPI
from controller.person_controller import router as person_router
from controller.typedoc_controller import router as typedoc_router
from controller.location_controller import location_router, set_location_service
from service.location_service import LocationService
from exception.handlers import register_exception_handlers

app = FastAPI()

# Initialize LocationService with CSV data
location_service = LocationService(csv_path="CSV/DIVIPOLA.csv")
set_location_service(location_service)

# Register routers
app.include_router(person_router, prefix="/api/v1/persons", tags=["Persons"])
app.include_router(typedoc_router, prefix="/api/v1/typedocs", tags=["TypeDocs"])
app.include_router(location_router, prefix="/api/v1/locations", tags=["Locations"])

# Register exception handlers
register_exception_handlers(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)