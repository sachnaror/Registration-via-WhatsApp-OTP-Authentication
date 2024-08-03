# WhatsApp OTP Authentication App

A Django web application for user registration and authentication with WhatsApp OTP confirmation. This project uses PostgreSQL as the database and integrates with a WhatsApp API (like Twilio) to send OTPs for verifying users.

## Features

- User Registration with OTP confirmation via WhatsApp
- User Login with verified credentials
- Secure password handling
- Unique username enforcement
- Dashboard access after successful login
- Comprehensive error handling and user feedback

## Prerequisites

- Python 3.12+
- Django 4.2+
- PostgreSQL
- A WhatsApp API provider (e.g., Twilio) account
- Git

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd whatsapplogin


Here's the content for your README.md file:

```markdown
# WhatsApp Login System

This project implements a user authentication system using WhatsApp for OTP verification.

## Setup

1. Clone the repository:
   ```
   git clone <repository_url>
   cd whatsapplogin
   ```

2. Set Up Virtual Environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL Database:
   Ensure PostgreSQL is installed and running. Create a new database:
   ```
   CREATE DATABASE watw;
   ```
   Update `settings.py` with your database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'watw',
           'USER': 'your_db_username',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Apply Migrations:
   ```
   python manage.py migrate
   ```

6. Run the Server:
   ```
   python manage.py runserver
   ```

7. Set Up WhatsApp API:
   - Set up an account with a WhatsApp API provider (e.g., Twilio).
   - Replace placeholder credentials in `utils.py` with your actual API details.

## Usage

1. Register a User:
   - Visit `/app1/register/`.
   - Enter your details (username, email, phone number, password).
   - An OTP will be sent to your phone via WhatsApp.

2. OTP Verification:
   - Enter the received OTP on the registration page.
   - Upon successful verification, the user is registered and redirected to the dashboard.

3. Login:
   - Visit `/app1/login/`.
   - Enter your verified username and password to log in and access the dashboard.

## Project Structure

```
whatsapplogin/
│
├── app1/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── app1/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── dashboard.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── utils.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Important Files

- `app1/models.py`: Contains the UserProfile model.
- `app1/views.py`: Handles the registration, login, and dashboard views.
- `app1/urls.py`: URL routing for the app.
- `app1/utils.py`: Contains `send_whatsapp_otp` function for sending OTPs.

## Security Considerations

- Passwords are securely hashed using Django's default authentication system.
- OTPs are randomly generated and should be securely handled.
- Use HTTPS in production for secure communication.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- Django Documentation
- Twilio API

## Contact

For further queries, please contact [Your Email].
```

To download this README.md file, you can copy the content above and save it as a file named `README.md` on your local machine. Alternatively, you can use a text editor to create a new file, paste the content, and save it as `README.md`.

Remember to replace placeholders like `<repository_url>`, `your_db_username`, `your_db_password`, and `[Your Email]` with actual values specific to your project before using or sharing this README.
