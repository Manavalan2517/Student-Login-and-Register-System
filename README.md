# Student Login and Register



https://github.com/Manavalan2517/Student-Login-and-Register-System/assets/112639423/349bbd5a-cabb-45a1-ac29-f2b4cad253ad



This Python application provides a simple student login and registration system using Tkinter for the graphical user interface and MySQL for data storage.  It allows students to register with their personal and academic details and then log in to view their stored information.

## Features

* **User Registration:**  Students can register by providing their username, password, roll number, admission number, class, phone number, email, city, hobby, and 10th result.  Input validation ensures data integrity.
* **User Login:** Registered students can log in using their username and password. The system checks the entered credentials against the database and provides feedback.
* **Data Storage:**  User data is stored securely in a MySQL database.
* **Data Display:** Upon successful login, the system displays the student's details in a user-friendly format.
* **Login Attempt Limit:**  To prevent brute-force attacks, the system limits login attempts to three tries.
* **Password Hiding:** The password entry field uses a "show/hide" button for enhanced security.
* **Intuitive GUI:** The Tkinter-based interface provides a visually appealing and easy-to-use experience.

## Technologies Used

* **Python:** The core programming language.
* **Tkinter:** Python's standard GUI library.
* **MySQL:** Relational database management system for data storage.
* **`mysql.connector`:** Python library for connecting to MySQL.

## Installation and Setup

1. **Prerequisites:**
    * Ensure you have Python 3 installed.
    * Install the necessary libraries:
        ```bash
        pip install tkinter mysql-connector-python
        ```
    * Set up a MySQL server and create a database named `student`.  

2. **Database Configuration:**
    * Update the database connection details within the `Main.py` file:
        ```python
        mydatabase = mysql.connector.connect(host='localhost', user='root', password='Manoragavi-2517') 
        ```
    * Replace `'localhost'`, `'root'`, and `'Manoragavi-2517'` with your MySQL server credentials.

3. **Run the application:**
    ```bash
    python Main.py
    ```

## Usage

1. **Registration:**
   * Click the "REGISTER" button.
   * Fill in all the required fields in the registration form.
   * Click "SUBMIT" to register.

2. **Login:**
   * Enter your registered username and password.
   * Click the "LOGIN" button.

3. **View Details:**
   * Upon successful login, a new window will appear displaying your stored details.

## File Structure

* `Main.py`: The main Python script containing the application logic and GUI implementation.
* `images/`: Directory containing image files used in the GUI (ensure these are present).

## Future Improvements

* **Enhanced Security:** Implement more robust password hashing and salting.
* **Error Handling:**  Improve error handling and user feedback for database interactions.
* **User Management:**  Add features for administrators to manage student accounts.
* **Modern UI:** Consider using a more modern UI library for a more polished look and feel.


## Contributing

Contributions are welcome!  Please feel free to submit pull requests or open issues.
