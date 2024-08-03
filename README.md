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
