```
 ██████╗ ██╗  ██╗██╗███╗   ███╗ █████╗ ██████╗ ████████╗
 ██╔══██╗██║  ██║██║████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
 ██████╔╝███████║██║██╔████╔██║███████║██████╔╝   ██║   
 ██╔═══╝ ██╔══██║██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║   
 ██║     ██║  ██║██║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   
 ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
```

### 🛒 A Scalable RESTful E-Commerce API Backend

#### *Authentication · Catalog · Cart · Orders — Production Ready*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-FF1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-Djoser-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![Swagger](https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![API Docs](https://img.shields.io/badge/API_Docs-Swagger-85EA2D?style=flat-square&logo=swagger)](http://127.0.0.1:8000/docs/)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square)](https://github.com/Tanbir-Hasan-247)

<br/>

[**API Documentation**](http://127.0.0.1:8000/docs/) · [**Report a Bug**](https://github.com/Tanbir-Hasan-247/PhiMart/issues) · [**Request a Feature**](https://github.com/Tanbir-Hasan-247/PhiMart/issues)

<br/>

</div>

---

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Database Schema](#-database-schema)
- [API Reference](#-api-reference)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [API Documentation](#-api-documentation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🌟 About The Project

**PhiMart** is a fully functional, highly scalable e-commerce backend REST API built with Django and Django REST Framework (DRF). It provides a complete suite of endpoints covering the full e-commerce lifecycle — from user registration and email activation, through product catalog browsing and cart management, all the way to order placement and status tracking.

Engineered for clean separation of concerns, PhiMart is designed to be the backbone of any modern frontend — whether that's a React SPA, a mobile app, or a Next.js storefront.

> 💡 **Why PhiMart?**
> E-commerce backends are notoriously complex to get right. PhiMart ships with JWT auth via Djoser, anonymous cart sessions, multi-image product support, admin-controlled order status transitions, and interactive Swagger docs — all out of the box.

---

## ✨ Key Features

<details>
<summary><b>🔐 Advanced Authentication (Djoser + JWT)</b></summary>
<br/>

Full user lifecycle management powered by `Djoser` and `djangorestframework-simplejwt`:

| Feature | Description |
|---|---|
| Registration | Create a new account with email and password |
| Email Activation | Account activation via tokenized email link |
| JWT Login | Obtain access & refresh tokens |
| Token Refresh | Seamlessly renew expired access tokens |
| Password Reset | Request and confirm password reset via email |
| Profile Management | View and update authenticated user profile |

</details>

<details>
<summary><b>🛍️ Product Catalog</b></summary>
<br/>

| Feature | Description |
|---|---|
| Categories | Full CRUD for product categories |
| Products | Create, list, filter, and manage product listings |
| Multi-Image Upload | Attach multiple images to a single product |
| Reviews | Authenticated users can submit and view product reviews |
| Public Browsing | Unauthenticated users can browse all products and categories |

</details>

<details>
<summary><b>🛒 Shopping Cart</b></summary>
<br/>

| Feature | Description |
|---|---|
| Anonymous Sessions | Cart creation requires no account — works for guest users |
| Add Items | Add any product to a cart by cart ID |
| Update Quantity | Adjust item quantities dynamically |
| Remove Items | Delete individual items from the cart |
| Total Calculation | Cart detail endpoint returns computed total price |

</details>

<details>
<summary><b>📦 Order Management</b></summary>
<br/>

| Feature | Description |
|---|---|
| Place Order | Convert an active cart into a confirmed order |
| Order History | Authenticated users can view all their past orders |
| Order Detail | Retrieve full details of a specific order |
| Status Update | Admins can progress orders through processing stages |
| Cancellation | Users can cancel active orders before dispatch |

</details>

<details>
<summary><b>📚 Interactive API Documentation</b></summary>
<br/>

Auto-generated and always in sync via `drf-spectacular`:

| Interface | URL | Purpose |
|---|---|---|
| **Swagger UI** | `/docs/` | Interactive live endpoint testing |
| **ReDoc** | `/redoc/` | Clean and readable API reference |
| **OpenAPI Schema** | `/api/schema/` | Raw YAML for SDK/client generation |

</details>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| **Language** | Python 3.10+ |
| **Framework** | Django 4.x |
| **API Layer** | Django REST Framework (DRF) |
| **Authentication** | Djoser + `djangorestframework-simplejwt` (JWT) |
| **Database (Dev)** | SQLite |
| **Database (Prod)** | PostgreSQL |
| **API Documentation** | `drf-spectacular` (Swagger UI + ReDoc) |
| **Image Handling** | Pillow |
| **Config Management** | `python-decouple` |

</div>

---

## 🏗️ System Architecture

```
+-------------------------------------------------------------------+
|                          PhiMart API                              |
|                                                                   |
|  +------------+   +-----------+   +----------+   +----------+    |
|  |   Public   |   |   Buyer   |   |  Admin   |   | Frontend |    |
|  |  (Browse)  |   |  (Auth)   |   | (Manage) |   |   App    |    |
|  +-----+------+   +-----+-----+   +----+-----+   +----+-----+    |
|        |                |              |               |          |
|  +-----v----------------v--------------v---------------v-------+  |
|  |                 JWT Authentication (Djoser)                 |  |
|  +------------------------------+------------------------------+  |
|                                 |                                 |
|  +------------------------------v------------------------------+  |
|  |           Django REST Framework (DRF) Router               |  |
|  |     ViewSets . Serializers . Permissions . Filters         |  |
|  +------+-------------+------------------+--------------------+  |
|         |             |                  |                        |
|  +------v------+ +----v------+  +--------v--------+              |
|  |   Catalog   | |   Cart    |  |     Orders      |              |
|  |  Module     | |  Module   |  |    Module       |              |
|  | (Products,  | | (Session  |  | (Checkout,      |              |
|  |  Categories,| |  Based)   |  |  Status, Cancel)|              |
|  |  Images,    | |           |  |                 |              |
|  |  Reviews)   | |           |  |                 |              |
|  +------+------+ +----+------+  +--------+--------+              |
|         |             |                  |                        |
|  +------v-------------v------------------v--------------------+  |
|  |              Django ORM  <->  SQLite / PostgreSQL          |  |
|  +------------------------------------------------------------+  |
|                                                                   |
|  +------------------------------------------------------------+   |
|  |       Swagger UI / ReDoc  (drf-spectacular)                |   |
|  +------------------------------------------------------------+   |
+-------------------------------------------------------------------+
```

---

## 🗄️ Database Schema

The API is built on a normalized relational schema. Core models and their serializers:

<details>
<summary><b>👤 Authentication & Users</b></summary>
<br/>

| Model / Serializer | Purpose |
|---|---|
| `User` | Core user model (email, password, is_active) |
| `UserCreate` | Registration serializer |
| `Activation` | Email activation token handler |
| `CustomUserSerializer` | Profile read/update |
| `SendEmailReset` | Trigger password reset email |
| `PasswordResetConfirm` | Confirm new password with token |
| `SetUsername` / `SetPassword` | In-session credential updates |

</details>

<details>
<summary><b>🔑 JWT Security</b></summary>
<br/>

| Serializer | Purpose |
|---|---|
| `TokenObtainPair` | Login — returns access + refresh |
| `TokenRefresh` | Renew expired access token |
| `TokenVerify` | Validate token integrity |

</details>

<details>
<summary><b>🛍️ Catalog</b></summary>
<br/>

| Model / Serializer | Purpose |
|---|---|
| `Category` | Product grouping |
| `Product` | Full product detail (name, price, stock, category) |
| `SimpleProduct` | Lightweight product reference for cart/order items |
| `ProductImage` | Multiple images per product |
| `Review` | Customer star ratings and written reviews |

</details>

<details>
<summary><b>🛒 Cart System</b></summary>
<br/>

| Model / Serializer | Purpose |
|---|---|
| `Cart` | Session-based cart container (UUID primary key) |
| `CartItem` | Individual product + quantity within a cart |
| `Empty` | Utility serializer for empty response bodies |

</details>

<details>
<summary><b>📦 Orders</b></summary>
<br/>

| Model / Serializer | Purpose |
|---|---|
| `Order` | Top-level order (user, status, timestamp) |
| `OrderItem` | Snapshot of product + price at checkout time |
| `CreateOrder` | Converts a cart UUID into a confirmed order |
| `UpdateOrder` | Admin-only status progression serializer |

</details>

---

## 📌 API Reference

### 🔐 Authentication & Users (`/auth/`)

| Method | Endpoint | Description | Access |
|:---:|---|---|:---:|
| `POST` | `/auth/users/` | Register a new user | Public |
| `POST` | `/auth/users/activation/` | Activate account via email token | Public |
| `GET` | `/auth/users/me/` | Retrieve current user profile | Auth |
| `PATCH` | `/auth/users/me/` | Update user profile | Auth |
| `POST` | `/auth/users/reset_password/` | Send password reset email | Public |
| `POST` | `/auth/users/reset_password_confirm/` | Confirm new password | Public |
| `POST` | `/auth/jwt/create/` | Obtain JWT access & refresh tokens | Public |
| `POST` | `/auth/jwt/refresh/` | Refresh an expired access token | Public |
| `POST` | `/auth/jwt/verify/` | Verify token validity | Public |

### 🛍️ Product Catalog (`/products/` & `/categories/`)

| Method | Endpoint | Description | Access |
|:---:|---|---|:---:|
| `GET` | `/categories/` | List all product categories | Public |
| `POST` | `/categories/` | Create a new category | Admin |
| `GET` | `/categories/{id}/` | Retrieve a specific category | Public |
| `PATCH/DELETE` | `/categories/{id}/` | Update or delete a category | Admin |
| `GET` | `/products/` | List all products (filterable) | Public |
| `POST` | `/products/` | Create a new product listing | Admin |
| `GET` | `/products/{id}/` | Retrieve product details | Public |
| `PATCH/DELETE` | `/products/{id}/` | Update or remove a product | Admin |
| `GET/POST` | `/products/{id}/images/` | List or upload product images | Public / Admin |
| `DELETE` | `/products/{id}/images/{img_id}/` | Remove a specific product image | Admin |
| `GET/POST` | `/products/{id}/reviews/` | List or submit product reviews | Public / Auth |

### 🛒 Shopping Cart (`/carts/`)

| Method | Endpoint | Description | Access |
|:---:|---|---|:---:|
| `POST` | `/carts/` | Create a new anonymous cart session | Public |
| `GET` | `/carts/{id}/` | Retrieve cart with items & total | Public |
| `DELETE` | `/carts/{id}/` | Destroy a cart session | Public |
| `GET/POST` | `/carts/{cart_id}/items/` | List items or add product to cart | Public |
| `PATCH` | `/carts/{cart_id}/items/{id}/` | Update item quantity | Public |
| `DELETE` | `/carts/{cart_id}/items/{id}/` | Remove item from cart | Public |

### 📦 Order Management (`/orders/`)

| Method | Endpoint | Description | Access |
|:---:|---|---|:---:|
| `GET` | `/orders/` | List all orders for logged-in user | Auth |
| `POST` | `/orders/` | Create order from active cart | Auth |
| `GET` | `/orders/{id}/` | Retrieve a specific order's full details | Auth |
| `DELETE` | `/orders/{id}/` | Delete a specific order | Auth |
| `PATCH` | `/orders/{id}/update_status/` | Advance order processing status | Admin |
| `POST` | `/orders/{id}/cancel/` | Cancel an active order | Auth |

> 📖 Full request bodies, response schemas, headers, and live testing at:
> **http://127.0.0.1:8000/docs/**

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed:

- **Python** `>= 3.10` — [Download](https://python.org/downloads)
- **Git** — [Download](https://git-scm.com/)
- **pip** — bundled with Python 3.x

---

### Installation

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Tanbir-Hasan-247/PhiMart.git
cd PhiMart
```

**Step 2 — Create and activate a virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Configure environment variables**

Create a `.env` file in the root directory (see [Environment Variables](#environment-variables) below).

**Step 5 — Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 6 — Create a superuser (Admin)**

```bash
python manage.py createsuperuser
```

**Step 7 — Start the development server**

```bash
python manage.py runserver
```

🎉 API is live at **http://127.0.0.1:8000/**
📚 Swagger docs at **http://127.0.0.1:8000/docs/**

---

### Environment Variables

Create a `.env` file in the project root:

```env
# --- Django -----------------------------------------------------------
SECRET_KEY=your_super_secret_django_key_here
DEBUG=True

# --- Database (leave blank for SQLite locally) ------------------------
DB_NAME=phimart_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

# --- Email (Gmail SMTP for activation & password reset) --------------
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_16_character_app_password

# --- Frontend Domain (for activation email links) --------------------
DOMAIN=localhost:3000
SITE_NAME=PhiMart
```

> ⚠️ **Security Note:** Never commit `.env` to version control — add it to `.gitignore`.
> 📩 **Gmail App Password:** Enable 2FA at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

---

## 📚 API Documentation

PhiMart ships with **auto-generated, always-in-sync** interactive documentation via `drf-spectacular`:

<div align="center">

| Interface | URL | Description |
|:---:|---|---|
| 🟡 **Swagger UI** | `/docs/` | Try every endpoint live in your browser |
| 📘 **ReDoc** | `/redoc/` | Clean, print-friendly reference documentation |
| 📄 **OpenAPI Schema** | `/api/schema/` | Raw OpenAPI 3.0 YAML for SDK/client generation |

</div>

---

## 📁 Project Structure

```
PhiMart/
|
+-- manage.py
+-- requirements.txt
+-- .env                        # Environment variables (not committed)
|
+-- phimart/                    # Core Django project config
|   +-- settings.py
|   +-- urls.py
|   +-- wsgi.py
|
+-- apps/
|   +-- store/                  # Product catalog (Category, Product, Image, Review)
|   +-- cart/                   # Cart session management (Cart, CartItem)
|   +-- orders/                 # Order processing (Order, OrderItem, Status)
|   +-- users/                  # Custom user model & Djoser integration
|
+-- templates/                  # Email templates (activation, password reset)
+-- media/                      # Uploaded product images
+-- static/                     # Static files
```

---

## 🗺️ Roadmap

- [x] ✅ JWT authentication with Djoser (register, activate, reset)
- [x] ✅ Full product catalog CRUD (categories, products, images)
- [x] ✅ Anonymous session-based shopping cart
- [x] ✅ Multi-image support per product
- [x] ✅ Customer product reviews
- [x] ✅ Order placement from cart with item snapshot
- [x] ✅ Admin order status management
- [x] ✅ Order cancellation by users
- [x] ✅ Interactive Swagger UI + ReDoc documentation
- [ ] 🔄 **Pagination & Filtering** — cursor/page-based pagination, price range filters
- [ ] 💳 **Payment Gateway** — Stripe or SSLCommerz integration for checkout
- [ ] 📦 **Inventory Management** — Stock tracking and low-stock alerts
- [ ] 🔔 **Order Notifications** — Email alerts on status changes via Django Signals
- [ ] ⭐ **Wishlist API** — Save products for later
- [ ] 🏷️ **Discount & Coupon Engine** — Promo code support at checkout
- [ ] 🐳 **Docker Support** — Containerized setup for production deployment

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome!

1. **Fork** the repository
2. **Create** a feature branch → `git checkout -b feature/AmazingFeature`
3. **Commit** your changes → `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch → `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

Please ensure your code is clean, well-documented, and consistent with DRF conventions.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👨‍💻 Author

<div align="center">

### Tanbir Hasan

*Aspiring Software Developer & Competitive Programmer*

<br/>

[![Email](https://img.shields.io/badge/Email-tanbirhasan569%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanbirhasan569@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Tanbir--Hasan--247-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tanbir-Hasan-247)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tanbir-hasan-638075345/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-3b82f6?style=for-the-badge&logo=safari&logoColor=white)](https://tanbir-hasan-247.github.io/Tanbir-Hasan/)

<br/>

*If PhiMart was useful to you, please consider giving it a ⭐ — it really helps!*

</div>

---

<div align="center">

Made with ❤️ and ☕ by **Tanbir Hasan**

*PhiMart — Powering commerce, one API call at a time.*

</div>
