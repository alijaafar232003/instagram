# Auth App - Flask Authentication System

A simple yet secure authentication system built with Flask for learning about APIs, user authentication, and web development.

## 🎯 Project Purpose

This project was created as a university assignment to learn:
- How to work with APIs using Python
- User authentication and security best practices
- Flask web framework
- Database management with SQLAlchemy
- RESTful API design
- Deployment to cloud platforms

## ✨ Features

- **User Registration**: Create new accounts with username, email, and password
- **User Login**: Secure login system with password hashing
- **Protected Routes**: Dashboard accessible only to logged-in users
- **Session Management**: Flask-Login for session handling
- **RESTful API**: JSON endpoints for programmatic access
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Flash Messages**: User feedback for actions
- **SQLite Database**: Lightweight database for development

## 📁 Project Structure

```
auth-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .gitignore            # Files to exclude from Git
├── .env.example          # Example environment variables
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── dashboard.html    # User dashboard
└── static/               # Static files
    └── css/
        └── style.css     # Stylesheet
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd auth-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and change SECRET_KEY to a random string
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   ```
   Navigate to: http://localhost:5000
   ```

## 🔌 API Endpoints

### POST /api/register
Register a new user

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response (Success):**
```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

### POST /api/login
Login a user

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "securepassword"
}
```

**Response (Success):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  }
}
```

### GET /api/users
Get all users (requires authentication)

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "username": "johndoe",
      "email": "john@example.com"
    }
  ]
}
```

## 🧪 Testing the API

### Using curl:

**Register a user:**
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"password123"}'
```

**Login:**
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"password123"}'
```

### Using Python:

```python
import requests

# Register
response = requests.post('http://localhost:5000/api/register', json={
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'password123'
})
print(response.json())

# Login
response = requests.post('http://localhost:5000/api/login', json={
    'username': 'testuser',
    'password': 'password123'
})
print(response.json())
```

## 🔒 Security Features

1. **Password Hashing**: Passwords are hashed using Werkzeug's security functions (PBKDF2 with SHA-256)
2. **Session Management**: Secure session handling with Flask-Login
3. **CSRF Protection**: Built-in protection (can be enhanced with Flask-WTF)
4. **Input Validation**: Server-side validation of user inputs
5. **Unique Constraints**: Email and username must be unique

## 🌐 Deployment to Render

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - Name: `auth-app` (or your choice)
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python app.py`
   - Add environment variable:
     - Key: `SECRET_KEY`
     - Value: (generate a random string)
   - Click "Create Web Service"

## 📚 How It Works

### 1. Registration Flow
```
User fills form → POST to /register → 
Validate input → Check if user exists → 
Hash password → Save to database → 
Redirect to login
```

### 2. Login Flow
```
User fills form → POST to /login → 
Find user in database → Check password hash → 
Create session → Redirect to dashboard
```

### 3. Password Security
- Passwords are NEVER stored in plain text
- Uses Werkzeug's `generate_password_hash()` with salt
- Verification done with `check_password_hash()`

### 4. Session Management
- Flask-Login manages user sessions
- `@login_required` decorator protects routes
- Sessions stored securely with SECRET_KEY

## 🛠️ Technologies Used

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Werkzeug**: Password hashing utilities
- **SQLite**: Database (development)
- **HTML/CSS**: Frontend
- **JavaScript**: API interaction

## 📝 Future Enhancements

- [ ] Email verification
- [ ] Password reset functionality
- [ ] OAuth login (Google, GitHub)
- [ ] Profile picture uploads
- [ ] Two-factor authentication (2FA)
- [ ] Rate limiting for API endpoints
- [ ] PostgreSQL for production
- [ ] Docker containerization

## 🤝 Contributing

Feel free to fork this project and submit pull requests!

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Created as a university project to learn Flask and API development.

## 🆘 Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'flask'`
**Solution**: Make sure you've activated your virtual environment and installed dependencies

**Problem**: Database errors
**Solution**: Delete `users.db` file and restart the app to recreate the database

**Problem**: Port already in use
**Solution**: Change the port in `app.py` or kill the process using port 5000

## 📞 Support

If you have questions about this project, feel free to reach out or open an issue on GitHub!
"# test" 
