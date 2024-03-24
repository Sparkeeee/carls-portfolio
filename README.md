<h1 align="center">c-sparks-fly.net</h1>                                      


<p align="center">
<img src="static/images/PPResponsive.PNG" width="600" height="100%">
</p>



Hello, welcome to the project's readme document.
This project utilises a full-stack framework, incorporating Django, Python, JavaScript, CSS, and HTML. My objective is to develop a responsive website that enables me, as the site owner, to perform CRUD operations to make updating my portfolio simple. This project is to be my own personal website to promote myself as a web developer.



**[Visit my website](https://my-portfolio-final-project-f3fce3db626e.herokuapp.com/)**

# Overview

This website is to act as major promotional point for me entering the market as a Full Stack Developer, it is to communicate value to visitors. The site is to be under construction for a while and the current state of the site represents the Minimum Viable Product (MVP) having been reached. It is a starting point for further development, with new features planned to help me organise my workflow in the back end. More content is to be added after some websites have been built for real world use (initially these websites will be built for free) and the blog articles have their full content in place. 

The website being built as a final project piece for a fullstack bootcamp is specified to require CRUD functionality. This is fulfilled here by making a gated dashboard (only available to superuser), where portfolio entries can be uploaded, edited and deleted as required. This is akin to functionality already present in django admin but, it is accessed faster and has a nicer UI. This aims to make the experience of updating the site both faster and more enjoyable and has set the stage for future dashboard functions to be added, such as To Do Lists.

# Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

#
# UX

For the UX planning I researched by web searching other people offering web developer services in Carmarthenshire. I decided to go with a clean, simple and personable approach, while showcasing some design abilities


The target market for 'c-sparks-fly.net' includes:

- Individuals wanting websites built.
- Small to medium sized businesses, whose requirements are most likely to fall within my skillset.
- Recruiters who may be visiting while scouting for potential employees.
- Other developers, who may mention the site to colleagues and this lead to networking or other opportunities.

These users will be looking for:

- A website that provides context and shows my ability as a developer.
- Examples of my work.
- The ability to contact me easily if they want to.
- A visually appealing experience.
- A user-friendly interface with intuitive navigation to access content and resources.
- The ability to post, comment and like events an provide feedback reviews.
- Links to explore my work further.


The website currently provides these features. The design is colorful without being overwhelming and suited to having good visibility on monitors and screens in a variety of lighting conditions. The site being database driven and with image static files being accessed by cloudinary has a fast load time.

## User Stories
These User stories have been used to help structure the direction of this project, to prioritise features and are also used later in this readme file as a basis for demonstrating testing, using these as core criteria.

- As a ** Site Owner** I can **provide my CV for download , so that ** it is easy for prospective employers to access.
- As a ** Site Owner** I can upload completed projects, so that ** I can show my ability**.
- As a Site Owner ** I can ** share my abilities and tech stack, so that prospective employers can see where I am at.
- As a Site Owner I can share my formal achievements, so that viewers can see proof of my learning.
- As a **client/co-worker ** I can share a positive experiences, so that **I can show appreciation and enhance public trust in Carl **.
- As a ** Site Owner** I can post articles, so that i can share my thoughts and interests..

- As a ** Site User** I can **upload my contact details and a message **, so that **I can be reached by Carl and explain my interest **.

#
# Scope

## **Features**

### **Home Page**

1. **Navigation Bar**
   - The navigation bar appears on every page so users can easily navigate through the site.
   - Navigation bar has links for 'Home', 'Portfolio', 'Blog', 'Contact' and 'Login(superuser only)'. As a logged in superuser (site owner) there is nav link to 'Dashboard' and 'Login' is replaced by 'Logout'. The site's Logo acts as a universal link back to the main home/page across the site also.
   - The navigation links appear in the nav bar to the right hand side on screens above 767px viewport widths. Below that width the navbar collapses into a 'hamburger' style toggle icon, which when clicked, calls a drop down style navigation menu to appear to the left of the viewport.
   - Further forms of Navigation outside of the NavBar itself are detail view pages for Blog articles and Portfolio entries, which are accessed from title based links that are dynamically generated from the relevant object's properties in the databse. The site owner in the Dashboard Page has a handy button 'Admin' which takes them to Django's built in admin area.
   - The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

   <p align="center">
<img src="static/images/NavDTStrip.PNG" width="100%" height="100%">
</p>
   <p align="center">
<img src="static/images/NavMobOpenPP.PNG" width="100%" height="100%">
</p>

   - Other links icludes email links in the sites footer bar and on the contact page. Clicking on the email links invokes a 'mailto' function that calls up options for which email provider the site user would like to use and populates the email services address bar with my email address to facilitate easy access to email.
   - External links are generated dynaically for Portfolio entries and populate in the Portfolio detail pages, these take the browser to live deployments of the site being showcased.  The footer currently also has a link to the site owners Github profile.

   <p align="center">
<img src="static/images/PPFooterStrip.PNG" width="100%" height="100%">
</p>