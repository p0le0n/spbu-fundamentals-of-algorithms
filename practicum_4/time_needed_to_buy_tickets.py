from typing import Any

import yaml


def solve(tickets: list[int], k: int) -> int:
    num_of_seconds = 0
    s = len(tickets)
    while tickets[k] != 0:
        num_of_seconds += s
        for i in range(len(tickets)):
            tickets[i] -= 1
            if tickets[i] == 0:
                s -= 1
    return num_of_seconds


if __name__ == "__main__":
    with open("time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        tickets_original = c["input"]["tickets"].copy()
        res = solve(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {tickets_original}. Output: {res}. Expected output: {c['output']}")