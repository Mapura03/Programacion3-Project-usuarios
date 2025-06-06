import csv
import os
from typing import List, Optional
from model.person import Person
from model.tree import TreeN
from model.typedoc import Typedoc
from model.location import Location

# ----------------------------
# Instancia global del servicio
# ----------------------------
person_service_instance = None

def set_person_service(service):
    global person_service_instance
    person_service_instance = service

def get_person_service():
    return person_service_instance

# ----------------------------
# Servicio de Personas con persistencia CSV
# ----------------------------
class PersonService:
    def __init__(self, csv_path: str = "data/persons.csv"):
        self.csv_path = csv_path
        self.tree = TreeN()
        self._load_from_csv()

    def _load_from_csv(self):
        if not os.path.exists(self.csv_path):
            return
        with open(self.csv_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                person = Person(
                    id=row["id"],
                    name=row["name"],
                    lastname=row["lastname"],
                    age=int(row["age"]),
                    gender=row["gender"],
                    typedoc=Typedoc(
                        code=int(row["typedoc_code"]),
                        description=row["typedoc_description"]
                    ),
                    location=Location(
                        code=int(row["location_code"]),
                        description=row["location_description"]
                    )
                )
                self.tree.create_person(person)

    def _save_person_to_csv(self, person: Person):
        file_exists = os.path.exists(self.csv_path)
        with open(self.csv_path, mode="a", newline="", encoding="utf-8") as f:
            fieldnames = [
                "id", "name", "lastname", "age", "gender",
                "typedoc_code", "typedoc_description",
                "location_code", "location_description"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "id": person.id,
                "name": person.name,
                "lastname": person.lastname,
                "age": person.age,
                "gender": person.gender,
                "typedoc_code": person.typedoc.code,
                "typedoc_description": person.typedoc.description,
                "location_code": person.location.code,
                "location_description": person.location.description
            })

    def _rewrite_csv(self, persons: List[Person]):
        with open(self.csv_path, mode="w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "id", "name", "lastname", "age", "gender",
                "typedoc_code", "typedoc_description",
                "location_code", "location_description"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for person in persons:
                writer.writerow({
                    "id": person.id,
                    "name": person.name,
                    "lastname": person.lastname,
                    "age": person.age,
                    "gender": person.gender,
                    "typedoc_code": person.typedoc.code,
                    "typedoc_description": person.typedoc.description,
                    "location_code": person.location.code,
                    "location_description": person.location.description
                })

    def create_person(self, person: Person, parent_id: Optional[str] = None) -> bool:
        success = self.tree.create_person(person, parent_id)
        if success:
            self._save_person_to_csv(person)
        return success

    def get_all_persons(self) -> List[Person]:
        return self.tree.get_persons()

    def update_person(self, id: str, updated_person: Person) -> bool:
        updated = self.tree.update_person(id, updated_person)
        if updated:
            persons = self.get_all_persons()
            self._rewrite_csv(persons)
        return updated

    def delete_person(self, id: str) -> bool:
        deleted = self.tree.delete_person(id)
        if deleted:
            persons = self.get_all_persons()
            self._rewrite_csv(persons)
        return deleted

    def get_persons_with_adult_child(self) -> List[Person]:
        return self.tree.get_persons_with_adult_child()

    def filter_by_location_typedoc_gender(self, location_code: int, typedoc_code: int, gender: str) -> List[Person]:
        return self.tree.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)

    def get_persons_by_location(self, location_code: int) -> List[Person]:
        return self.tree.get_persons_by_location(location_code)

    def get_person_by_id(self, person_id: str) -> Optional[Person]:
        return self.tree.get_person_by_id(person_id)
