#!/usr/bin/env python3
"""
Test script to verify multiple images functionality
"""

import sqlite3
import json
import os

def test_database_schema():
    """Test if the images column exists and works correctly"""
    print("🔍 Testing database schema...")
    
    try:
        conn = sqlite3.connect("jubair_boot_house.db")
        cursor = conn.cursor()
        
        # Check if images column exists
        cursor.execute("PRAGMA table_info(products)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'images' in columns:
            print("✅ Images column exists in products table")
        else:
            print("❌ Images column missing from products table")
            return False
        
        # Test JSON storage
        test_images = ["/static/uploads/test1.jpg", "/static/uploads/test2.jpg"]
        test_json = json.dumps(test_images)
        
        # Insert a test product
        cursor.execute("""
            INSERT INTO products (name, description, price, category, status, images)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("Test Product", "Test Description", 99.99, "Sports", "Available", test_json))
        
        # Retrieve and verify
        cursor.execute("SELECT images FROM products WHERE name = 'Test Product'")
        result = cursor.fetchone()
        
        if result and result[0]:
            retrieved_images = json.loads(result[0])
            if retrieved_images == test_images:
                print("✅ JSON storage and retrieval working correctly")
            else:
                print("❌ JSON storage/retrieval mismatch")
                return False
        else:
            print("❌ Failed to retrieve stored images")
            return False
        
        # Clean up test data
        cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
        conn.commit()
        
        print("✅ Database schema test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {str(e)}")
        return False
    finally:
        conn.close()

def test_uploads_directory():
    """Test if uploads directory exists and is writable"""
    print("🔍 Testing uploads directory...")
    
    uploads_dir = "static/uploads"
    
    if os.path.exists(uploads_dir):
        print("✅ Uploads directory exists")
    else:
        print("❌ Uploads directory missing")
        return False
    
    if os.access(uploads_dir, os.W_OK):
        print("✅ Uploads directory is writable")
    else:
        print("❌ Uploads directory is not writable")
        return False
    
    print("✅ Uploads directory test passed!")
    return True

def test_model_methods():
    """Test the Product model's get_images_list method"""
    print("🔍 Testing Product model methods...")
    
    try:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
        from models import Product
        
        # Create a test product instance
        product = Product()
        product.image_url = "https://example.com/image.jpg"
        product.images = json.dumps(["/static/uploads/test1.jpg", "/static/uploads/test2.jpg"])
        
        # Test get_images_list method
        images_list = product.get_images_list()
        expected_images = ["/static/uploads/test1.jpg", "/static/uploads/test2.jpg"]
        
        if images_list == expected_images:
            print("✅ get_images_list method working correctly")
        else:
            print(f"❌ get_images_list method failed. Expected: {expected_images}, Got: {images_list}")
            return False
        
        # Test with only image_url
        product.images = None
        images_list = product.get_images_list()
        if images_list == []:
            print("✅ get_images_list with only image_url working")
        else:
            print(f"❌ get_images_list with only image_url failed. Expected: [], Got: {images_list}")
            return False
        
        # Test with only uploaded images
        product.image_url = None
        product.images = json.dumps(["/static/uploads/test1.jpg"])
        images_list = product.get_images_list()
        if images_list == ["/static/uploads/test1.jpg"]:
            print("✅ get_images_list with only uploaded images working")
        else:
            print(f"❌ get_images_list with only uploaded images failed. Expected: ['/static/uploads/test1.jpg'], Got: {images_list}")
            return False
        
        print("✅ Product model methods test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Model test failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting multiple images functionality tests...\n")
    
    tests = [
        test_database_schema,
        test_uploads_directory,
        test_model_methods
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Multiple images functionality is ready.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
    
    return passed == total

if __name__ == "__main__":
    main()
