# Paper Replication Project

## Setup
You will need to be on Mac OS, Linux, or the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install).

First, install [Python 3.9.7](https://www.python.org/downloads/release/python-397/) onto your machine. Then install [direnv](https://direnv.net) and hook in into your shell. Then, `cd` into this directory, type `direnv allow`, and run:

```sh
pip3 install ./requirements.txt
```

This should make sure you have all the requisite dependencies to run the code here. Setting up a virtual environment by hand should work, too.

Optionally, if you want to generate the list of words related to sexuality, you'll need a C++ compiler. If you're on Mac OS, running:

```sh
cd code && clang++ find_adult_words.cpp
```

Should print the list of words in the ./code/raw/sexuality_similarity file.

## Testing
You can run all the unit tests for the project by running:

```sh
cd ./code && pytest
```
