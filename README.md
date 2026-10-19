# Mini Git Version Control

A minimal version control system implemented from scratch in Python to explore the core concepts behind Git and understand how version control works under the hood.

## Overview

The goal of this project is to build a simplified version control system while learning about repository management, object storage, staging, commits, and branches.

Rather than relying on Git internally, the core mechanisms are implemented as part of the project.

## Tech Stack

- Python
- `argparse` for command-line argument parsing
- `pathlib` for filesystem operations
- `json` for the initial staging index implementation

### Prerequisites

Python 3.10 or later.

### Run the CLI

Clone the repository and navigate to the project directory.

Display available commands:

```bash
python src/main.py --help