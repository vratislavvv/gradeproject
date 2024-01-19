# General

## What is folD?
Personal finance manager, that helps you understand your current financial situation. folD includes features such as adding your expenses & incomes, or viewing them in a chart!

## The idea
I wanted to create something that would actually help me, and I alway found banking apps kinda complicated + I wasn't able to see expenses from multiple account in one graph.

# Pages

## Authentification
Login- used for logging in
Register- used for registering new user

## Myapp
Dashboard- displays everything, incomes, expenses, data in chart, savings & investments, balance, etc. 
Add expense- used for adding expenses and flushing them
Add earnings and assets- used for adding incomes, savings & investments and flushing them 
Settings- used for logging out of the application and reseting data in application.

# Desing

## Logo
Picture I use as a logo was not made by me, it is a canva template which I liked a lot and you can find the creator [here](https://www.canva.com/p/cincin-emas/).

## Colors
As you might noticed, the colors are matching the logo. I just took the color codes from the logo and created a gradient that is displayed in the background. Later on, I picked color codes from the gradient, and added them to the script that is creating the graph.

# Technical documentation

## Technologies
Application is built using Python framework Django, which covers the whole backend side.
On the other side, for front end, I decided to use classic HTML & CSS. Besides these two, I also used free open-source JavaScript library called Charts.js, which covers the big chart on the dashboard.
Every piece of data is stored in sqlite3 database that is automatically created for you when you create django project.

## Backend structure
To start off, in the code, there are three main important folders. First one called folD which represents the project folder, and then 2 application folders. First application folder called *myapp*, and second one called *accessing*.

Let's start with the *accessing*. This app has only one and single purpose, and that is authentification. It is much safer to handle authentification this way than having everything in a single app. The authentification system is handled by Django user authentification system.

*Myapp* is basically for everything else. This app manages everything related to folD AFTER you log in, from dashboard, through adding pages, to settings tab.

## Frontend structure

For frontend, I have 2 folders inside both applications. One called static and one called templates.

Static folder is used for storing all static files (images, stylesheets, js scripts) and in templates folder I store HTML layouts and also, extended versions of them (pages!).



## Database structure

##
