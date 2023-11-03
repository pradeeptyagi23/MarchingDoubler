Description:
This script generates a marching doubler series as specified in the problem description.

Execution instructions:
1. Clone this repo using git clone https://github.com/pradeeptyagi23/MarchingDoubler.git
2. cd to MarchingDoubler
  a. Standalone execution
   The script can be executed on a commandline with where python interpreter is install. Ideally it requires python version 3.9 or greater
   It takes run length, no. of terms and output file name as command line arguments.
   If any of it is not provided, the script will prompt user for the same.
  Example execution:
```python
python marching_doubler.py --rlen 5 --terms 10 --ofile test
```
Above command will create the series for a run length of 5 until the total terms are met , and will write to the file test in the current directory

  b. Containerized execution using Docker
  The folder contains a Dockerfile. Once cd into the folder, execute below command to create an image that can then run as a container on any system with docker installed
  ```python
  docker build -t generatorpy .
```
This creates an image and tags it as 'gereratorpy' . 
This image can then be run as a container with following command.
```python
docker run -v ${PWD}:/app -i generatorpy --runlen 5 --terms 10 --ofile test
```
The above command will write to the test file in the current directory of the host.


