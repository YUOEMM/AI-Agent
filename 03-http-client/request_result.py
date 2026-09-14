from dataclasses import dataclass
from typing import Any

@dataclass
class RequestResult:
    success:bool
    status_code:int | None
    data:Any
    elapsed:float
    attempts:int
    error:Exception |None=None

if __name__ == "__main__":
    result = RequestResult(
    success=True,
    status_code=200,
    data={"message": "ok"},
    elapsed=0.35,
    attempts=1
)
    print(result)