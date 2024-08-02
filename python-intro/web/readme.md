# Creating Your First Flask Web Application

#### Objective:

Learn how to set up a basic web application using Flask that returns "Hello, World!" upon visiting the homepage.

#### Time to Code:

Approximately 30 minutes.

#### Prerequisites:

- Basic understanding of Python programming.
- Python installed on your computer.
- Familiarity with using the command line or terminal.

#### Tools and Materials Needed:

- Computer with Python installed.
- Text editor or IDE (Integrated Development Environment) of your choice.

#### Instructions:

##### Step 1: Setting Up Your Environment

1. **Install Flask**: If you haven't installed Flask, open your terminal or command prompt and run the following command:
   ```
   pip install Flask
   ```
   This command downloads and installs Flask and its dependencies.

2. **Create a Project Folder**: Create a new folder on your computer where your project will reside. This can be done through the file explorer or using the command line:
   ```
   mkdir my_flask_app
   cd my_flask_app
   ```

##### Step 2: Writing the Flask Application

1. **Create a New Python File**: In your project folder, create a new file named `app.py`. You can do this using your text editor or IDE.

2. **Add the Flask Code**: Open `app.py` in your text editor or IDE and paste the following code:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def index():
       return "Hello, World!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```
   This code creates a basic Flask application that returns "Hello, World!" when the root URL is accessed.

##### Step 3: Running Your Flask Application

1. **Start the Flask Application**: With your terminal or command prompt open in the project folder, run the application by executing:
   ```
   python app.py
   ```
   If everything is set up correctly, Flask will start a local web server.

2. **Visit Your Application**: Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see "Hello, World!" displayed on the page.

##### Step 4: Exploring Further

1. **Understanding the Code**: Review the code in `app.py` to understand how Flask routes HTTP requests to functions.

2. **Experimenting with Flask**: Try modifying the return value of the `index` function or add new routes to see how they affect your application.

#### Conclusion:

Congratulations! You've successfully created and run a basic Flask application. Flask is powerful yet simple to use, making it a great choice for developing web applications in Python. As you become
more comfortable with Flask, you can explore its extensive documentation to learn about more complex features like templates, form handling, and database integration.

#### Additional Resources:

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Python Documentation](https://docs.python.org/3/)
- Online tutorials and courses for web development with Flask.

### Evaluation:

- Verify that the application runs successfully and displays "Hello, World!" when accessed via a web browser.
- Encourage experimentation with the Flask application by modifying routes and return values.

This guide should provide a comprehensive introduction to creating a simple web application with Flask, geared towards beginners.