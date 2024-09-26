# Online Library Project 

### Technical Requirements

#### Models

1. **User** :

* Use Django's default user model to manage authentication.`title`

1. **Book** :

* `title`: CharField, up to 255 characters.
* `author`: CharField, up to 255 characters.
* `isbn`: CharField, unique, 13 characters.
* `summary`: TextField, optional.
* `genre`: CharField, up to 100 characters.
* `available`: BooleanField, indicates if the book is available for borrowing.

1. **Borrow** :

* `book`: ForeignKey to Book.
* `user`: ForeignKey to User.
* `borrow_date`: DateTimeField, auto_now_add=True.
* `return_date`: DateTimeField, optional.

#### Views and URLs

1. **User Views** :

* User registration, login, and logout.
* User profile page with a list of borrowed books.

1. **Book Views** :

* Full CRUD operations for the Book model.
* Search books by title, author, or genre.

1. **Borrow Views** :

* Create borrow records (only authenticated users can borrow books).
* Display the borrowing history of a user.
* Return books (update availability).

#### Admin Interface

1. Configure Django admin for the Book and Borrow models.
2. Add custom filters and search options.
3. Display borrowing information on the admin page for users.

#### Celery Tasks

1. Integrate Celery to send an email notification to the user when a borrow is created or a book is returned.

#### SQL Query Optimization

1. Optimize queries for GET views to minimize the number of database queries.

#### Tests

1. Write unit and integration tests for models, views, and services.
2. Include tests to verify query optimization and the correct functioning of Celery tasks.

#### Documentation

1. Provide a `README.md` file with instructions for setting up the development environment, running the application, and running tests.

#### Additional Instructions

* Use Django and Django REST Framework to develop the application.
* Use Class-Based Views (CBV) for the views.
* Use Django signals to update book availability and send notifications.
* Secure access to views with appropriate permissions.
* Include comments in your code to explain important parts.

### Deliverables

1. The source code of the Django application.
2. A `README.md` file with instructions for setting up the development environment, running the application, and running tests.
3. Migration files for the models.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
