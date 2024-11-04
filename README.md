# Book Inventory Management System

## Project Setup Instructions

### Prerequisites
- Python 3.12 installed
- Django 5.1.2 installed (already added in requirements.txt)
- SQLite3 (optional, as Django includes SQLite by default)

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rakeshbasnet/djngo-book-inventory.git
   cd BookInventorySystem
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Database Migrations**:
   ```bash
   python manage.py migrate

5. **Run the Development Server**:
   ```bash
   python manage.py runserver

6. **Access the Application**:
   Open a browser and go to: `http://127.0.0.1:8000`