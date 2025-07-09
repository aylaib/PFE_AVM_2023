# PFE_AVM_2023 : Aviation & Marine Fuel and Lubricant Sales Website
## 🎯 Project Description
This project is a dynamic web application developed as part of my **Bachelor's Thesis in Information Systems and Software Engineering** at the University of Science and Technology Houari Boumediene (USTHB). It is an online sales website for fuel and lubricant products intended for the aviation and marine sectors, designed for **NAFTAL Fuel Branch**.
The work was completed approximately 3 years ago (defense on 05/06/2023).
## 💻 Technologies Used
This project was developed using the following technologies:
* **Python**
* **Django** (web framework)
* **HTML, CSS, JavaScript** (for frontend)
* **MySQL** (relational database)
## 📁 Directory Structure
Here's an overview of the main code structure:
PFE_AVM_2023-main/
├── src/                       # Main Django source code directory
│   ├── admin_app/             # Application for administration interface
│   ├── media/                 # Media files (images, etc.) uploaded
│   ├── Produit/               # Application managing products
│   ├── project/               # Main Django project configuration
│   │   ├── settings.py        # Configuration file
│   │   └── urls.py            # Main URL routes
│   ├── user_app/              # Application for user interface
│   ├── User_Aviation/         # Specific application for aviation user management
│   └── manage.py              # Django administration utility
├── requirements.txt           # List of Python project dependencies
├── .gitignore                 # Files and folders to be ignored by Git
└── README.md                  # This file
## 🛠️ Installation and Execution Guide (for reference)
*Note: These steps describe how the project was set up and executed at the time of its conception.*
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/PFE_AVM_2023.git](https://github.com/your_username/PFE_AVM_2023.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd PFE_AVM_2023
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env_pfeavm
    # For Windows:
    .\env_pfeavm\Scripts\activate
    # For Linux/macOS:
    source env_pfeavm/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Apply database migrations:**
    ```bash
    python src/manage.py migrate
    ```
6.  **Start the development server:**
    ```bash
    python src/manage.py runserver
    ```
    The application would then be accessible via your browser at `http://127.0.0.1:8000/`.
## 🤝 Authors
* **DIGUER Nedjemddine**
* **LAIB Ayoub**
## 🙏 Acknowledgments
We would like to express our sincere gratitude to our supervisor, Mr. BRADAIE Mustapha, for his valuable guidance and support throughout the completion of this Final Year Project.

## 📌 Citation
If you use this project, please cite it as:

LAIB Ayoub, DIGUER Nedjemddine (2025), *Aviation & Marine Fuel and Lubricant Sales Website*, GitHub repository: https://github.com/aylaib/PFE_AVM_2023

