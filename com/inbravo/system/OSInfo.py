# Script Name		: OSInfo.py
# Authors		    : {Amit Dixit after Forking the Git repo from 'geekcomputers'}
# Created		    : 10th August 2025
# Version		    : 1.0
# Usage			    : "python OSInfo.py"
# Dependencies		: platform module
# License		    : GNU General Public License v3.0
# Description		: Displays some information about the OS you are running this script on

import platform as pl

# A utility class for terminal text formatting with ANSI escape sequences.
# Provides color and style codes for text output.
class BColors:
    """Class for terminal text formatting with ANSI escape sequences."""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def format_text(text, color):
        """Formats the given text with the specified color."""
        return f"{color}{text}{BColors.ENDC}"

    @staticmethod
    def bold_text(text):
        """Formats the given text in bold."""
        return f"{BColors.BOLD}{text}{BColors.ENDC}"

# List of platform attributes to retrieve OS information
profile = [
    "architecture",
    # "linux_distribution",  # Removed in Python 3.8
    "mac_ver",
    "machine",
    "node",
    "platform",
    "processor",
    "python_build",
    "python_compiler",
    "python_version",
    "release",
    "system",
    "uname",
    "version",
]

for key in profile:
    if hasattr(pl, key):
        try:
            value = getattr(pl, key)()
            # Print the key in GREEN and the value in BLUE color
            print(f"{BColors.OKGREEN}{key}:{BColors.OKBLUE} {value}")
        except (AttributeError, TypeError) as e:
            print(
                f"{BColors.FAIL}{key}:{BColors.OKBLUE} Unable to retrieve information ({e})"
            )
