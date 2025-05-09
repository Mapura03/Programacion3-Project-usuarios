from typing import List, Optional
from pydantic import BaseModel
from model.person import Person


class NodeN(BaseModel):
    person: Person
    children: List["NodeN"] = []

    def add_child(self, child: "NodeN") -> None:
        self.children.append(child)

    def remove_child_by_id(self, id: str) -> bool:
        for i, child in enumerate(self.children):
            if child.person.id == id:
                self.children.pop(i)
                return True
        for child in self.children:
            if child.remove_child_by_id(id):
                return True
        return False


class TreeN(BaseModel):
    root: Optional[NodeN] = None

    def create_person(self, person: Person, parent_id: Optional[str] = None) -> bool:
        new_node = NodeN(person=person)
        if self.root is None:
            self.root = new_node
            return True
        if parent_id is None:
            self.root.add_child(new_node)
            return True
        return self.find_and_add_child(self.root, parent_id, new_node)

    def find_and_add_child(self, node: NodeN, parent_id: str, new_node: NodeN) -> bool:
        if node.person.id == parent_id:
            node.add_child(new_node)
            return True
        for child in node.children:
            if self.find_and_add_child(child, parent_id, new_node):
                return True
        return False

    def get_persons(self) -> List[Person]:
        if self.root is None:
            return []
        result = []
        self.traverse_tree(self.root, result)
        return result

    def traverse_tree(self, node: NodeN, result: List[Person]) -> None:
        result.append(node.person)
        for child in node.children:
            self.traverse_tree(child, result)

    def update_person(self, id: str, person: Person) -> bool:
        if self.root is None:
            return False
        return self.update_person_recursively(self.root, id, person)

    def update_person_recursively(self, node: NodeN, id: str, person: Person) -> bool:
        if node.person.id == id:
            node.person = person
            return True
        for child in node.children:
            if self.update_person_recursively(child, id, person):
                return True
        return False

    def delete_person(self, id: str) -> bool:
        if self.root is None:
            return False
        if self.root.person.id == id:
            if not self.root.children:
                self.root = None
                return True
            return False
        return self.root.remove_child_by_id(id)

    def get_persons_with_adult_child(self) -> List[Person]:
        if self.root is None:
            return []
        result = []
        self.find_persons_with_adult_child(self.root, result)
        return result

    def find_persons_with_adult_child(self, node: NodeN, result: List[Person]) -> None:
        has_adult_child = any(child.person.age >= 18 for child in node.children)
        if has_adult_child:
            result.append(node.person)
        for child in node.children:
            self.find_persons_with_adult_child(child, result)

    def filter_by_location_typedoc_gender(self, loc: str, td: str, g: str) -> List[Person]:
        if self.root is None:
            return []
        result = []
        self.filter_recursive(self.root, loc, td, g, result)
        return result

    def filter_recursive(self, node: NodeN, loc: str, td: str, g: str, result: List[Person]) -> None:
        if node.person.location.code == loc and node.person.typedoc.code == td and node.person.gender == g:
            result.append(node.person)
        for child in node.children:
            self.filter_recursive(child, loc, td, g, result)

    def get_persons_by_location(self, location: str) -> List[Person]:
        if self.root is None:
            return []
        result = []
        self.get_by_location_recursively(self.root, location, result)
        return result

    def get_by_location_recursively(self, node: NodeN, location: str, result: List[Person]) -> None:
        if node.person.location.code == location:
            result.append(node.person)
        for child in node.children:
            self.get_by_location_recursively(child, location, result)