


###############################################################
To set up ansible controler and manage nodes follow below link :
###############################################################

https://www.linode.com/docs/guides/getting-started-with-ansible/#set-up-the-control-node



####################################################
To install maven on aws ec2 linux follow below steps :
####################################################

sudo wget https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
sudo yum install -y apache-maven
sudo yum install java-1.8.0-devel -y
sudo /usr/sbin/alternatives --config java #select java 8
sudo /usr/sbin/alternatives --config javac #select javac 8

add java path :

sudo vi /etc/profile

export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.342.b07-1.amzn2.0.1.x86_64"

export PATH=$PATH:$JAVA_HOME/bin


###################################
To install Git follow below steps :
###################################

- sudo yum update -y
- sudo yum install git -y

########################################
To install Terraform follow below steps :
########################################

- sudo yum install -y yum-utils
- sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
- sudo yum -y install terraform


