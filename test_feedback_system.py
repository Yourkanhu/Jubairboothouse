#!/usr/bin/env python3
"""
Test Feedback System Script for Jubair Boot House
This script will test the feedback system functionality.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from database import SessionLocal
from models import Feedback
from datetime import datetime

def test_feedback_system():
    """Test the feedback system functionality"""
    print("🧪 Testing Feedback System...")
    print("=" * 50)
    
    db = SessionLocal()
    try:
        # Test 1: Check if feedback table exists
        print("1. Checking feedback table...")
        feedback_count = db.query(Feedback).count()
        print(f"   ✅ Feedback table exists with {feedback_count} records")
        
        # Test 2: Check table structure
        print("\n2. Checking table structure...")
        if feedback_count > 0:
            sample_feedback = db.query(Feedback).first()
            print(f"   ✅ Sample feedback found:")
            print(f"      - ID: {sample_feedback.id}")
            print(f"      - Name: {sample_feedback.name}")
            print(f"      - Email: {sample_feedback.email}")
            print(f"      - Message: {sample_feedback.message[:50]}...")
            print(f"      - Created: {sample_feedback.created_at}")
        else:
            print("   ℹ️  No feedback records found (this is normal for a new system)")
        
        # Test 3: Test adding a sample feedback
        print("\n3. Testing feedback creation...")
        test_feedback = Feedback(
            name="Test User",
            email="test@example.com",
            message="This is a test feedback message to verify the system is working correctly.",
            created_at=datetime.now()
        )
        
        db.add(test_feedback)
        db.commit()
        db.refresh(test_feedback)
        
        print(f"   ✅ Test feedback created with ID: {test_feedback.id}")
        
        # Test 4: Verify the new feedback
        new_count = db.query(Feedback).count()
        print(f"   ✅ Total feedback count: {new_count}")
        
        # Test 5: Clean up test data
        print("\n4. Cleaning up test data...")
        db.delete(test_feedback)
        db.commit()
        final_count = db.query(Feedback).count()
        print(f"   ✅ Test feedback removed. Final count: {final_count}")
        
        print("\n🎉 All tests passed! The feedback system is working correctly.")
        
    except Exception as e:
        print(f"❌ Error testing feedback system: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_feedback_system()
