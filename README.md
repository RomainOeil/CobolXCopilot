# CobolXCopilot

**It is expected to run the command from the root of the Github repo**
**The programs have been tested on Fedora 34, some commands for install may be different depending on the OS used**

## Requirements

The Cobol language, necessary to compile and launch the original cobol program.
**Cobol: 3.1.2.0**
**Python: 3.9.13**
**Pytest: 8.4.1**


### Cobol

Check your cobol version using:

> cobc -v

If you don't have it, install using:

> sudo dnf install gnucobol

### Python

Check your python version using:

> python3 --version

If you don't have it, install using:

> sudo dnf install pyhton3

## Pytest (used for the test program)

Check your python version using:

> pytest --version

If you don't have it, install first pip:

> sudo dnf install pyhton3-pip

And then, install pytest:

> pip install pytest

## Running the programs

### Cobol program

To build the Cobol program, use this command in the terminal:

> ./cobol/build.sh

Permission may be needed (e.g., using zsh)

### Python program

To launch the program, use this command:

> python3 ./python/src/main.py

### Python test program

To launch the test program, use this command:

> pytest ./python/src/test_operations.py