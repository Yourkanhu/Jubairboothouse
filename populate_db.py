#!/usr/bin/env python3
"""
Database Population Script for Jubair Boot House
This script will populate the database with sample product data.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from database import SessionLocal
from models import Product

def populate_products():
    """Populate the products table with sample data"""
    
    # Sample product data
    sample_products = [
        {
            "name": "Nike Air Max 270",
            "description": "Comfortable running shoes with excellent cushioning and breathable mesh upper.",
            "price": 129.99,
            "size": "10",
            "category": "Sports",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Adidas Ultraboost 22",
            "description": "Premium running shoes with responsive Boost midsole and Primeknit upper.",
            "price": 179.99,
            "size": "9",
            "category": "Sports",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Converse Chuck Taylor",
            "description": "Classic canvas sneakers perfect for casual wear and street style.",
            "price": 59.99,
            "size": "8",
            "category": "Casual",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1607522370275-f14206abe5d3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Vans Old Skool",
            "description": "Iconic skate shoes with durable suede upper and signature side stripe.",
            "price": 64.99,
            "size": "11",
            "category": "Casual",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Dr. Martens 1460",
            "description": "Classic leather boots with air-cushioned sole and durable construction.",
            "price": 169.99,
            "size": "10",
            "category": "Boots",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1549298916-b41d501d3772?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Timberland Premium",
            "description": "Waterproof leather boots with premium construction and comfort.",
            "price": 199.99,
            "size": "9",
            "category": "Boots",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Allen Edmonds Oxford",
            "description": "Premium leather dress shoes with Goodyear welt construction.",
            "price": 349.99,
            "size": "10",
            "category": "Formal",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Cole Haan Wingtip",
            "description": "Elegant wingtip shoes with modern comfort technology.",
            "price": 199.99,
            "size": "11",
            "category": "Formal",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1595341888016-a392ef81b7de?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "New Balance 990v5",
            "description": "Premium running shoes with superior comfort and stability.",
            "price": 184.99,
            "size": "9",
            "category": "Sneakers",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "ASICS Gel-Kayano 28",
            "description": "Advanced stability running shoes with GEL technology.",
            "price": 159.99,
            "size": "10",
            "category": "Sneakers",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Birkenstock Arizona",
            "description": "Comfortable sandals with contoured footbed and adjustable straps.",
            "price": 99.99,
            "size": "8",
            "category": "Sandals",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Teva Hurricane XLT2",
            "description": "Adventure sandals with quick-dry webbing and comfortable footbed.",
            "price": 49.99,
            "size": "11",
            "category": "Sandals",
            "status": "Available",
            "image_url": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        }
    ]
    
    try:
        db = SessionLocal()
        
        # Check if products already exist
        existing_count = db.query(Product).count()
        if existing_count > 0:
            print(f"⚠️  Database already has {existing_count} products. Skipping population.")
            return
        
        # Add sample products
        for product_data in sample_products:
            product = Product(**product_data)
            db.add(product)
        
        db.commit()
        print(f"✅ Successfully added {len(sample_products)} sample products to the database!")
        
        # Show some statistics
        total_products = db.query(Product).count()
        print(f"📊 Total products in database: {total_products}")
        
        # Show products by category
        categories = db.query(Product.category).distinct().all()
        print("📂 Products by category:")
        for category in categories:
            count = db.query(Product).filter(Product.category == category[0]).count()
            print(f"   {category[0]}: {count} products")
        
        db.close()
        
    except Exception as e:
        print(f"❌ Error populating database: {e}")
        db.rollback()
        db.close()

def main():
    print("🚀 Populating Jubair Boot House Database with Sample Data...")
    print("=" * 60)
    
    populate_products()
    
    print("=" * 60)
    print("🎉 Database population completed!")
    print("📝 Next steps:")
    print("   1. Run the application: python run.py")
    print("   2. Visit http://localhost:8000 to see the products")
    print("   3. Login as admin to manage products")

if __name__ == "__main__":
    main()
