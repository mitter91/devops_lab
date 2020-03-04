DevOps Lab 2020 (January-April)
Homework4: Artsemi Yoursh

Description: <br>
This app outputs next information: 
- html url of repository by default
- Number of forks with -f key
- Number of subscribers with -s key
- Number of opened issues with -i key
- Creation date and time with -t key
- SSH link of repository with -ssh key

Outputs data in terminal.

How it works: <br>
Application recieves two parameters:<br>
- Enter the name of repository owner after key -o or --owner
- Enter the repository name after key -r or --repo

It combines data into a link and uses it to receive the information.

Defaults (if keys not entered):
-o alenaPy
-r devops_lab

How to setup: <br>
Clone the repo and navigate to this folder.

```bash
# to install
 pip pr-stats .
 pr-stats

Helpfile: <br>
usage: pr-stats [-h] [-f] [-s] [-i] [-t] [-ssh] [-o OWNER] [-r REPO] [-v]

Greetings

optional arguments:
  -h, --help            show this help message and exit
  -f                    Outputs number of forks
  -s                    Outputs number of subscribers
  -i                    Outputs number of opened issues
  -t                    Outputs creation date and time
  -ssh                  SSH link for work
  -o OWNER, --owner OWNER
                        Repository owner name.
  -r REPO, --repo REPO  Name of repository.
  -v, --version         show program's version number and exit

