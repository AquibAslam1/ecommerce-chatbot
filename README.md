
# 🤖 E-commerce Chatbot – AI-Powered Product Assistant

An intelligent, Django-based e-commerce chatbot that enables users to search for products using natural language. It returns real-time responses with product links, making the shopping experience more interactive and efficient.

---

## 🔍 Overview

The **E-commerce Chatbot** integrates a dynamic chatbot interface into an online store platform. Users can type queries like _"show me phone"_ or _"find HP laptops"_ and instantly receive results with links to detailed product pages.

---

## 🚀 Key Features

- 🔐 **User Authentication**  
  Secure login/logout functionality using Django's built-in auth system.

- 💬 **Chatbot UI**  
  A responsive, AJAX-powered chatbot interface styled with CSS animations and bubble effects.

- 🛍️ **Smart Product Search**  
  Users can ask natural-language queries to find products by brand, category, or price.

- 🖼️ **Product Detail Pages**  
  Dynamic pages show full product information including name, category, price, description, rating, image, and stock status.

- 🧠 **Chat History**  
  Logged chat interactions (user query and bot response) stored per user and displayed in history.

- 📦 **100+ Sample Products**  
  Easily populate the product database with randomized mock data using Django shell.

---

## 🛠️ Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| **Frontend** | HTML, CSS, JavaScript     |
| **Backend**  | Python, Django            |
| **Database** | SQLite (Django default)   |
| **Tools**    | Git, GitHub, VS Code      |

---

## 📁 Project Structure

```
ecommerce_chatbot/
├── chatbot/                # Chatbot logic and templates
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   ├── chatbot.html
│   │   └── product_detail.html
├── products/               # Product model and management
│   └── models.py
├── db.sqlite3              # Default database
├── manage.py
├── requirements.txt
└── static/ (optional)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AquibAslam1/ecommerce-chatbot.git
cd ecommerce-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

### 7️⃣ Add Sample Products (via shell)

```bash
python manage.py shell
```

Then paste the following:

```python
from products.models import Product
import random

categories = ['Electronics', 'Books', 'Textiles', 'Accessories', 'Clothing']
for i in range(1, 101):
    Product.objects.create(
        name=f"Product {i}",
        description=f"Description for Product {i}",
        price=round(random.uniform(100, 10000), 2),
        rating=round(random.uniform(3.0, 5.0), 1),
        image_url="https://via.placeholder.com/300",
        category=random.choice(categories),
        stock=random.choice([True, False])
    )
```

---

## 🧪 How to Use

- Visit the homepage and **log in**.
- Ask product-related questions in natural language like:
  - _"show me redmi phones"_
  - _"laptop"_, _"headphones"_, _"books"_
- Chatbot responds with **clickable product links**.
- Click a link to view the **product detail page**.
- View full **chat history** from the history tab.

---

## 📄 License

This project is open source and free for **educational and personal use only**.  
Contact the author for commercial usage rights.

---

## 👨‍💻 Author

**Md Aquib Aslam**  
GitHub: [@AquibAslam1](https://github.com/AquibAslam1)

---

## 📬 Contributing

Contributions are welcome!  
Feel free to open a pull request or raise an issue.

---
