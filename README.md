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

   <p align="center">
<img src="KANBAN PIC TO BE ADDED" width="100%" height="100%">
</p>

#
# Scope

## **Features**

### **Home Page**

1. **Navigation Bar**
   - The navigation bar appears on every page so users can easily navigate through the site.
   - Navigation bar has links for 'Home', 'Portfolio', 'Blog', 'Contact' and 'Login(superuser only)'. As a logged in superuser (site owner) there is nav link to 'Dashboard' and 'Login' is replaced by 'Logout'. The site's Logo acts as a universal link back to the main home/page across the site also.
<p align="center">
<img src="static/images/pp-logo.PNG" width="100%" height="100%">
</p>
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

  <p align="center">
<img src="static/images/PPFooterStrip.PNG" width="100%" height="100%">
</p>

   - External links are generated dynaically for Portfolio entries and populate in the Portfolio detail pages, these take the browser to live deployments of the site being showcased.  The footer currently also has a link to the site owners Github profile.

2. **Landing Page Banner Area - Portrait, Bio, Buttons with Swirling Background**
   - The landing area features a screen with a Welcome, a portrait photo of myself as the site and business owner, a quick intro text to orient the user and a few immediate calls to action - Download CV (Button) and Contact (Button). The backfrop uses houdini CSS rotating gradient styling to form an attractive feature, in otherwise blank space, facilitating an uncluttered yet attractive appearance.

  <p align="center">
<img src="static/images/pp-landingpage.PNG" width="100%" height="100%">
</p>

3. **Testimonials Section - Slider of promotional reviews**
   - The Testimonials sections is placed directly below the banner area to inspire early confidence in the visitor. The use of a manual slider encourages engagement and gives the reader the choice of time it taskes to read each review, as opposed to the use of an automated scrolling 'conveyor belt' of reviews. These have a personable and human quality, being from individuals.

    <p align="center">
<img src="static/images/pp-testi.PNG" width="100%" height="100%">
</p>

4. **Certificates Section - Manual slider of visible accreditations**
   - As with the Testimonials, manual slider lets users peruse at their own pace. The certificates being placed here attempt to reinforce a growing sense of confidence in the reader as they scroll down the page. These show more formal kinds of recognition.

    <p align="center">
<img src="static/images/pp-certi.PNG" width="100%" height="100%">
</p>

5. **Featured Work Section - Clickable Briefs with images of completed projects**
   - This is a list view of the portfolio projects currently on the site. These feature an image, clickable (and hoverable) links to more details about that project on its own page for further reading and exploration via external links there.

    <p align="center">
<img src="static/images/pp-features.PNG" width="100%" height="100%">
</p>

6. **Skills Section - Icons and Labelled Progress Bars**
   - This section shows the most pertinent tech stack of the site owner. Icons of the individual technologies are used as an attractive 'key' to the left of the labelled progress bars to the right. These are updateable in admin area as the site owner's skills change and develop. These aim to attractively give an honest portrayal of tech abilities, which may be of especial importance to recruiters looking at the site, so that their expectations are realistic when contacting.

    <p align="center">
<img src="static/images/pp-skills.PNG" width="100%" height="100%">
</p>

7. **Recent Posts - Slider view of Blog posts currently available**
   - These tiles have clickable (and hoverable) links to articles. This feature is currently being used to convey information, a sense of the owner's personality and also offer details about services not currently covered in other areas of the site.

    <p align="center">
<img src="static/images/pp-recentposts.PNG" width="100%" height="100%">
</p>

### **Portfolio Page**
    - This page simply comprises an attractively staggered tiling layaout of the items that users can find out more about by clicking through to the details by hovering over the images which are each hoverable links in themselves. Images here are given more space than in the homepage list view, so that people can see the kind of aesthetic quality of the site owners recent projects, even if they do not want to know more about each one. If they do want to explore further they can click on them to read more into the projects and from there click to any of the sites that are currently live. 
    
    These provide links to detail view if users have not scrolled down the long homepage but rather gone straight towards Portfolio via the Navbar.

<p align="center">
<img src="static/images/pp-portipage.PNG" width="100%" height="100%">
</p>

### **Blog Page**
    - Almost identical to the Portfolio page this Blog page simply comprises an attractively staggered tiling layaout of the items that users can find out more about by clicking through to the details by hovering over the images which are each hoverable links in themselves. These links go to detail views if users have not scrolled down the long homepage but rather gone straight towards Blog via the Navbar. 
    
    Images here are given more space than in the homepage list view. From here, users who want to explore further can click on them to read the articles themselves. 

 <p align="center">
<img src="static/images/pp-blogspage.PNG" width="100%" height="100%">
</p>

### **Contact Page**
    - This page provides an attractive, yet simple form layout for users to be able to send a message and their contact details to the site owner, such as for making enquiries relating to hiring them for a project. There is also an upfront and obvious link providing alternative means of emailing the site owner, if that is preferable to the user. This hoverable link nactivates a 'mailto' html function, calling up the user's email provider as a window and populating the address bar of the email with the site owner's email address.

<p align="center">
<img src="static/images/pp-contactpage1.PNG" width="100%" height="100%">
</p>

<p align="center">
<img src="static/images/pp-contactpage2.PNG" width="100%" height="100%">
</p>

    Upon submission of the form a popup appears saying 'Thank you. I will be in touch soon.' to alert the user that submission has occured.

<p align="center">
<img src="static/images/popup-contactform.PNG" width="100%" height="100%">
</p>

### **Login Page**
    - This comprises a simple form for the site owner to fill in username and password which have been formerly set using:-
     ```console
     python3 manage.py createsuperuser
     ```
<p align="center">
<img src="static/images/pp-login.PNG" width="100%" height="100%">
</p> 