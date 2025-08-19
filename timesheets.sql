-- Databricks notebook source
CREATE TABLE timesheets (
    Employee_id INT,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Department VARCHAR(50),
    Work_type VARCHAR(20),
    Lead_status VARCHAR(20),
    Date_worked DATE,
    Date_filled DATE,
    Hours_worked DECIMAL(5,2),
    PRIMARY KEY(Employee_id, Date_worked)
);