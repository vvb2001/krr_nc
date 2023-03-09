import pydantic as pd

from robusta_krr.core.models.allocations import ResourceAllocations


class K8sObjectData(pd.BaseModel):
    cluster: str
    name: str
    container: str
    namespace: str
    kind: str | None
    allocations: ResourceAllocations

    def __str__(self) -> str:
        return f"{self.kind} {self.namespace}/{self.name}/{self.container}"

    def __hash__(self) -> int:
        return hash(str(self))