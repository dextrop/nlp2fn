# Python Automation Tool : nlp2fn

nlp2fn is a pioneering Python library that enables you to use simple English commands to execute Python code. This transformative tool leverages Natural Language Processing (NLP) to automate and streamline your development process. 

## Core Functionality

nlp2fn works by mapping English language statements to specific Python functions. When an NLP statement is invoked, nlp2fn triggers the corresponding function. Let's understand this by an example.

## Using nlp2fn: An Example

Let's dive into an example to see how easy it is to automate tasks with nlp2fn. We'll create a function to download files from a link to a specified directory. 

You'll first need to write your function and link it with an NLP statement, like this:

```python
import os
import requests, shutil

statement = "download {link} to {output_dir}"

def execute(args):
    file = args[0]
    output = args[1]
    if file.split(".")[-1] in ["jpg", "png", "jpeg"]:
        res = requests.get(file, stream=True)
        if res.status_code == 200:
            with open(output, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
    else:
        response = requests.get(file).text
        open(os.path.join(os.getcwd(), output), "w").write(response)
    return True
```

Once you've created your function, you can add it to your function gallery source. To do this, you'll need to install nlp2fn from pip and set the function source directory:

```shell
pip install nlp2fn
nlp2fn set source /path/to/directory
```

Now, you're all set to execute your function using nlp2fn.

```shell
nlp2fn run
```

When you run this command, you'll be prompted to enter your command:

```shell
What do you want me to do?
>> download https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv to output/biostats.csv
```

nlp2fn will then execute your command:

```shell
Executing download files
link: https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
output_dir: output/biostats.csv
```

And voila! Your file is downloaded to the specified directory.

**Use can also use the function in other way**

- Single Command
```
nlp2fn exec -m 'download https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv to output/biostats.csv'
```

## Conclusion

nlp2fn simplifies coding and automation, making it an invaluable tool for developers looking to streamline their workflows. It also opens up endless possibilities for customization, enabling developers to build their own unique automation gallery. So, what are you waiting for? Install nlp2fn today and transform the way you code!