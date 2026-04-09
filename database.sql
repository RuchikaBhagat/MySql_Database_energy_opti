CREATE DATABASE energy_db;
USE energy_db;

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100),
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE energy_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT,
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    energy FLOAT,
    frequency FLOAT,
    power_factor FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);
