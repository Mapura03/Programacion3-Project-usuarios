from fastapi import HTTPException, status


class PersonNotFoundException(HTTPException):
    def __init__(self, person_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with ID '{person_id}' not found."
        )


class EmptyTreeException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The tree is empty."
        )


class LocationNotFoundException(HTTPException):
    def __init__(self, location_code: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Location with code '{location_code}' not found."
        )


class TypeDocNotFoundException(HTTPException):
    def __init__(self, type_doc_code: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TypeDoc with code '{type_doc_code}' not found."
        )


class InvalidCSVFormatException(HTTPException):
    def __init__(self, filename: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid CSV format in file '{filename}'."
        )