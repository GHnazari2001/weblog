# اطلس  📖: پروژه وبلاگ با جنگو

![Django](https://img.shields.io/badge/Django-4.2-blue?logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

اطلس بلاگ یک وب اپلیکیشن کامل و مدرن است که با استفاده از فریم‌ورک جنگو پایتون توسعه داده شده است. این پروژه به عنوان بخشی از دوره کارآموزی طراحی شده و شامل تمام قابلیت‌های یک وبلاگ استاندارد به همراه ویژگی‌های پیشرفته می‌باشد.

🔗 **لینک نسخه زنده:** [ghadir2.pythonanywhere.com](http://ghadir2.pythonanywhere.com/)

---

## ✨ ویژگی‌های کلیدی

* **مدیریت کامل پست‌ها (CRUD):** قابلیت ایجاد، مشاهده، ویرایش و حذف پست‌ها توسط نویسنده.
* **سیستم کاربران سفارشی:** مدل کاربر (`CustomUser`) با قابلیت ثبت‌نام، ورود، خروج و پروفایل شخصی (شامل عکس، بیوگرافی و لینک‌های اجتماعی).
* **دسته‌بندی و برچسب‌گذاری:** سازماندهی مطالب بر اساس دسته‌بندی‌ها و تگ‌های داینامیک (`django-taggit`).
* **سیستم لایک AJAX:** قابلیت لایک کردن پست‌ها بدون نیاز به بارگذاری مجدد صفحه.
* **بخش دیدگاه‌ها:** امکان ثبت دیدگاه برای هر پست توسط کاربران عضو.
* **جستجوی پیشرفته:** قابلیت جستجو در عنوان و متن پست‌ها.
* **صفحه‌بندی (Pagination):** تقسیم لیست پست‌ها در صفحات مختلف برای ناوبری بهتر.
* **طراحی واکنش‌گرا (Responsive):** ظاهر کاملاً واکنش‌گرا و سازگار با دستگاه‌های مختلف (موبایل، تبلت و دسکتاپ) با استفاده از بوت‌استرپ.


---

## 🛠️ تکنولوژی‌های استفاده شده

* **بک‌اند (Backend):**
    * Python 3.12
    * Django 5.2
* **فرانت‌اند (Frontend):**
    * HTML5
    * CSS3
    * Bootstrap 5
    * JavaScript
* **دیتابیس:**
    * SQLite 3 (برای توسعه)
* **کتابخانه‌های کلیدی پایتون:**
    * `django-taggit`: برای مدیریت تگ‌ها.
    * `django-crispy-forms` & `crispy-bootstrap4`: برای رندر کردن فرم‌ها با استایل بوت‌استرپ.
    * `Pillow`: برای پردازش تصاویر آپلود شده.
    
* **استقرار (Deployment):**
    * PythonAnywhere
    * Gunicorn (WSGI Server)

---

## 🚀 راه‌اندازی پروژه به صورت محلی (Local Setup)

برای اجرای این پروژه روی سیستم خود، مراحل زیر را دنبال کنید:

1.  **کلون کردن ریپازیتوری:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **ایجاد و فعال‌سازی محیط مجازی:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **نصب پکیج‌های مورد نیاز:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **ایجاد فایل `.env`:**
    یک فایل به نام `.env` در ریشه پروژه بسازید و مقادیر زیر را در آن قرار دهید:
    ```
    SECRET_KEY='your-secret-key-here'
    DEBUG=True
    ```

5.  **اجرای مایگریشن‌ها:**
    ```bash
    python manage.py migrate
    ```

6.  **ایجاد کاربر ادمین:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **اجرای سرور توسعه:**
    ```bash
    python manage.py runserver
    ```
    اکنون پروژه در آدرس `http://127.0.0.1:8000` در دسترس است.

---


---

## 👤 نویسنده

* **نام شما:** [قدیر نظری]
* **ایمیل:** [ghadir.nazari19@gmail.com]
