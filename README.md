📂 File Handling Project (Python)

A complete demonstration of **Python File Handling** operations — including file creation, reading, writing, appending, and deletion — all implemented in an interactive, menu-driven console application.  

This project is designed for beginners in Python to understand how file systems work and how data can be managed efficiently using basic file handling functions.

---

## 🧭 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Concepts Covered](#-concepts-covered)
- [Project Structure](#-project-structure)
- [Installation & Setup](#️-installation--setup)
- [How to Run](#-how-to-run)
- [Code Explanation](#-code-explanation)
- [Sample Output](#-sample-output)
- [Error Handling](#-error-handling)
- [Future Enhancements](#-future-enhancements)
- [References](#-references)
- [Author](#-author)

---

## 📝 Overview

File handling is an essential part of programming that allows you to **store, access, and modify data** on your system.  
This Python-based console application allows users to:
- Create new files  
- Write data into files  
- Read and display file contents  
- Append data to existing files  
- Delete unwanted files safely  

It demonstrates **real-world file operations** and good programming practices such as **modular design, exception handling, and user interaction**.

---

## 🚀 Features

✅ Create new text files  
✅ Write and append data to files  
✅ Read file contents  
✅ Delete existing files safely  
✅ Check file existence  
✅ Graceful error handling  
✅ User-friendly menu interface  

---

## 🧠 Concepts Covered

| Concept | Description |
|----------|--------------|
| **File Handling Functions** | `open()`, `read()`, `write()`, `close()` |
| **Modes** | `'r'` (read), `'w'` (write), `'a'` (append), `'x'` (create) |
| **Exception Handling** | Using `try-except` blocks to avoid runtime errors |
| **OS Module** | Used for checking existence and deleting files (`os.remove`, `os.path.exists`) |
| **Functions in Python** | Modular approach using separate functions for each operation |
| **User Input** | Interactive CLI menu for performing operations |

---file-handling-project/
│
├── main.py # Main Python file containing all logic
├── sample.txt # Example text file created during execution
├── README.md # Project documentation
└── requirements.txt # (Optional) Dependencies, if any



💻 Code Explanation

Here’s the breakdown of major functions:

Function	Purpose
createFile()	Creates a new text file
writeFile()	Writes user input to a file (overwrites existing data)
readFile()	Reads and displays file contents
appendFile()	Appends user input to the end of a file
deleteFile()	Deletes a specified file if it exists
main()	Controls the program flow using a menu-driven loop

🧾 Sample Output
===== File Handling Menu =====
1. Create File
2. Write to File
3. Read File
4. Append to File
5. Delete File
6. Exit
Enter your choice: 1

Enter file name to create: sample.txt
File created successfully!


Example of reading:

===== File Handling Menu =====
Enter your choice: 3
Enter file name to read: sample.txt

File Content:
Hello! This is a test file.

⚠️ Error Handling
Error Type	Description	Example
FileNotFoundError	Occurs if user tries to read/delete a non-existent file	“File not found!”
PermissionError	Raised if the file is open or locked	“Access denied!”
IOError	General input/output operation failure	“I/O error occurred!”
🔮 Future Enhancements

Add Graphical User Interface (GUI) using Tkinter or PyQt

Support for multiple file types (CSV, JSON, XML)

Add logging functionality

Implement file search and rename options

Include encryption/decryption for secure file handling

📚 References

Python Official Documentation

W3Schools - Python File Handling

GeeksforGeeks - File Handling in Python

👨‍💻 Author

Ritik Gujre
📧 Email: ritik26cs103@satiengg.in
]
🔗 GitHub: https://github.com/ritik12004

💼 LinkedIn: www.linkedin.com/in/ritikgujre



⭐ If you find this project useful, please give it a star on GitHub!

Would you like me to also create a **`main.py` file** that perfectly matches this README (with clean menu, comments, and exception handling)?  
That way, your GitHub project will look complete and professional.

