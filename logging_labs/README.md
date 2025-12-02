## 📘 Logging Demo — Python Logging & Exception Handling

This project demonstrates how to use Python’s built-in logging module to:

- Configure logging with different levels

- Log messages to a file

- Capture exceptions with full stack traces

- Log user actions (login, activity, logout)

- Use multiple handlers (File + Console)

----

## Logging Configuration

The project initializes structured logging with:

- DEBUG, INFO, WARNING, ERROR, CRITICAL

- Timestamped logs

- Output written to app.log

- Clean formatting for production use

---

## 📂 Project Structure

```

logging_labs/
│
├── main.py        # Main script with logging examples
├── app.log        # Contains debug + exception logs
└── user_actions.log  # Contains user activity logs

```

---

## 📄 Example Log Output

```

2025-11-03 22:10:43 - DEBUG - This is a debug message — useful for development.
2025-11-03 22:10:43 - INFO - This is an info message — for general updates.
2025-11-03 22:10:43 - WARNING - This is a warning — something might be wrong.
2025-11-03 22:10:43 - ERROR - This is an error message — something went wrong.
2025-11-03 22:10:43 - CRITICAL - This is critical — the program may not recover.
2025-11-03 22:10:43 - ERROR - An error occurred!
```
