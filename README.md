DevOps Lab 2020 (January-April)
Homework4: Artsemi Yoursh

Description: <br>
This app outputs next information: 
- outputs file list of parent derictory
- outputs file list of recursively
- filtered by file extrnsion
- order file list by filename
- order file list by creation date

Outputs data in terminal.

How it works: <br>
- Enter the path after -p key
- one of parameteres -par or -rec is MANDATORY
- parameters -of and -od exclude eachother

If any key not entered:
	Error message that you need -par or -rec key

Defaults:
If path not entered): path = /home

How to setup: <br>
Clone the repo and navigate to this folder.

```bash
# to install
 pip install .
 
 use:
 filedir

Helpfile: <br>
usage: filedir.py [-h] [-par] [-rec] [-fe [FE]] [-of] [-od] [-p [PATH]]

Greetings

optional arguments:
  -h, --help            show this help message and exit
  -par                  MANDATORY: List of files from the parent directory
  -rec                  MANDATORY: List of files recursively
  -fe [FE]              File extention filter
  -of                   Order output by filename
  -od                   Order output by date of creation
  -p [PATH], --path [PATH]
                        Path. Default: /home

