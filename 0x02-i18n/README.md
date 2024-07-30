# Flask Internationalization (i18n) Project

This project demonstrates how to set up and use internationalization (i18n) in a Flask application. The application supports multiple languages and can infer the locale and timezone based on various factors such as user settings and URL parameters.

## Project Structure

- `0-app.py`: Basic Flask app with a simple homepage.
- `1-app.py`: Flask app with basic Babel setup for language support.
- `2-app.py`: Flask app that determines the locale from the request.
- `3-app.py`: Flask app with parameterized templates for localization.
- `4-app.py`: Flask app that allows locale to be forced via URL parameters.
- `5-app.py`: Flask app with mock user login functionality for locale and timezone.
- `6-app.py`: Flask app that uses user settings for locale.
- `7-app.py`: Flask app that infers appropriate timezone for the user.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/clarksonlawson/alx-backend.git
   cd alx-backend/0x02-i18n
