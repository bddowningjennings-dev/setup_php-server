## This is a thing

1) create a new ec2 instance (Ubuntu 18.04)
2) remote in
```bash
  ssh -i *location of .pem* ubuntu@*aws ip*
```
3) clone this repo
4) fix index.php so that it has the ip and password
5) run the script
```bash
 ./script.py
```
6) check your aws ip
