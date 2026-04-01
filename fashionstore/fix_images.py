import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashionstore.settings')
django.setup()

from store.models import Product

# Fixed working image URLs for all products
fixed_images = {
    "Linen Blazer": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400&q=80",
    "Summer Maxi Skirt": "https://images.unsplash.com/photo-1562572159-4efd90232655?w=400&q=80",
    # Update all others too just to be safe
    "Floral Wrap Dress": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&q=80",
    "High-Waist Jeans": "https://images.unsplash.com/photo-1582418702059-97ebafb35d09?w=400&q=80",
    "Classic Polo Shirt": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400&q=80",
    "Slim Chinos": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400&q=80",
    "Denim Jacket": "https://images.unsplash.com/photo-1551537482-f2075a1d41f2?w=400&q=80",
    "Casual Linen Shirt": "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=400&q=80",
    "Rainbow Hoodie": "https://images.unsplash.com/photo-1611911813383-67769b37a149?w=400&q=80",
    "Denim Overalls": "https://images.unsplash.com/photo-1519278409-1f56ab241a94?w=400&q=80",
    "Leather Tote Bag": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?w=400&q=80",
    "Classic Sunglasses": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&q=80",
}

updated = 0
for name, url in fixed_images.items():
    count = Product.objects.filter(name=name).update(image_url=url)
    if count:
        print(f"✅ Updated: {name}")
        updated += count
    else:
        print(f"⚠️  Not found: {name}")

print(f"\nDone! Updated {updated} products.")
