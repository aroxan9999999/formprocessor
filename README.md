# FormProcessor

Это Django-приложение предназначено для анализа и идентификации заполненных форм посредством сравнения с заранее определенными шаблонами в базе данных.

## Быстрый старт

### Клонирование репозитория

```bash
git clone https://github.com/aroxan9999999/formprocessor.git
cd formprocessor
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py test
docker build -t formprocessor-app .
docker run -p 8000:8000 formprocessor-app
