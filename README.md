## STILL UNDER DEVELOPMENT

# :moneybag: **Personal Finance Tracker** :chart_with_upwards_trend:

An **intuitive** and **user-friendly** personal finance tracker that helps you manage your income, expenses, and provides insightful reports, predictions, and charts. Built with **Flask**, **Bootstrap**, **SCSS**, and **SQLite**. This web app gives you full control over your financial health, with features to track, analyze, and predict your financial trends.

---

## 🚀 **Features**

### :star2: **User Authentication**
- Secure login and registration system for users to manage their finances.

### :credit_card: **Transaction Management**
- Add, view, and categorize your transactions with ease. Keep track of both income and expenses.

### :chart_with_upwards_trend: **Financial Reporting**
- Generate beautiful, detailed reports showing your income, expenses, and balance over time.

### :bulb: **Predictive Analysis**
- Predict your future income and expenses based on historical trends.

### :bar_chart: **Interactive Dashboard**
- An aesthetically pleasing dashboard with **charts** and **summary stats** of your financial activities.

### :dark_sunglasses: **Dark Theme Support**
- Toggle between light and dark modes for a better viewing experience.

---

## 🛠️ **Technologies Used**

- **Flask**: Lightweight Python framework to handle routing and application logic.
- **SQLAlchemy**: ORM for managing SQLite database.
- **Bootstrap**: For responsive, modern UI design.
- **SCSS**: Advanced styling for better customization and theming.
- **Chart.js**: For interactive charts and graphs of your financial data.
- **SweetAlert2**: For beautiful, customizable alert messages.
- **SQLite**: Local database to store user data, transactions, and other app information.

---

## 🏁 **Setup & Installation**

Follow these steps to set up the **Personal Finance Tracker** on your local machine:

### 1. **Clone the Repository**
git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker

### 2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
Run the following command to install required Python packages:
pip install -r requirements.txt

### 4. Run the Application
python app.py

Visit http://localhost:5000 to begin managing your finances!

### project structure 
personal-finance-tracker/
│
├── app.py                      # Main Flask app entry point
├── config.py                   # Global config settings (dev, prod)
├── database.db                 # SQLite database (auto-generated)
│
├── /instance/                  # Sensitive config (ignored by Git)
│   └── config.py
│
├── /static/                    # Static assets (CSS, JS, images)
│   ├── /css/
│   │   ├── styles.css          # Main stylesheet
│   │   ├── bootstrap.min.css   # Bootstrap CSS
│   │   ├── dark-theme.css      # Dark theme styles
│   ├── /scss/
│   │   ├── _variables.scss     # SCSS variables (colors, spacing)
│   │   ├── _mixins.scss        # SCSS mixins
│   │   ├── _components.scss    # Buttons, cards, etc.
│   │   ├── _dashboard.scss     # Dashboard-specific styles
│   │   └── styles.scss         # Main SCSS entry point
│   ├── /js/
│   │   ├── scripts.js          # Custom JS logic
│   │   ├── charts.js           # Financial charts
│   │   ├── sweetalert2.min.js  # SweetAlert2 for alerts
│   │   ├── bootstrap.bundle.min.js
│   ├── /images/
│       └── logo.png
│
├── /templates/                 # Jinja2 HTML templates
│   ├── base.html               # Base layout (navbar, footer)
│   ├── login.html              # Login page
│   ├── register.html           # Registration page
│   ├── dashboard.html          # User dashboard
│   ├── add_transaction.html    # Add a new transaction
│   ├── report.html             # Financial report
│   ├── predict.html            # Prediction page
│
├── /models/                    # SQLAlchemy models
│   └── models.py               # Database models
│
├── /routes/                    # Flask route blueprints
│   ├── auth_routes.py          # Routes for authentication
│   ├── transaction_routes.py   # Routes for transactions
│   ├── report_routes.py        # Routes for reports
│   ├── predict_routes.py       # Routes for predictions
│
├── /utils/                     # Utility and helper functions
│   ├── helpers.py              # Helper functions
│   └── predictions.py          # Functions for financial predictions
│
├── /tests/                     # Unit and integration tests
│   ├── test_auth.py            # Auth-related tests
│   ├── test_transactions.py    # Transaction tests
│   ├── test_reports.py         # Report tests
│   └── test_predictions.py     # Prediction tests
│
├── /migrations/                # (Optional) DB migration scripts
│
├── Dockerfile                  # Docker container config
├── docker-compose.yml          # Docker orchestration config
│
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignored files (e.g., venv, instance)
├── README.md                   # Project overview
└── LICENSE                     # Project license (MIT)
