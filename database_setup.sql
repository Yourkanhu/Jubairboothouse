-- Jubair Boot House Database Setup Script
-- Run this script in MySQL to create the database and tables

-- Create database
CREATE DATABASE IF NOT EXISTS jubair_boot_house;
USE jubair_boot_house;

-- Create admins table
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    size VARCHAR(20) NOT NULL,
    category VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Available' NOT NULL,
    image_url VARCHAR(255)
);

-- Insert default admin user (password: Juber@708492 - hashed with bcrypt)
-- Note: This is a sample hashed password, you should generate your own
INSERT INTO admins (username, password) VALUES 
('JuberSiddique', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/HS.iK2i')
ON DUPLICATE KEY UPDATE username=username;

-- Show tables
SHOW TABLES;

-- Show table structures
DESCRIBE admins;
DESCRIBE products;
