CREATE TABLE Dealer (
    D_id INT PRIMARY KEY,
    D_name TEXT
);


CREATE TABLE Customer (
    C_id INT PRIMARY KEY,
    C_name TEXT,
    C_add TEXT
);

CREATE TABLE Company (
    Reg_no INT PRIMARY KEY,
    C_name TEXT,
    Owner TEXT,
    Location TEXT,
    Contact TEXT
);


CREATE TABLE deals_with (
    D_id INT,
    Reg_no INT,
    PRIMARY KEY(D_id, Reg_no),
    FOREIGN KEY (D_id) REFERENCES Dealer(D_id),
    FOREIGN KEY (Reg_no) REFERENCES Company(Reg_no)
);

SELECT * FROM Dealer, deals_with, Company WHERE 

CREATE TABLE Customer_con (
    C_id INT PRIMARY KEY,
    Number TEXT,
    FOREIGN KEY (C_id) REFERENCES Customer(C_id)
);

SELECT * FROM Customer, Customer_con WHERE Customer.C_id=Customer_con.C_id;



CREATE TABLE Vehicle (
    M_id INT,
    V_in INT, 
    C_id INT
    PRIMARY KEY (M_id, V_in, C_id)
);

CREATE TABLE Model (
    B_name TEXT,
    M_id INT,
    Style TEXT,
    lan_yr DATE,
    M_name TEXT
);

CREATE TABLE Brand (
    Reg_no , 
    B_name,
)

CREATE TABLE Company (
    Reg_no INT PRIMARY KEY,
    C_name 
)


-- 1. get names of all the dealers 
SELECT D_name FROM Dealer;

-- 2. get the names and add. of all the customers
SELECT C_name, C_add FROM Customer;

-- 3. get the name, location and contact of all companies
SELECT C_name, Location, Contact FROM Company;

-- 4. get the numbers of all customers
SELECT Number FROM Customer_con;

-- 5. get all possible pais of dealer and company combination
SELECT * FROM Dealer, Company;

-- 6. get customer names and numbers 
SELECT C_name, Number FROM Customer, Customer_con WHERE Customer.C_id=Customer_con.C_id;

-- 7. get all the dealer Names and the companies the dealer deals with 
SELECT D_name, C_name 
FROM Dealer, deals_with, Company
WHERE Dealer.D_id=deals_with.D_id AND Company.Reg_no=deals_with.Reg_no;


SELECT D_name, C_name 
FROM Dealer, deals_with, Company
WHERE Dealer.D_id=deals_with.D_id AND Company.Reg_no=deals_with.Reg_no
GROUP BY 