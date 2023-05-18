# Learning Django

This is a simple Django project that demonstrates the usage of Django views, models, and templates. It includes several pages such as the home page, about page, services page, and contact page.

## [Link to the Website](https://learningdjango.pythonanywhere.com/)

## Project Structure

- **views.py**: Contains the view functions for different pages.
- **models.py**: Defines the database models.
- **base.html**: The base template that other templates extend.
- **about.html**: The template for the about page.
- **contact.html**: The template for the contact page.
- **index.html**: The template for the home page.
- **services.html**: The template for the services page.

## Installation

To run this project, follow these steps:

1. Clone the repository

   ```bash
   git clone https://github.com/Hardvan/Learning-Django
   ```

2. Change to the project directory

   ```bash
   cd Learning-Django
   ```

3. Create a virtual environment

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment

   - On Windows, run:

   ```bash
   .venv\Scripts\activate.bat
   ```

   - On Linux or macOS, run:

   ```bash
     source .venv/bin/activate
   ```

5. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations

   ```bash
   python manage.py migrate
   ```

7. Run the development server

   ```bash
    python manage.py runserver
   ```

8. Open your browser and navigate to <http://localhost:8000> to see the application.

## Usage

The project provides the following pages:

- **Home**: Displays a carousel of images and some information about the ice creams.
- **About**: Provides information about the company.
- **Services**: Shows a list of services offered.
- **Contact**: Allows users to submit a contact form that is stored in the database.

## Deployment

The website is deployed on [PythonAnywhere](https://www.pythonanywhere.com/).
