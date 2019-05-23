#!/usr/bin/python3

import subprocess

instructions = [
  'sudo apt update',
  'sudo apt upgrade -y',
  'sudo apt install php nginx php-pgsql php-fpm',
  'sudo service apache2 stop',
  'sudo service nginx start',
  'sudo rm /var/www/html/*',
  'sudo cp ./index.php /var/www/html/index.php',
  'sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/old_default',
  'sudo cp ./nginx.conf /etc/nginx/sites-available/default',
  'sudo service nginx restart',
  'echo "\n should be finished?"'
]

for cmd in range(instructions):
  subprocess.call(cmd, shell=True)
