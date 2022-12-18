Setting up Database with aws rds 

	Connect with ssh and setup env variable
	
$ eb ssh
$ sudo su -
$ export $(cat /opt/elasticbeanstalk/deployment/env | xargs)
$ source /var/app/venv/*/bin/activate
$ python3 /var/app/current/manage.py <command name>


(for admin site)
uername: rafat
password: 7898788

