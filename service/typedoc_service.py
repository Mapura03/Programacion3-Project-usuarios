from model.typedoc import Typedoc
import pandas as pd
from typing import List

class TypedocService:
    def __init__(self, csv_path: str):
        self.typedocs_df = pd.read_csv(csv_path, encoding='latin1', sep=';')

    def get_all_typedocs(self) -> List[Typedoc]:
        return [
            Typedoc(code=int(row["code"]), description=row["description"])
            for _, row in self.typedocs_df.iterrows()
        ]

    def get_typedoc_by_code(self, code: int) -> Typedoc:
        match = self.typedocs_df[self.typedocs_df["code"] == code]
        if not match.empty:
            row = match.iloc[0]
            return Typedoc(code=int(row["code"]), description=row["description"])
        return None