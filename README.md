Real buy is a real estate management web app. Follows MVT architecture.

**Features included:**
1. Property CRUD
2. Authentication( Custom and Social)
3. User Profile Create and Update
4. Contactus
5. Maps Integration
6. Multi Parameter Property search
7. Shortlisting and Notification
8. IBM Watson chatbot
9. Google Analytics
10. Analytics and Visualisation along with role based access
11. Text search without MySQL

**To run the application:**
1. Clone the project using git clone command
2. Update settings.py with your credentials(AWS details, DB Credentials, Email Credentials...)
3. Run `python manange.py makemigrations` and then `python manage.py migrate` for applying those migrations.
4. Run `python manage.py runserver`
5. To access admin pannel run `python manage.py createsuperuser` and set a username, password.

**Tech Stack Used**
Django, Django REST Framework, HTML5 and CSS3, Javascript(ES6), Bootstrap 4, Jquery, Jinja2, Amazon S3, Google Maps API, MapBox API, PostgreSQL, Pandas & Plotly, IBM Watson, Django Channels, Google Analytics Platform


**API docs:**
https://documenter.getpostman.com/view/11431269/TVejg9n7

**Deployed Website**
https://realbuy-demo.herokuapp.com/

**Database Design**
https://app.dbdesigner.net/designer/schema/0-real_buy
