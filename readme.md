# Photographer Portfolio on Django

Welcome to the Photographer Portfolio project built on Django! This portfolio website is designed to showcase a photographer's work and allow users to explore various features, including a portfolio page, blog, reviews, contact information, and an about page. The project also includes admin capabilities for managing content and configuration.

## Project Overview

### Features

- **Portfolio Page**: Users can view different categories and click on them to see photos within each category.
- **Blog Page**: Users can read blog posts by the photographer. The page includes pagination for easy navigation.
- **Contacts Page**: Users can view contact information and use a "Get in Touch" form to send emails.
- **Reviews Page**: Users can read and add reviews.
- **Admin Panel**: The photographer can manage categories, photos, and blog posts using the Django admin panel.

### Technologies Used

- **Django**: The web framework used for building the project.
- **JavaScript**: Used for features like scroll to top.
- **Django Templates**: Used for rendering data.
- **CSS**: Used for styling the website.
- **AWS S3 Storage (Previously)**: Initially used for saving static files and images.
- **Local Storage (Current)**: Switched to local storage on the server due to sufficient server space.

## Getting Started

To run this project, follow these steps:

1. Install project requirements.

   ```shell
   pip install -r requirements.txt

2. Set up a virtual environment (venv).

3. Create an `.env` file (See `example.env` for reference).

4. Run the Django development server.
   ```shell
   python manage.py runserver
5. Access the project in your web browser at `http://localhost:8000`.

## Note

The project initially used AWS S3 Storage for saving static files and images. However, it has since been switched to local storage on the server, as there is enough space to meet the photographer's needs.
