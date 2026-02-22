# smart-business-manager
##Description
This is a Django backend project with security setup, for managing business accounts, products, and users.

## Installation

1. Clone the repository:
   git clone https://github.com/Ftima-ezzahra2005/smart-business-manager.git

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - Linux/Mac: source venv/bin/activate

4. Install requirements:
   pip install -r requirements.txt

5. Set up .env file with your DJANGO_SECRET_KEY and DJANGO_DEBUG

## Usage

1. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

2. Collect static files:
   python manage.py collectstatic

3. Run the server:
   python manage.py runserver

## Contributors

- Ftima-ezzahra ZAGHLOUL (Backend & Security)
- Hasna KHAYARI (Backend & Security)
- Nacim OUALLA (Frontend)
