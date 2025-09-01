#!/usr/bin/env python3
"""
Create Admin User Script for Jubair Boot House
This script will create an admin user in the SQLite database.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from database import SessionLocal
from models import Admin
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin_user():
    """Create admin user in the database"""
    db = SessionLocal()
    
    try:
        # Check if admin already exists
        existing_admin = db.query(Admin).first()
        if existing_admin:
            print(f"✅ Admin user already exists: {existing_admin.username}")
            return
        
        # Create default admin
        admin = Admin(
            username="JuberSiddique",
            password=pwd_context.hash("Juber@708492")
        )
        
        db.add(admin)
        db.commit()
        
        print("✅ Admin user created successfully!")
        print("📝 Username: JuberSiddique")
        print("🔑 Password: Juber@708492")
        print("🔗 Login at: http://localhost:8000/auth/login")
        
    except Exception as e:
        print(f"❌ Error creating admin: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Creating Admin User for Jubair Boot House...")
    print("=" * 50)
    
    create_admin_user()
    
    print("=" * 50)
    print("🎉 Done! You can now login to the admin panel.")
