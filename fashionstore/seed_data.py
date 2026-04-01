import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashionstore.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

# Create categories
cats = [
    ('Women', 'women'),
    ('Men', 'men'),
    ('Kids', 'kids'),
    ('Accessories', 'accessories'),
]
for name, slug in cats:
    Category.objects.get_or_create(name=name, slug=slug)

women = Category.objects.get(slug='women')
men = Category.objects.get(slug='men')
kids = Category.objects.get(slug='kids')
acc = Category.objects.get(slug='accessories')

products = [
    # Women
    ("Floral Wrap Dress", "A beautiful floral wrap dress perfect for any occasion.", 49.99, women,
     "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=400&q=80"),
    ("High-Waist Jeans", "Classic high-waist slim-fit jeans in indigo blue.", 59.99, women,
     "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400&q=80"),
    ("Linen Blazer", "Lightweight linen blazer ideal for work or weekend.", 89.99, women,
     "https://images.unsplash.com/photo-1594938298603-c8148c4b4d8e?w=400&q=80"),
    ("Summer Maxi Skirt", "Flowing maxi skirt with tropical print.", 39.99, women,
     "https://images.unsplash.com/photo-1583496661160-fb5218b8de07?w=400&q=80"),
    # Men
    ("Classic Polo Shirt", "Breathable cotton polo shirt in navy.", 34.99, men,
     "https://images.unsplash.com/photo-1598032895397-b9472444bf93?w=400&q=80"),
    ("Slim Chinos", "Smart slim-fit chinos in khaki.", 54.99, men,
     "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400&q=80"),
    ("Denim Jacket", "Timeless denim jacket with chest pockets.", 79.99, men,
     "https://images.unsplash.com/photo-1544441893-675973e31985?w=400&q=80"),
    ("Casual Linen Shirt", "Relaxed linen shirt perfect for summer days.", 44.99, men,
     "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&q=80"),
    # Kids
    ("Rainbow Hoodie", "Fun rainbow-striped hoodie for kids.", 29.99, kids,
     "https://images.unsplash.com/photo-1518831959646-742c3a14ebf7?w=400&q=80"),
    ("Denim Overalls", "Cute denim overalls for toddlers.", 34.99, kids,
     "https://images.unsplash.com/photo-1503944583220-79d8926ad5e2?w=400&q=80"),
    # Accessories
    ("Leather Tote Bag", "Spacious leather tote with inner pockets.", 69.99, acc,
     "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400&q=80"),
    ("Classic Sunglasses", "UV-protected oval sunglasses.", 24.99, acc,
     "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400&q=80"),
]

for name, desc, price, cat, img in products:
    Product.objects.get_or_create(
        name=name,
        defaults={'description': desc, 'price': price, 'category': cat, 'image_url': img, 'stock': 20}
    )

# Create superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: admin / admin123")

# Create demo user
if not User.objects.filter(username='demo').exists():
    User.objects.create_user('demo', 'demo@example.com', 'demo1234')
    print("Demo user created: demo / demo1234")

print(f"Seeded {Product.objects.count()} products in {Category.objects.count()} categories.")
