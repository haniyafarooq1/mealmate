# 🍽️ MealMate - Smart Meal Decision Assistant

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<div align="center">
  <h3>✨ Can't decide what to eat? Let MealMate help you! ✨</h3>
  <p><i>"One cannot think well, love well, sleep well, if one has not dined well." - Virginia Woolf</i></p>
</div>

---

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Built With](#-built-with)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [SOLID Principles](#-solid-principles-implementation)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About The Project

**MealMate** is a smart decision assistant that solves the everyday struggle of **"What should I eat today?"** 

Unlike traditional food delivery apps or recipe platforms that only solve half the problem, MealMate combines **restaurant suggestions** AND **recipe recommendations** into one seamless experience. Whether you want to cook at home or eat out, MealMate guides you through the decision process with personalized suggestions.

### **The Problem We Solve:**
- 🤔 Decision fatigue about what to eat
- 📱 Switching between multiple apps
- 🍳 Wasted ingredients from not knowing what to cook
- 🏪 Missing out on great local restaurants

---

## 🚀 Key Features

### 🔥 **Core Functionality**

| Feature | Description |
|--------|-------------|
| **🍽️ Eat Out** | Discover restaurants by cuisine type (Italian, Chinese, Desi, etc.) |
| **👨‍🍳 Cook at Home** | Find recipes by meal type OR ingredients you have |
| **🎲 Surprise Me** | Random restaurant/recipe recommendation for indecisive moments |
| **❤️ Favorites** | Save your preferred restaurants and recipes for quick access |

### ✨ **Premium Features**
- ✅ **Dual Decision Flow** - One app, two paths (Eat Out OR Cook)
- ✅ **Smart Filtering** - Filter recipes by available ingredients
- ✅ **Personalized Experience** - User authentication & saved favorites
- ✅ **Responsive Design** - Works perfectly on desktop & mobile
- ✅ **Animated UI** - Smooth animations & beautiful pastel gradients
- ✅ **Rotating Food Quotes** - Inspirational culinary wisdom

---

## 🛠️ Built With

### **Backend**
- [Django](https://www.djangoproject.com/) - Python web framework
- [SQLite](https://www.sqlite.org/) - Database (easily upgradable to PostgreSQL/MySQL)
- Django Authentication - User management system

### **Frontend**
- [Bootstrap 5](https://getbootstrap.com/) - Responsive framework
- [Font Awesome 6](https://fontawesome.com/) - Beautiful icons
- [Google Fonts](https://fonts.google.com/) - Playfair Display & Inter
- [AOS](https://michalsnik.github.io/aos/) - Scroll animations
- Custom CSS - Pastel gradients & glass morphism

### **Tools**
- Git & GitHub - Version control
- VS Code - Development environment
- Figma - UI/UX prototyping

---

## 📸 Screenshots

<div align="center">
  <table>
    <tr>
      <td><strong>🏠 Landing Page</strong></td>
      <td><strong>🍳 Cook at Home</strong></td>
    </tr>
    <tr>
      <td><img src="screenshots/landing.png" alt="Landing Page" width="400"/></td>
      <td><img src="screenshots/cook.png" alt="Cook at Home" width="400"/></td>
    </tr>
    <tr>
      <td><strong>🍽️ Eat Out</strong></td>
      <td><strong>🎲 Surprise Me</strong></td>
    </tr>
    <tr>
      <td><img src="screenshots/eatout.png" alt="Eat Out" width="400"/></td>
      <td><img src="screenshots/surprise.png" alt="Surprise Me" width="400"/></td>
    </tr>
    <tr>
      <td><strong>❤️ Favorites</strong></td>
      <td><strong>⚙️ Admin Panel</strong></td>
    </tr>
    <tr>
      <td><img src="screenshots/favorites.png" alt="Favorites" width="400"/></td>
      <td><img src="screenshots/admin.png" alt="Admin" width="400"/></td>
    </tr>
  </table>
</div>

---

## ⚙️ Installation

### **Prerequisites**
- Python 3.8+ 
- pip (Python package manager)
- Virtual environment (recommended)

### **Step-by-Step Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mealmate.git
   cd mealmate
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   cd mealmate
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📖 Usage Guide

### **👤 For Users (Food Explorers)**

1. **Sign Up / Login** - Create your account or log in
2. **Choose Your Path** - Select from three options:
   - **🍳 Cook at Home** → Choose meal type → Enter optional ingredients → Get recipes
   - **🍽️ Eat Out** → Select cuisine → Discover restaurants → Add to favorites
   - **🎲 Surprise Me** → Get random recommendation (restaurant OR recipe)
3. **❤️ Save Favorites** - Bookmark restaurants and recipes you love
4. **📱 Access Anywhere** - Your favorites are saved to your account

### **👑 For Admins (Content Managers)**

1. **Access Admin Panel** - `/admin` endpoint
2. **Manage Content** - Add/edit/delete restaurants and recipes
3. **Monitor Users** - View registered users
4. **Curate Experience** - Update discounts, prices, ingredients

---

## 📁 Project Structure

```
mealmate/
├── mealmate/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI config
│
├── mealmate_app/            # Main application
│   ├── templates/          # HTML templates
│   │   └── mealmate_app/   # App-specific templates
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py            # App URL routes
│   └── admin.py           # Admin configuration
│
├── users/                  # User authentication app
│   ├── templates/users/    # User templates
│   ├── views.py           # Login/signup logic
│   └── urls.py           # User URL routes
│
├── home/                  # Landing page app
├── static/               # Static files (CSS, JS, images)
├── db.sqlite3           # Database file
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

---

## 🏗️ SOLID Principles Implementation

### **✅ Single Responsibility Principle**
- Each view handles ONE specific task
- Models separated by domain (Restaurant, Recipe, Favorite)
- Template files isolated by function

### **✅ Open/Closed Principle**
- New cuisine types can be added without modifying existing code
- Recipe filtering extensible for new criteria
- UI components are extendable via Bootstrap classes

### **✅ Liskov Substitution Principle**
- FavoriteRestaurant and FavoriteRecipe inherit cleanly from base models
- Consistent interface for all recommendation types

### **✅ Interface Segregation Principle**
- Separate interfaces for restaurant and recipe selection
- User vs Admin distinct interfaces
- Clean separation between authentication and core logic

### **✅ Dependency Inversion Principle**
- Views depend on abstractions (models), not concrete implementations
- Template inheritance hierarchy
- Loose coupling between components

---

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Haniya Farooq** -  haniya.farooq1290@gmail.com

**Project Link:** [https://github.com/yourusername/mealmate](https://github.com/yourusername/mealmate)

---
