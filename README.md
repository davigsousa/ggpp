# ggpp - An Useful g++ Interface

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

"ggpp" is a simple g++ interface made with python3, it is useful to run C/C++ code in only one command.<br>
So, instead of:<br>
`g++ example.cpp -o example`<br>
`./example`<br>
And sometimes you don't want the compiled file. So, you also do:<br>
`rm -rf example`<br>
All theses steps, can be reduced with ggpp to:<br>

```
ggpp example.cpp
```

And you will run your C/C++ code without (optionally) leaving a compiled file on the folder.<br>

## Getting Started <a name = "getting_started"></a>

Install ggpp is very simple.

### Prerequisites

You will need **python3** installed on your PC.<br>
For Python 3 installation, download on the [official page](https://www.python.org/downloads/).<br>

- Python 3 is already installed on the most linux distributions.<br>
  Try run "`python3`" on your shell.

As the ggpp is a **g++** interface, you will need it installed too.

As a plus, if you want to copy the content of you C/C++ code automatically after ran it, you will need **xclip** installed on linux. <br>
For install it, you can follow this [useful guide](https://linoxide.com/linux-how-to/copy-paste-commands-output-xclip-linux/). <br>
On Windows, to copy the content, you don't need any prerequisites.

### Installing

Download or clone this repository

```
git clone https://github.com/davigsousa/ggpp.git
```

Then, open the repository folder

```
cd ggpp
```

And run pip3 to install the package.

```
pip3 install .
```

Now, restart your shell and you will be able to use ggpp, try:

```
ggpp --help
```

## Usage <a name = "usage"></a>

You can run your C/C++ code,<br>
just passing the filename as first argument. On Windows, you need file path, like: .\targetfile.cpp <br>

```
ggpp targetfile.cpp
```

You can also pass arguments to the g++ just passing in the end.

```
ggpp targetfile.cpp -Wall -H
```

Currently, there are two arguments to configure ggpp,<br>
they are "-c" or "--clip" to copy file content to the clipboard (xclip is required on linux), <br>
And "-nr" or "--noremove" to make ggpp do not remove the compiled file.

Usage:

```
ggpp example.cpp -c -nr
```
