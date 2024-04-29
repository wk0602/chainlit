from typing import Dict, Literal, TypedDict

from dataclasses_json import DataClassJsonMixin
from pydantic.dataclasses import Field, dataclass

import random

Provider = Literal[
    "credentials", "header", "github", "google", "azure-ad", "okta", "auth0", "descope"
]


class UserDict(TypedDict):
    id: str
    identifier: str
    metadata: Dict


# Used when logging-in a user
@dataclass
class User(DataClassJsonMixin):
    id = str(random.uniform(0, 100000000))
    identifier: str= Field(default=id)
    metadata: Dict = Field(default_factory=dict)

@dataclass
class PersistedUserFields:
    id: str
    createdAt: str


@dataclass
class PersistedUser(User, PersistedUserFields):
    pass
