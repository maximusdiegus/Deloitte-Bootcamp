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

## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   

![RA](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/risk%20assesment.PNG)  
Some of the control measures implemented in the project as a result of the risk assessment are as follows:  
* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.   

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.


## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed.

![build]()  
The coverage reports, showing what percentage of statements were included in the tests, were output as html files, which were archived post-build. The coverage report for the above build was:  

# The App:  
Upon navigating to the app the user is presented with the login page: 

![login](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/login.PNG)

The nav bar provides links which allow users to sign up,

![register](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/register.PNG)

or edit their password. 

![editpassword](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/edituser.PNG)

Once the user has logged in, this is what it is shown, the home page:
![home](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/home.PNG)

From here a user can see it's own posts:
![viewpost](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/viewpost.PNG)

Every post has their own option for updatin the information of the post or to delete the post itself.


Finally the user can add a new post and logout
![addpost](https://github.com/maximusdiegus/Deloitte-Bootcamp/blob/main/Project/Blog/utils/addpost.PNG)

which will redirect to the login page.

## Updates:
    Tests added

## Known Issues:
* A user cannot have their own posts for himself. it's a shared blog

## Future Work:
In future sprints, in addition to fixing the issues identified above, I would like to add a more featres for every post so the user an have more options for his posts. 
