## bigdata-pipeline

##Ingestor

##Druid


*Setting up Imply (Druid, Tranquility, Plywood, Pivot) on AWS Instance*

1. Change directories to the location of the private key file (.pem file) that was used to launch the instance.
2. Use the chmod command to ensure private key file isn’t public. 
  * Ex: `chmod 400 /path-to/pipeline.pem`
3. ssh into your instance. Specify .pem file as well as your unique public DNS name, shown below.
  * Sample ssh command: `ssh -i /path-to/pipeline.pem your-public-dns.computer.amazonaws.com`
4. If the instance asks if you are sure you want to continue connecting, enter yes.
5. To run Druid, Tranquility and all the other associated tools, we need Java 8 JDK. Check if Java 8 JDK is installed on your instance. (`java -version`)
6. If not, visit:  [Java JDK Download](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) to find the appropriate Java JDK. Accept the License Agreement, but instead of downloading onto your local machine, right-click and copy the link of the download. 
7. Install and cd into the Imply package
  * `curl -O http://static.imply.io/release/imply-1.3.0.tar.gz`
  * `tar -xzf imply-1.3.0.tar.gz`
  * `cd imply-1.3.0`
8. Check that you have the following packages: 
  * bin/*, conf/*, conf-quickstart/*, dist/*, quickstart/*
9. Exit the Imply directory. 
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install python-software-properties
