from model.person import Person
from model.tree import TreeN
from typing import List, Optional

class PersonService:
    def __init__(self):
        self.tree = TreeN()

    def create_person(self, person: Person, parent_id: Optional[str] = None) -> bool:
        return self.tree.create_person(person, parent_id)

    def get_all_persons(self) -> List[Person]:
        return self.tree.get_persons()

    def update_person(self, id: str, updated_person: Person) -> bool:
        return self.tree.update_person(id, updated_person)

    def delete_person(self, id: str) -> bool:
        return self.tree.delete_person(id)

    def get_persons_with_adult_child(self) -> List[Person]:
        return self.tree.get_persons_with_adult_child()

    def filter_by_location_typedoc_gender(self, location_code: int, typedoc_code: int, gender: str) -> List[Person]:
        return self.tree.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)

    def get_persons_by_location(self, location_code: int) -> List[Person]:
        return self.tree.get_persons_by_location(location_code)