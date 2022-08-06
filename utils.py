import re
from typing import Iterator, List, Any


def construct_query(cmd: str, value: str, file: Iterator) -> List[Any]:
    if cmd == "filter":
        result = list(filter(lambda x: value in x, file))
        return result
    if cmd == "map":
        value = int(value)
        result = list([x.split()[value] for x in file])
        return result
    if cmd == "limit":
        value = int(value)
        result = list(file)[:value]
        return result
    if cmd == "sort":
        value = bool(value)
        result = list(sorted(file, reverse=value))
        return result
    if cmd == "unique":
        result = list(set(file))
        return result
    if cmd == "regex":
        regex = re.compile(value)
        result = list(filter(lambda x: regex.search(x), file))
        return result
    return []
