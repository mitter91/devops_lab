
DevOps Lab 2020 (January-April)
Homework3: Artsemi Yoursh

Description: <br>
This app outputs next information: 
- Timestamp
- % of CPU load
- % of disk usage
- % of usage virtual memory
- IO information
- network packets sent

And redirect information to json/txt (output.<json/txt>) file in your current directory.

How it works: <br>
Application recieves two parameters:<br>
- Output file format: txt or json. Default - txt
- Time interval. Default - 5 mins

```bash
# for help
snapshot -h (--help)
# for run by default
snapshot 
# takes snaphosts every 3 mins and put it into json file
snapshot json 3
# takes snaphosts every 1 min and put it into txt file
snapshot txt 1
```

How to setup: <br>
Clone the repo and navigate to this folder.

```bash
# to install
 pip install .
 snapshot
