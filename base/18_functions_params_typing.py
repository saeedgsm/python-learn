# پارامترها، *args، **kwargs و تایپ‌هینت‌ها
from typing import List, Dict, Optional

def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix} {name}"

print(greet("Ali"))
print(greet("Sara", prefix="Hi"))

def add_all(*nums: int) -> int:
    total = 0
    for n in nums:
        total += n
    return total

print(add_all(1, 2, 3, 4))

def build_user(name: str, **attrs: str) -> Dict[str, str]:
    data = {"name": name}
    data.update(attrs)
    return data

print(build_user("Ali", city="Tehran", job="Dev"))

def find_first_even(nums: List[int]) -> Optional[int]:
    for n in nums:
        if n % 2 == 0:
            return n
    return None

print(find_first_even([1, 3, 5, 8, 9]))

