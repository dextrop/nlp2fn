# Python Automation Made Simple: [nlp2fn](https://pypi.org/project/nlp2fn/)

Welcome to `nlp2fn`, a seamless and intuitive software tool for Python automation. With the ability to load and read Python functions from any specified location, `nlp2fn` brings all your automation tasks together. Whether your functions reside in local directories or remote servers, `nlp2fn` fetches, loads, and prepares them for execution — as simple as a statement.


## The Magic of nlp2fn

A typical function for `nlp2fn` follows this format:

```python
# Write you execute statement, this shall be an 
# input by user to execute your events, make sure all the 
# parameters that are required by event is properly captured with {param_name}.
statement = "download {link} to {output_dir}"


# This shall be the main function for your event. once 
def execute(args):
    file = args[0]
    output_dir = args[1]
    
    # Complete the function.
    return True
```

The `execute` function is the heart of the operation where the actual task takes place.

## Quick Start Guide

Here's how to install and get started with [`nlp2fn`](https://pypi.org/project/nlp2fn/):

```bash
pip install nlp2fn
```

Next, add the source directory where your Python functions are located:

```bash
nlp2fn set-source local /path/to/directory
```

or 

```bash
nlp2fn set-source git https://github.com/{githubid}/{repo}
```

make sure repo is public.


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

## Events

- Langchain Automations : https://github.com/dextrop/evt-langchain
- https://medium.com/@askjennie/creating-your-own-automation-library-with-nlp2fn-6657b1276361
