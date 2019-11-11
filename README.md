# CCPP - A Simple g++ Interface

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

"ccpp" is a simple g++ interface made with python3, it is useful to run C/C++ code in only one command.<br>
So, instead of:<br>
`g++ example.cpp -o example`<br>
`./example`<br>
And sometimes you don't want the compiled file. So, you also do:<br>
`rm -rf example`<br>
All theses steps, can be reduced with ccpp to:<br>

```
ccpp example.cpp
```

And you will run your C/C++ code without (optionally) leaving a compiled file on the folder.<br>

## Getting Started <a name = "getting_started"></a>

Install ccpp is very simple.

### Prerequisites

You will need **python3** installed on your PC.<br>
For Python 3 installation, download on the [official page](https://www.python.org/downloads/).<br>

- Python 3 is already installed on the most linux distributions.<br>
  Try run "`python3`" on your shell.

As the ccpp is a **g++** interface, you will need it installed too.

As a plus, if you want to copy the content of you C/C++ code automatically after ran it, you will need **xclip** installed. <br>
For install it, you can follow this [useful guide](https://linoxide.com/linux-how-to/copy-paste-commands-output-xclip-linux/).

### Installing

Download or clone this repository

```
git clone https://github.com/davig-sousa/ccpp.git
```

Then, open the repository folder

```
cd ccpp
```

And run install.sh

```
chmod +x install.sh && ./install.sh
```

Now, restart your shell and you will be able to use ccpp, try:

```
ccpp --help
```

## Usage <a name = "usage"></a>

You can run your C/C++ code,<br>
just passing the filename as first argument.<br>

```
ccpp targetfile.cpp
```

You can also pass arguments to the g++ just passing in the end.

```
ccpp targetfile.cpp -Wall -H
```

Currently, there are two arguments to configure ccpp,<br>
they are "-c" or "--clip" to copy file content to the clipboard (xclip is required), <br>
And "-nr" or "--noremove" to make ccpp do not remove the compiled file.

Usage:

```
ccpp example.cpp -c -nr
```
