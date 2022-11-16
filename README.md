# QA-DevOps-Fundamental-Project- MCQ App: 
This repository contains my deliverable for the QA devops fundamental project.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief: 
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:

![app structure](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/app%20design.PNG)

## App Design:
I have chosen to build a simple blog, which allows users to write a post that has a title, when it was created and the text itself (create functionality). Users can also see all the post created (read functionality), update (update functionality) the posts and delete posts (delete functionality). The database for the MVP for this project comprises a Users table and an Post table. Each user can have multiple posts posted in the blog (one-to-many relationship). The ERD for this MVP is shown below: 

![ERD](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/UML%20App%20Diagram.jpg)

The goal for the future is to implement a more complete set of options for the users to be able to add more features to their posts like embbeded images, videos or a live chat.

## CI Pipeline:  
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. These were project tracking, version control, development environment and build server. For project tracking Jira was used to create a project tracking board. Items were assigned story points, acceptance criteria and MoSCoW prioritisation, and moved from project backlog, to sprint backlog, to review and then complete as the project progressed. The state of the Jira board at the beginning of sprint one was:  

![jira](
https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/Jira.PNG
)  
The jira board can be accessed [here](https://diegusdeveloper.atlassian.net/jira/software/projects/BLOG/boards/3).

For version control, git was used, with the project repository hosted on github. Version control via git allows changes to the project to be made and committed whilst keeping the commit history for access to earlier versions. GitHub as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing. 

The development environment used was a python3 virtual environment (venv) hosted on a virtual machine running Ubuntu 20.04. Python is used as Flask is a python-based framework. A venv allows pip installs to be performed and the app to be run without affecting any conflicting pip installs on the same machine.