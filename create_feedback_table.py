#!/usr/bin/env python3
"""
Create Feedback Table Script for Jubair Boot House
This script will create the feedback table in the database.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from database import engine, Base
from models import Feedback

def create_feedback_table():
    """Create feedback table in the database"""
    try:
        # Create the feedback table
        Feedback.__table__.create(engine, checkfirst=True)
        print("✅ Feedback table created successfully!")
        print("📋 Table structure:")
        print("   - id: Auto-incrementing primary key")
        print("   - name: User's full name")
        print("   - email: User's email address")
        print("   - message: Feedback message content")
        print("   - created_at: Timestamp of submission")
        
    except Exception as e:
        print(f"❌ Error creating feedback table: {e}")

if __name__ == "__main__":
    print("🚀 Creating Feedback Table for Jubair Boot House...")
    print("=" * 50)
    
    create_feedback_table()
    
    print("=" * 50)
    print("🎉 Done! The feedback table is now ready to store user messages.")
