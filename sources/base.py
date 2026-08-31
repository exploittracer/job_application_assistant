from dataclasses import dataclass
from typing import Optional


@dataclass
class JobPosting:

    source: str

    title: str

    company: str

    url: str

    description: str

    location: Optional[str] = None

    salary: Optional[str] = None

    date_posted: Optional[str] = None


class JobSource:

    name = "Base"

    def search(self, query: str, location: str):

        raise NotImplementedError