from .classes.account import Account
from .logs_manager import Logger as log
import sys
from os.path import dirname, abspath
import os

from typing import List

def parse_accs(file_path) -> List[Account]:
    accounts = list()
    log.debug(f'accounts path: {file_path}')
    if os.path.isfile(file_path):
        lines = [line.strip().split(":") for line in open(file_path).readlines()]
    else:
        log.error("accounts.txt file not found!")
        close(1)
    # ^ reads every line from a file and splits into a :
    for line in lines:  # This variable cannot be referenced before assignment due to close()

        if len(line) in (2, 5):
            accounts.append(Account(*line))
        else:
            log.error(f"accounts.txt invalid account on line {lines.index(line) + 1}")

    log.debug("loaded accounts from file")
    if len(accounts) == 0:
        log.error("No accounts were loaded from file. Please check accounts.txt and try again.")
        sys.exit(0)
    return accounts


def close(code) -> None:
    log.input(f"Press enter to exit:")
    sys.exit(code)
