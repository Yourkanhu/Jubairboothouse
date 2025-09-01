#!/usr/bin/env python3
"""
Database Initialization Script for Jubair Boot House
This script will create the database and tables if they don't exist.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from database import engine, Base
from models import Admin, Product, User, UserFavourite

def create_tables():
    """Create all tables using SQLAlchemy"""
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ All tables created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

def test_connection():
    """Test the database connection"""
    try:
        # Test connection by creating a session
        from database import SessionLocal
        db = SessionLocal()
        db.close()
        print("✅ Database connection successful!")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def main():
    print("🚀 Initializing Jubair Boot House Database...")
    print("=" * 50)
    
    # Step 1: Test connection
    print("🔗 Step 1: Testing database connection...")
    if not test_connection():
        print("❌ Database connection failed. Exiting.")
        sys.exit(1)
    
    # Step 2: Create tables
    print("📋 Step 2: Creating tables...")
    if not create_tables():
        print("❌ Failed to create tables. Exiting.")
        sys.exit(1)
    
    print("=" * 50)
    print("🎉 Database initialization completed successfully!")
    print("📝 Next steps:")
    print("   1. Run the application: python run.py")
    print("   2. Visit http://localhost:8000/auth/setup to create admin user")
    print("   3. Login with JuberSiddique/Juber@708492")

if __name__ == "__main__":
    main()
