import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashionstore.settings')
django.setup()

from store.models import Product

fixes = {
    "Summer Maxi Skirt": "https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=400&q=80",
    "Denim Overalls":    "https://images.unsplash.com/photo-1612336307429-8a898d10e223?w=400&q=80",
}

for name, url in fixes.items():
    count = Product.objects.filter(name=name).update(image_url=url)
    if count:
        print(f"✅ Fixed: {name}")
    else:
        print(f"⚠️  Not found: {name}")

print("\nDone!")
