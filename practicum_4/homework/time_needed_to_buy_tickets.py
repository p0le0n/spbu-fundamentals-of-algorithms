from typing import Any

import yaml


def solve(tickets: list[int], k: int) -> int:
    tickets_ = tickets.copy()
    num_of_seconds = 0
    s = len(tickets_)
    while tickets_[k] != 0:
        num_of_seconds += s
        for i in range(len(tickets_)):
            tickets_[i] -= 1
            if tickets_[i] == 0:
                s -= 1
    return num_of_seconds


if __name__ == "__main__":
    with open("../time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = solve(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")