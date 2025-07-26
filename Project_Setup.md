# 🛍️ E-Commerce Backend API

A robust, scalable Django backend for managing products, categories, sellers, carts, orders, and user authentication for an e-commerce platform.

---

## 🚀 Features

- User Registration & JWT Authentication
- Product Catalog with Filtering, Search & Sorting
- Seller Management
- Shopping Cart
- Order Placement & Tracking
- Admin & Seller Permissions
- Swagger & ReDoc API Documentation
- Secure Production Configuration

---

## 🛠 Technologies

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (or SQLite for local)
- **Auth**: JWT (via `djangorestframework-simplejwt`)
- **Docs**: Swagger/OpenAPI (`drf-yasg`)

---

## 📁 Project Structure

```bash
project_nexus_BE/
├── ecommerce_backend/    # Django project
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routes incl. Swagger
│   ├── wsgi.py           # WSGI application
├── users_app/            # Custom user model, auth
├── product_app/          # Products
├── sellers_app/          # Seller model
├── cart_app/             # Cart and cart items
├── orders_app/           # Orders and order items
├── category_app          # categories of Products
├── logs/                 # Log output directory
├── manage.py             # Django entrypoint
