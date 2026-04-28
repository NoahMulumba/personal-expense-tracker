# Personal Expense Tracker

#### Video Demo:
https://youtu.be/hRc9GjrwFMg

#### Description
This project is a personal expense tracker developed in Python that enables users to record, store, and analyze their everyday expenses using a simple command-line interface. The primary goal of the program is to provide an accessible and practical way for users to monitor their spending habits while demonstrating fundamental programming concepts taught in CS50P, such as functions, file input and output, error handling, and testing.

The program allows users to add expenses by entering a description, a category, and a monetary amount. Each expense is automatically timestamped with the current date and saved to a CSV file, ensuring that data persists across multiple executions of the program. By using a CSV file as the storage format, the project maintains a balance between simplicity and structure, allowing expense data to be easily read, written, and inspected outside the program if necessary.

In addition to recording expenses, the program provides functionality to display all previously entered expenses in a readable format. This allows users to review their spending history and better understand how their money is being allocated across different categories. The application also includes a feature that calculates the total amount spent by reading and processing the stored CSV data. This calculation logic is separated into a dedicated helper function, which improves code organization and makes the program easier to test and maintain.

Special attention was given to input validation and error handling to ensure the program behaves reliably. User input is validated to prevent invalid or negative expense amounts, and appropriate error messages are displayed when incorrect input is provided. The program also gracefully handles cases where the expense file does not yet exist or contains no data, preventing crashes and ensuring a smooth user experience.

To further improve code quality and reliability, the project includes automated tests written using pytest. These tests focus on verifying the correctness of the total expense calculation and ensuring that the program handles edge cases such as empty or missing files appropriately. By separating core logic from user interaction, the project allows meaningful unit tests to be written without relying on manual input.

Overall, this project was designed to be both practical and educational. It demonstrates how Python can be used to build a functional real-world application while adhering to good programming practices such as modular design, clear separation of concerns, and defensive programming. The personal expense tracker serves as a useful tool for managing expenses while also showcasing the skills and concepts developed throughout CS50P.

