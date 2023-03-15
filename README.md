<h1>CS 816 - Software Production Engineering</h1>
<h2>Mini Project - Scientific Calculator with DevOps</h2>
<h3>Problem Statement</h3><br/>
Create a scientific calculator program with user menu driven operations<br/>
● Square root function - √x<br/>
● Factorial function - x!<br/>
● Natural logarithm (base е) - ln(x)<br/>
● Power function - x^b<br/>

<h2>DevOps tool chain</h2>
You can use any set of DevOps tool chains you want, but the pipeline would be the same.<br/>
The pipeline includes<br/>
1. Using a source control management tool - like GitHub, GitLab, BitBucket etc<br/>
2. Testing - test your code using either JUnit, Selenium, PyUnit and many more<br/>
3. Build - build your code using tool like Maven, Gradle, Ant and many more<br/>
4. Continuous Integration - Continuous integrate your code using tool like Jenkins,
GitLab CLI, Travis CLI, and many more<br/>
5. Containerize - Containerize your code using Docker.<br/>
6. Push your created Docker image to Docker hub.<br/>
7. Deployment - Do configuration management and deployment using either Chef,
Puppet, Ansible, Rundeck. Using these do configuration management and pull your
docker image and run it on the managed hosts.<br/>
8. For Deployment you can either do it on your local machine or on Kubernetes cluster
or OpenStack cloud. You can also use Amazon AWS or Google Cloud or some other
3rd party cloud.<br/>
9. Monitoring - for monitoring use the ELK stack. Use a log file to do the monitoring.
Generate the log file for your mini project and pass in your ELK stack.<br/>

<h2>Submission</h2>
● You can create a command line application or web application totally up to you<br/>
● You can use any language to implement this project, example - Java, C, Python, C++
and many more<br/>
● Create a report explaining each step.<br/>
● Report includes:<br/>
○ What and Why of DevOps?<br/>
○ Tools used<br/>
● Each step explanation includes<br/>
○ A Brief about step, example Source Control Management and tool used<br/>
○ Explain - setup to the tool and any configurations that had to be done and
attach screenshots of it, example github push, commit, Jenkins credential
management, Ansible connection settings, Rundeck Job creation and many
more<br/>
○ Add the commands that were used<br/>
○ Explain all the steps done in that tool and attach screenshots of each step,
example GitHub Repo creation, Jenkins Pipeline creation and Docker Hub
repo creation, Kibana output and many more<br/>
○ Add links to your github repo, docker hub<br/>
○ Also add scripts to the configuration file like Dockerfile, ansible playbook,
rundeck xml, Jenkins pipeline script and if anything else<br/>
○ Screenshot of the scientific calculator application and its various operations<br/>
● Create a zipped folder with your RollNumber as folder name example MT2020xx.zip<br/>
● The folder contains, screenshot images, pdf file of the report with name as
MT2020xx.pdf<br/>
● Your project report should be in such a way that a naive person can easily reciprocate
those steps and produce the end result.<br/>
This project has to be done individually and all the reports will be checked
for plagiarism.<br/>
