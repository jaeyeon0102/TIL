-- Active: 1752639458321@@localhost@3306@hospital
CREATE DATABASE hospital

USE hospital

CREATE TABLE patient (
  patient_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  birth_date DATE,
  phone_number VARCHAR(15)
)

INSERT INTO patient 
VALUES
(1,  'John',  'Doe',  '1990-01-01',  '123-456-7890'),
(2,  'Jane',  'Smith',  '1985-02-02',  '098-765-4321'),
(3,  'Alice', 'White',  '1970-03-15',  '111-222-3333')

CREATE TABLE doctor (
  doctor_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  specialty VARCHAR(100)
)

INSERT INTO doctor 
VALUES
(1,  'Alice',  'Brown',  'Cardiology'),
(2,  'Bob',  'Johnson',  'Neurology'),
(3,  'Charlie',  'Davis',  'Dermatology')

CREATE TABLE visits (
  visit_id INT PRIMARY KEY,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  visit_date DATE,
  FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
   
)

INSERT INTO visits 
VALUES
(1, 1, 1, '2024-01-01'),
(2, 2, 2, '2024-02-01'),
(3, 1, 2, '2024-03-01'),
(4, 3, 3, '2024-04-01'),
(5, 1, 2, '2024-05-01'),
(6, 2, 3, '2024-06-01'),
(7, 3, 1, '2024-07-01')

SELECT 
  p.first_name,
  p.last_name,
  p.phone_number,
  v.visit_date,
  d.first_name AS doctor_first_name,
  d.last_name AS doctor_last_name,
  d.specialty
FROM visits v
JOIN patient p ON p.patient_id = v.patient_id
JOIN doctor d ON d.doctor_id = v.doctor_id

SELECT 
 d.first_name,
 d.last_name,
 d.specialty,
 COUNT(v.visit_id) AS visit_count
FROM doctor d
LEFT JOIN visits v ON v.doctor_id = d.doctor_id 
WHERE YEAR(v.visit_date) = 2024 
GROUP BY d.doctor_id, d.first_name, d.last_name, d.specialty 


SELECT 
  p.first_name,
  p.last_name,
  p.phone_number,
  COUNT(v.visit_id) AS visit_count
FROM patient p 
LEFT JOIN visits v ON v.patient_id = p.patient_id 
WHERE v.doctor_id = 2 
GROUP BY p.first_name, p.last_name, p.phone_number 
HAVING visit_count >= 2