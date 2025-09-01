#!/usr/bin/env python3
"""
Update Admin Credentials Script for Jubair Boot House
This script will update the existing admin user credentials in the database.
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

def update_admin_credentials():
    """Update admin user credentials in the database"""
    db = SessionLocal()
    
    try:
        # Check if admin exists
        existing_admin = db.query(Admin).first()
        if not existing_admin:
            print("❌ No admin user found. Please run create_admin.py first.")
            return
        
        # Update admin credentials
        existing_admin.username = "JuberSiddique"
        existing_admin.password = pwd_context.hash("Juber@708492")
        
        db.commit()
        
        print("✅ Admin credentials updated successfully!")
        print("📝 New Username: JuberSiddique")
        print("🔑 New Password: Juber@708492")
        print("🔗 Login at: http://localhost:8000/auth/login")
        
    except Exception as e:
        print(f"❌ Error updating admin credentials: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Updating Admin Credentials for Jubair Boot House...")
    print("=" * 50)
    
    update_admin_credentials()
    
    print("=" * 50)
    print("🎉 Done! You can now login with the new credentials.")
