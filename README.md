# Interactive Registration Form
A modern, secure, and interactive user registration system built with Django, and Bootstrap 5. This project features real-time password strength validation, server-side error handling, and a clean UI.

### Key Features

Robust Validation: Server-side checks for email formats and matching passwords.

Security First: Built-in protection against CSRF (Cross-Site Request Forgery).

Responsive Design: Styled with Bootstrap 5 for mobile and desktop compatibility.

User Feedback: Toast-style success and error messages using Django's Messages framework.

### Technical Stack
Backend: Python 3.x, Django 5.x

Frontend: HTML5, Bootstrap 5

Database: SQLite (Default)

### Installation & Setup
Follow these steps to get the development environment running:

1. Clone the repository and Navigate
```
git clone https://github.com/yourusername/Form.git
cd Form
```
2. Set Up Virtual Environment
```
python -m venv venv
```
### Activate on Windows:
```
venv\Scripts\activate
```
### Activate on Mac/Linux:
```
source venv/bin/activate
```
3. Install Dependencies
```
pip install django
```
4. Database Migrations
Apply the initial migrations to set up the Django database schema.
```
python manage.py migrate
```
5. Run the Server
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/accounts/register/ in your browser.

### Project Structure
```
Form/
├── manage.py
├── forms/          # Project settings
│   ├── settings.py
│   └── urls.py
└── accounts/           # Your app
    ├── templates/
    │   └── accounts/
    │       └── register.html
    ├── forms.py        # Validation logic lives here
    ├── views.py        # Handles the "Interactive" part
    └── urls.py
```
### License
This project is open-source and available under the MIT License.


