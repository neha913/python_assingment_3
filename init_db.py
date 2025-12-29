"""
Database initialization script
Run this script to create the database and tables
"""
import pymysql
from sqlalchemy import create_engine, text
from config import settings
from database import Base, engine
from models import User


def create_database_if_not_exists():
    """Create the database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying database)
        connection = pymysql.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✓ Database '{settings.DB_NAME}' created or already exists")
        
        connection.close()
    except Exception as e:
        print(f"✗ Error creating database: {e}")
        raise


def create_tables():
    """Create all database tables"""
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✓ Database tables created successfully")
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        raise


def verify_connection():
    """Verify database connection"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
        print("✓ Database connection verified")
    except Exception as e:
        print(f"✗ Error verifying connection: {e}")
        raise


if __name__ == "__main__":
    print("=" * 50)
    print("FastAPI Database Initialization")
    print("=" * 50)
    print(f"Host: {settings.DB_HOST}")
    print(f"Port: {settings.DB_PORT}")
    print(f"Database: {settings.DB_NAME}")
    print(f"User: {settings.DB_USER}")
    print("=" * 50)
    print()
    
    try:
        print("Step 1: Creating database...")
        create_database_if_not_exists()
        print()
        
        print("Step 2: Creating tables...")
        create_tables()
        print()
        
        print("Step 3: Verifying connection...")
        verify_connection()
        print()
        
        print("=" * 50)
        print("✓ Database initialization completed successfully!")
        print("=" * 50)
        print("\nYou can now start the FastAPI application with:")
        print("  uvicorn main:app --reload")
        
    except Exception as e:
        print()
        print("=" * 50)
        print("✗ Database initialization failed!")
        print("=" * 50)
        print(f"Error: {e}")
        print("\nPlease check:")
        print("  1. MySQL server is running")
        print("  2. Database credentials in .env file are correct")
        print("  3. User has permission to create databases")
        exit(1)

