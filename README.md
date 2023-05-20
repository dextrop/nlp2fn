# nlp2fn: Python Automation Made Simple

Welcome to `nlp2fn`, a seamless and intuitive software tool for Python automation. With the ability to load and read Python functions from any specified location, `nlp2fn` brings all your automation tasks together. Whether your functions reside in local directories or remote servers, `nlp2fn` fetches, loads, and prepares them for execution — as simple as a statement.

## The Magic of nlp2fn

A typical function for `nlp2fn` follows this format:

```python
import os
import requests, shutil

# The function statement
statement = "download {link} to {output_dir}"

def execute(args):
    file = args[0]
    output = args[1]
    # Continue with the function to download the file to the output location.
    return True
```

The `execute` function is the heart of the operation where the actual task takes place.

## Quick Start Guide

Here's how to install and get started with `nlp2fn`:

```bash
git clone https://github.com/dextrop/nlp2fn.git
cd nlp2fn
pip install .
```

Next, add the source directory where your Python functions are located:

```bash
nlp2fn set source /path/to/directory
```

Ready to launch `nlp2fn` as a chatbot? Use this command:

```bash
nlp2fn run
```

To run a single statement, use the `exec` command:

```bash
nlp2fn exec -m "statement"
```

If you need to reset your sources, simply use the `reset` command:

```bash
nlp2fn reset
```

## Join the Development

We welcome your contributions! Feel free to submit pull requests and create issues on our [GitHub page](https://github.com/dextrop/nlp2fn/issues).

## Contact

For questions, suggestions, or any kind of discussion, feel free to open an issue on our GitHub page.

Embrace the simplification of Python automation with `nlp2fn`.
\