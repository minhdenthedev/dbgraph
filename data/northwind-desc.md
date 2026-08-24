## Table: `Categories`
- ID: 8ab5a624-0596-497e-a0ee-3996d95dbe63
- Primary Keys: CategoryID.
- Shape: 8 row(s), 4 column(s).

### Column: `Picture`
- ID: 25ad7169-e449-40a6-95c9-8e09975036fa
- Data type: BLOB
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0

### Column: `CategoryID`
- ID: 04c20046-2808-4021-bbf1-99876e0eea6e
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: True
- Non null count: 8
- Null count: 0
- Numerical statistics: {'mean': 4.5, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 8}

### Column: `CategoryName`
- ID: 815cd167-41f4-45d9-a467-0ed9dd8a8ec8
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0
- Categorical statistics: {'value_counts': {'Seafood': 1, 'Produce': 1, 'Meat/Poultry': 1, 'Grains/Cereals': 1, 'Dairy Products': 1, 'Confections': 1, 'Condiments': 1, 'Beverages': 1}}

### Column: `Description`
- ID: 21fcbf83-627d-4ff0-957f-5e3b3dddcb25
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0
- Categorical statistics: {'value_counts': {'Sweet and savory sauces, relishes, spreads, and seasonings': 1, 'Soft drinks, coffees, teas, beers, and ales': 1, 'Seaweed and fish': 1, 'Prepared meats': 1, 'Dried fruit and bean curd': 1, 'Desserts, candies, and sweet breads': 1, 'Cheeses': 1, 'Breads, crackers, pasta, and cereal': 1}}

## Table: `CustomerCustomerDemo`
- ID: e1ea6b2c-3a25-4257-8eb7-ffa81b16b55f
- Primary Keys: CustomerID.
- Shape: 0 row(s), 2 column(s).

### Column: `CustomerID`
- ID: 707ed661-a134-48a9-bfd1-0966c06c962e
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

### Column: `CustomerTypeID`
- ID: f1668f51-ff26-46c1-b9b7-48813b3dbc37
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

## Table: `CustomerDemographics`
- ID: 169809a7-e312-4bac-9a68-d05105d14d7c
- Primary Keys: CustomerTypeID.
- Shape: 0 row(s), 2 column(s).

### Column: `CustomerTypeID`
- ID: 966a9cdc-7516-4b46-83ec-e33349896da8
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

### Column: `CustomerDesc`
- ID: 87dde91e-ae61-4dd8-810a-1bff7e5204ac
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

## Table: `Customers`
- ID: 09594675-9477-4331-8850-c2922cb0554f
- Primary Keys: CustomerID.
- Shape: 93 row(s), 11 column(s).

### Column: `CustomerID`
- ID: 6d8f6099-28b1-4e2e-98cf-227918948955
- Data type: TEXT
- Is Primary Key: True
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'ALFKI': 1, 'ANATR': 1, 'ANTON': 1, 'AROUT': 1, 'BERGS': 1, 'BLAUS': 1, 'BLONP': 1, 'BOLID': 1, 'BONAP': 1, 'BOTTM': 1}}

### Column: `CompanyName`
- ID: 3a4ea0d0-23c3-4115-9ebf-f64346f24464
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'IT': 2, 'Wolski  Zajazd': 1, 'Wilman Kala': 1, 'White Clover Markets': 1, 'Wellington Importadora': 1, 'Wartian Herkku': 1, 'Vins et alcools Chevalier': 1, 'Victuailles en stock': 1, 'Vaffeljernet': 1, "Trail's Head Gourmet Provisioners": 1}}

### Column: `ContactName`
- ID: c45ec1d3-e249-4e11-85ca-b8e611092d57
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'Zbyszek Piestrzeniewicz': 1, 'Yvonne Moncada': 1, 'Yoshi Tannamuri': 1, 'Yoshi Latimer': 1, 'Yang Wang': 1, 'Victoria Ashworth': 1, 'Valon Hoti': 1, 'Val2': 1, 'Thomas Hardy': 1, 'Sven Ottlieb': 1}}

### Column: `ContactTitle`
- ID: 97f93fdb-53ef-4e2b-9abf-21d1947ac492
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 17, 'Owner': 17, 'Marketing Manager': 12, 'Sales Manager': 11, 'Accounting Manager': 10, 'Sales Associate': 7, 'Marketing Assistant': 6, 'Sales Agent': 5, 'Order Administrator': 2, 'IT': 2}}

### Column: `Address`
- ID: c1440edd-6e14-42be-a4a0-09a83a55b0d7
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'Åkergatan 24': 1, 'ul. Filtrowa 68': 1, 'Walserweg 21': 1, 'Vinbæltet 34': 1, 'Via Monte Bianco 34': 1, 'Via Ludovico il Moro 22': 1, 'Torikatu 38': 1, 'Taucherstraße 10': 1, 'Strada Provinciale 124': 1, 'South House 300 Queensbridge': 1}}

### Column: `City`
- ID: 70e73112-d0a4-4ca5-8ae3-d3ca35a6c82d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'London': 6, 'México D.F.': 5, 'Sao Paulo': 4, 'Rio de Janeiro': 3, 'Madrid': 3, 'Buenos Aires': 3, 'Portland': 2, 'Paris': 2, 'Nantes': 2, 'Lisboa': 2}}

### Column: `Region`
- ID: 36cace1c-6d19-4d9f-9d7a-2808a05bbd8a
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'Western Europe': 28, 'South America': 16, 'North America': 16, 'Southern Europe': 10, 'British Isles': 8, 'Central America': 5, 'Northern Europe': 4, 'Scandinavia': 3, 'Eastern Europe': 1}}

### Column: `PostalCode`
- ID: cf00c753-955a-425e-b6b8-be2a75e7eb4c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 90
- Null count: 3
- Categorical statistics: {'value_counts': {'1010': 3, '44000': 2, '05033': 2, 'WX3 6FW': 1, 'WX1 6LT': 1, 'WA1 1DP': 1, 'V3F 2K1': 1, 'T2F 8M4': 1, 'SW7 1RZ': 1, 'S-958 22': 1}}

### Column: `Country`
- ID: 1143644d-9aeb-414b-b267-92749b3eae60
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'USA': 13, 'Germany': 11, 'France': 11, 'Brazil': 9, 'UK': 7, 'Spain': 5, 'Mexico': 5, 'Venezuela': 4, 'Italy': 3, 'Canada': 3}}

### Column: `Phone`
- ID: 78ddf161-80e0-48ed-8acb-e47fb6970d5a
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'981-443655': 1, '91.24.45.40': 1, '90-224 8858': 1, '88.60.15.31': 1, '86 21 32 43': 1, '78.32.54.86': 1, '7675-3425': 1, '6562-9722': 1, '61.77.61.10': 1, '40.67.88.88': 1}}

### Column: `Fax`
- ID: 29c30aa2-23c7-41fb-a473-e0577b5015a8
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 69
- Null count: 24
- Categorical statistics: {'value_counts': {'981-443655': 1, '91.24.45.41': 1, '90-224 8858': 1, '88.60.15.32': 1, '86 22 33 44': 1, '78.32.54.87': 1, '7675-3426': 1, '6562-9723': 1, '61.77.61.11': 1, '40.67.89.89': 1}}

## Table: `Employees`
- ID: d6090517-bb47-413b-a951-db0d8bf65c46
- Primary Keys: EmployeeID.
- Shape: 9 row(s), 18 column(s).

### Column: `EmployeeID`
- ID: 055d5005-5498-42f0-8815-569ba1622e3f
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: True
- Non null count: 9
- Null count: 0
- Numerical statistics: {'mean': 5.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `LastName`
- ID: 8ed5ab15-bfd6-4571-84ba-57ceae6f6632
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Suyama': 1, 'Peacock': 1, 'Leverling': 1, 'King': 1, 'Fuller': 1, 'Dodsworth': 1, 'Davolio': 1, 'Callahan': 1, 'Buchanan': 1}}

### Column: `FirstName`
- ID: 2f779241-dc95-4367-9d0f-e6612facaeac
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Steven': 1, 'Robert': 1, 'Nancy': 1, 'Michael': 1, 'Margaret': 1, 'Laura': 1, 'Janet': 1, 'Anne': 1, 'Andrew': 1}}

### Column: `Title`
- ID: 346d6b29-09c0-4a95-8086-bb800c6890f1
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 6, 'Vice President, Sales': 1, 'Sales Manager': 1, 'Inside Sales Coordinator': 1}}

### Column: `TitleOfCourtesy`
- ID: 902ebc10-0411-487e-85ac-70c48ea85620
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Ms.': 4, 'Mr.': 3, 'Mrs.': 1, 'Dr.': 1}}

### Column: `BirthDate`
- ID: f2d0e7f9-e881-4179-8705-96b3a2770d5e
- Data type: DATE
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `HireDate`
- ID: a378b57c-c080-4f1e-99be-04c7f1ac2719
- Data type: DATE
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `Address`
- ID: a60c5adb-1097-472d-8092-2f7c64ec410f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Edgeham Hollow\nWinchester Way': 1, 'Coventry House\nMiner Rd.': 1, '908 W. Capital Way': 1, '722 Moss Bay Blvd.': 1, '7 Houndstooth Rd.': 1, '507 - 20th Ave. E.Apt. 2A': 1, '4726 - 11th Ave. N.E.': 1, '4110 Old Redmond Rd.': 1, '14 Garrett Hill': 1}}

### Column: `City`
- ID: 18296191-f80c-433e-bdaa-d4cabec24a98
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'London': 4, 'Seattle': 2, 'Tacoma': 1, 'Redmond': 1, 'Kirkland': 1}}

### Column: `Region`
- ID: 9f56dac0-54d6-411f-bd13-d95c902d20d0
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'North America': 5, 'British Isles': 4}}

### Column: `PostalCode`
- ID: cbc88037-a5f0-4cd3-84e7-8d740c5fe968
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'WG2 7LT': 1, 'SW1 8JR': 1, 'RG1 9SP': 1, 'EC2 7JR': 1, '98401': 1, '98122': 1, '98105': 1, '98052': 1, '98033': 1}}

### Column: `Country`
- ID: 7a782190-5167-48c9-80a6-d959c46ed009
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 5, 'UK': 4}}

### Column: `HomePhone`
- ID: ef1cb775-2612-4b47-b650-b301ff943173
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'(71) 555-7773': 1, '(71) 555-5598': 1, '(71) 555-4848': 1, '(71) 555-4444': 1, '(206) 555-9857': 1, '(206) 555-9482': 1, '(206) 555-8122': 1, '(206) 555-3412': 1, '(206) 555-1189': 1}}

### Column: `Extension`
- ID: 311451a6-beca-4428-89de-eb45a8ce7f4c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'5467': 1, '5176': 1, '465': 1, '452': 1, '428': 1, '3457': 1, '3453': 1, '3355': 1, '2344': 1}}

### Column: `Photo`
- ID: 14ee59f6-36ef-49b6-9b1e-2e21df6141dc
- Data type: BLOB
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `Notes`
- ID: 1fd877cb-a607-45ec-8878-9194429c2f71
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses "Successful Telemarketing" and "International Sales Management."  He is fluent in French.': 1, 'Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan in 1992, the year he joined the company.  After completing a course entitled "Selling in Europe," he was transferred to the London office in March 1993.': 1, 'Michael is a graduate of Sussex University (MA, economics, 1983) and the University of California at Los Angeles (MBA, marketing, 1986).  He has also taken the courses "Multi-Cultural Selling" and "Time Management for the Sales Professional."  He is fluent in Japanese and can read and write French, Portuguese, and Spanish.': 1, 'Margaret holds a BA in English literature from Concordia College (1958) and an MA from the American Institute of Culinary Arts (1966).  She was assigned to the London office temporarily from July through November 1992.': 1, 'Laura received a BA in psychology from the University of Washington.  She has also completed a course in business French.  She reads and writes French.': 1, 'Janet has a BS degree in chemistry from Boston College (1984).  She has also completed a certificate program in food retailing management.  Janet was hired as a sales associate in 1991 and promoted to sales representative in February 1992.': 1, 'Education includes a BA in psychology from Colorado State University in 1970.  She also completed "The Art of the Cold Call."  Nancy is a member of Toastmasters International.': 1, 'Anne has a BA degree in English from St. Lawrence College.  She is fluent in French and German.': 1, 'Andrew received his BTS commercial in 1974 and a Ph.D. in international marketing from the University of Dallas in 1981.  He is fluent in French and Italian and reads German.  He joined the company as a sales representative, was promoted to sales manager in January 1992 and to vice president of sales in March 1993.  Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association.': 1}}

### Column: `ReportsTo`
- ID: 946d404b-1671-412a-bb08-941798554007
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 1
- Numerical statistics: {'mean': 3.125, 'std': None, 'min': 2, 'q2': None, 'median': None, 'q3': None, 'max': 5}

### Column: `PhotoPath`
- ID: d35c52e4-832c-4b2a-bb05-d6a9d45a4491
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'http://accweb/emmployees/davolio.bmp': 5, 'http://accweb/emmployees/peacock.bmp': 1, 'http://accweb/emmployees/leverling.bmp': 1, 'http://accweb/emmployees/fuller.bmp': 1, 'http://accweb/emmployees/buchanan.bmp': 1}}

## Table: `EmployeeTerritories`
- ID: cfe51f37-7ec6-423e-a5ff-69b06753125e
- Primary Keys: EmployeeID.
- Shape: 49 row(s), 2 column(s).

### Column: `EmployeeID`
- ID: ee1b41be-2d01-4dd0-896d-53cf3aa68d81
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 49
- Null count: 0
- Numerical statistics: {'mean': 5.510204081632653, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `TerritoryID`
- ID: 1f5ac5f7-6883-4b4d-8f54-0f32afc717fb
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 49
- Null count: 0
- Categorical statistics: {'value_counts': {'98104': 1, '98052': 1, '98004': 1, '95060': 1, '95054': 1, '95008': 1, '94105': 1, '94025': 1, '90405': 1, '85251': 1}}

## Table: `Order Details`
- ID: a03335e3-414c-4559-8764-66d67e903525
- Primary Keys: OrderID.
- Shape: 609283 row(s), 5 column(s).

### Column: `OrderID`
- ID: f3f851d4-e43f-4413-86f5-942fac652d2b
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 18785.56068526448, 'std': None, 'min': 10248, 'q2': None, 'median': None, 'q3': None, 'max': 26529}

### Column: `ProductID`
- ID: cdee512d-6316-4af3-91ad-cc4a7e1f3b4e
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 38.99956342126729, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 77}

### Column: `UnitPrice`
- ID: 06eda878-ecfa-4610-841b-01161017cd02
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0

### Column: `Quantity`
- ID: 8d8c0dbb-3ee3-4778-9d43-0710927ec8f2
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 25.503094621054583, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 130}

### Column: `Discount`
- ID: 3c216408-0e7c-4329-833a-7ca0ba9aa9d5
- Data type: REAL
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 0.00019865973611605774, 'std': None, 'min': 0.0, 'q2': None, 'median': None, 'q3': None, 'max': 0.25}

## Table: `Orders`
- ID: 20414a87-96a2-4314-887c-a247daf4b160
- Primary Keys: OrderID.
- Shape: 16282 row(s), 14 column(s).

### Column: `Freight`
- ID: 9b0a23b2-230a-413f-97bc-4bb6dabc430f
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `ShipName`
- ID: bd3f6cab-a437-40a8-b54d-6b3254c2c0f7
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Ernst Handel': 217, 'Wolski Zajazd': 213, 'Ana Trujillo Emparedados y helados': 209, 'Queen Cozinha': 207, 'Folk och fä HB': 205, 'Save-a-lot Markets': 204, 'Consolidated Holdings': 203, 'HILARION-Abastos': 202, 'Wartian Herkku': 201, 'Seven Seas Imports': 199}}

### Column: `ShipAddress`
- ID: 0093ef8a-e38a-46b2-ba33-f9b25249b96c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Obere Str. 57': 376, 'Kirchgasse 6': 217, 'ul. Filtrowa 68': 213, 'Avda. de la Constitución 2222': 209, 'Alameda dos Canàrios, 891': 207, 'Åkergatan 24': 205, '187 Suffolk Ln.': 204, 'Berkeley Gardens 12 \xa0Brewery': 203, 'Carrera 22 con Ave. Carlos Soublette #8-35': 202, 'Torikatu 38': 201}}

### Column: `ShipCity`
- ID: ea44ff9f-8cb2-4631-94c2-cd7aedb0079d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'London': 921, 'México D.F.': 899, 'Sao Paulo': 773, 'Rio de Janeiro': 545, 'Buenos Aires': 535, 'Berlin': 376, 'Nantes': 360, 'Lisboa': 357, 'Madrid': 345, 'Portland': 340}}

### Column: `ShipRegion`
- ID: aea35d32-a7dd-470d-8ebc-78dbd5c44acb
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Western Europe': 5056, 'South America': 2925, 'North America': 2875, 'Southern Europe': 1586, 'British Isles': 1452, 'Central America': 899, 'Northern Europe': 743, 'Scandinavia': 533, 'Eastern Europe': 213}}

### Column: `ShipPostalCode`
- ID: d0e7b9c0-5a5a-473e-af6c-7fed22ad93c5
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16110
- Null count: 172
- Categorical statistics: {'value_counts': {'1010': 535, '12209': 376, '5022': 360, '44000': 360, '5033': 351, '8010': 217, '01-012': 213, '5021': 209, '05487-020': 207, 'S-844 67': 205}}

### Column: `ShipCountry`
- ID: 0e8fa030-45e0-48e7-b743-92c7330bbc22
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 2328, 'Germany': 2193, 'France': 1778, 'Brazil': 1683, 'UK': 1280, 'Mexico': 899, 'Venezuela': 707, 'Spain': 691, 'Canada': 547, 'Italy': 538}}

### Column: `OrderID`
- ID: a43b85f8-7162-41a3-bfcd-77757ddeae5d
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 18388.5, 'std': None, 'min': 10248, 'q2': None, 'median': None, 'q3': None, 'max': 26529}

### Column: `CustomerID`
- ID: 1931e5b9-18a9-4079-9051-738029f36c76
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'BSBEV': 210, 'RICAR': 203, 'LILAS': 203, 'GOURL': 202, 'PRINI': 200, 'HUNGC': 198, 'TORTU': 197, 'FOLIG': 195, 'ANATR': 195, 'RANCH': 194}}

### Column: `EmployeeID`
- ID: ccfa910e-a6f8-49e6-954d-2138e3ef6d7c
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 4.96886131924825, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `OrderDate`
- ID: e12d3dce-f78d-47f0-bfe3-8aa4afd1e740
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `RequiredDate`
- ID: bbd20bd0-b23d-4d76-9606-a2198dd09f16
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `ShippedDate`
- ID: c303d001-34ce-406e-a8fc-0d6857e3359f
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16261
- Null count: 21

### Column: `ShipVia`
- ID: 601fca0f-9c27-4833-86d0-48f8383437a0
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 2.007738607050731, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 3}

## Table: `Products`
- ID: 23bdb40f-b7eb-4455-a550-e1e11b52589f
- Primary Keys: ProductID.
- Shape: 77 row(s), 10 column(s).

### Column: `ProductID`
- ID: dc55e671-0d2b-4845-b39a-31f976781892
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 39.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 77}

### Column: `ProductName`
- ID: f8a0dd49-a522-4b39-ba4a-52b3e56450a9
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaanse koeken': 1, 'Wimmers gute Semmelknödel': 1, 'Vegie-spread': 1, 'Valkoinen suklaa': 1, "Uncle Bob's Organic Dried Pears": 1, 'Tunnbröd': 1, 'Tourtière': 1, 'Tofu': 1, 'Thüringer Rostbratwurst': 1, 'Teatime Chocolate Biscuits': 1}}

### Column: `SupplierID`
- ID: 97c6985b-f361-47b7-a511-65abeff7f857
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 13.64935064935065, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 29}

### Column: `CategoryID`
- ID: 18752bcb-a929-43e5-bbde-5664733015c1
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 4.116883116883117, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 8}

### Column: `QuantityPerUnit`
- ID: cebb8a59-bbd0-40dd-9b85-7a043fcd90b2
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'24 - 12 oz bottles': 4, '5 kg pkg.': 2, '24 - 250 g pkgs.': 2, '24 - 200 g pkgs.': 2, '10 - 500 g pkgs.': 2, '750 cc per bottle': 1, '500 ml': 1, '500 g': 1, '50 bags x 30 sausgs.': 1, '50 - 300 g pkgs.': 1}}

### Column: `UnitPrice`
- ID: 47e0c1d8-d3cd-461b-b6f5-65ccf3505074
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0

### Column: `UnitsInStock`
- ID: 31fe2949-5401-468d-aed0-64d4f8fa122b
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 40.506493506493506, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 125}

### Column: `UnitsOnOrder`
- ID: 0e2b795d-6964-4a42-84b6-1f9269754954
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 10.12987012987013, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 100}

### Column: `ReorderLevel`
- ID: 957913b8-5a3a-4b44-ae68-2e7cab4fe22c
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 12.467532467532468, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 30}

### Column: `Discontinued`
- ID: 31bd44de-6eb3-4a66-bdcb-22453e3aad72
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'0': 69, '1': 8}}

## Table: `Regions`
- ID: ce5f3566-966b-4b0e-ac06-dfc1ec9cd53d
- Primary Keys: RegionID.
- Shape: 4 row(s), 2 column(s).

### Column: `RegionID`
- ID: 88373f02-73a7-4248-b2b0-2f478320a323
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 4
- Null count: 0
- Numerical statistics: {'mean': 2.5, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 4}

### Column: `RegionDescription`
- ID: 30cccc13-1be0-4621-8bc7-71453fe69a74
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 4
- Null count: 0
- Categorical statistics: {'value_counts': {'Western': 1, 'Southern': 1, 'Northern': 1, 'Eastern': 1}}

## Table: `Shippers`
- ID: 41a418ee-92f2-4b42-bad3-2ff144ac851f
- Primary Keys: ShipperID.
- Shape: 3 row(s), 3 column(s).

### Column: `ShipperID`
- ID: d3593656-7414-4dcc-b6a9-0daff3500dce
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 3
- Null count: 0
- Numerical statistics: {'mean': 2.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 3}

### Column: `CompanyName`
- ID: 7c8bbc27-7e1e-4b4d-9017-afdb7818b1b0
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 3
- Null count: 0
- Categorical statistics: {'value_counts': {'United Package': 1, 'Speedy Express': 1, 'Federal Shipping': 1}}

### Column: `Phone`
- ID: 1d16e744-0f04-4445-a120-964eaa60622f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 3
- Null count: 0
- Categorical statistics: {'value_counts': {'(503) 555-9931': 1, '(503) 555-9831': 1, '(503) 555-3199': 1}}

## Table: `Suppliers`
- ID: ebe5b00a-4cf0-4cad-9349-7cec2e75679a
- Primary Keys: SupplierID.
- Shape: 29 row(s), 12 column(s).

### Column: `Fax`
- ID: 2d372503-fad3-4441-bc60-d47932d1640d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 13
- Null count: 16
- Categorical statistics: {'value_counts': {'43844115': 1, '38.76.98.58': 1, '031-987 65 91': 1, '(617) 555-3389': 1, '(514) 555-2921': 1, '(313) 555-3349': 1, '(12345) 1210': 1, '(1) 03.83.00.62': 1, '(089) 6547667': 1, '(0544) 60603': 1}}

### Column: `HomePage`
- ID: 846ed4b6-ca1e-4275-b6a3-79858d93b621
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 5
- Null count: 24
- Categorical statistics: {'value_counts': {'Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#': 1, "Mayumi's (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/mayumi.htm#": 1, "G'day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#": 1, '#FORMAGGI.HTM#': 1, '#CAJUN.HTM#': 1}}

### Column: `SupplierID`
- ID: ac47be75-0bc8-456e-aa31-bc5bc5acc429
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 29
- Null count: 0
- Numerical statistics: {'mean': 15.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 29}

### Column: `CompanyName`
- ID: efa6d523-dc8e-49c9-ae4b-0b94b8aebabf
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaanse Snoepfabriek': 1, 'Tokyo Traders': 1, 'Svensk Sjöföda AB': 1, 'Specialty Biscuits, Ltd.': 1, 'Refrescos Americanas LTDA': 1, 'Plutzer Lebensmittelgroßmärkte AG': 1, 'Pavlova, Ltd.': 1, 'Pasta Buttini s.r.l.': 1, 'PB Knäckebröd AB': 1, 'Norske Meierier': 1}}

### Column: `ContactName`
- ID: a700e6ba-be69-4da9-9c57-20847197e4fd
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Yoshi Nagase': 1, 'Wendy Mackenzie': 1, 'Sven Petersen': 1, 'Shelley Burke': 1, 'Robb Merchant': 1, 'Regina Murphy': 1, 'Petra Winkler': 1, 'Peter Wilson': 1, 'Niels Petersen': 1, 'Michael Björn': 1}}

### Column: `ContactTitle`
- ID: 192ad429-6c1d-4c36-8073-beef923b6da3
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 6, 'Marketing Manager': 5, 'Sales Manager': 4, 'Order Administrator': 2, 'Accounting Manager': 2, 'Wholesale Account Agent': 1, 'Sales Agent': 1, 'Regional Account Rep.': 1, 'Purchasing Manager': 1, 'Product Manager': 1}}

### Column: `Address`
- ID: 93900ee3-6796-4da6-9cf2-7533bcfafc7f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Viale Dante, 75': 1, 'Via dei Gelsomini, 153': 1, 'Verkoop\nRijnweg 22': 1, 'Valtakatu 12': 1, 'Tiergartenstraße 5': 1, 'P.O. Box 78934': 1, 'Order Processing Dept.\n2100 Paul Revere Blvd.': 1, 'Lyngbysild\nFiskebakken 10': 1, 'Kaloadagatan 13': 1, 'Hatlevegen 5': 1}}

### Column: `City`
- ID: 29fb86b7-13f6-4a23-ab24-26d68881624f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaandam': 1, 'Tokyo': 1, 'São Paulo': 1, 'Sydney': 1, 'Stockholm': 1, 'Ste-Hyacinthe': 1, 'Singapore': 1, 'Sandvika': 1, 'Salerno': 1, 'Ravenna': 1}}

### Column: `Region`
- ID: 583eef62-19d6-4587-aab5-b2e8a1166284
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 28
- Null count: 1
- Categorical statistics: {'value_counts': {'Western Europe': 6, 'North America': 6, 'Southern Europe': 3, 'Northern Europe': 3, 'Scandinavia': 2, 'Eastern Asia': 2, 'British Isles': 2, 'Victoria': 1, 'South-East Asia': 1, 'South America': 1}}

### Column: `PostalCode`
- ID: 217676d6-1ac5-48f3-b79c-6f00792a9baa
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'S-345 67': 1, 'S-123 45': 1, 'M14 GSD': 1, 'J2S 7S8': 1, 'H1J 1C3': 1, 'EC1 4SD': 1, '9999 ZZ': 1, '97101': 1, '84100': 1, '75004': 1}}

### Column: `Country`
- ID: f361d250-a477-4e01-9871-874803a14b68
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 4, 'Germany': 3, 'France': 3, 'UK': 2, 'Japan': 2, 'Italy': 2, 'Canada': 2, 'Australia': 2, 'Sweden ': 1, 'Sweden': 1}}

### Column: `Phone`
- ID: c225f85d-1383-4875-a2c3-8719f153b630
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'85.57.00.07': 1, '555-8787': 1, '43844108': 1, '38.76.98.06': 1, '08-123 45 67': 1, '031-987 65 43': 1, '(98) 598 76 54': 1, '(953) 10956': 1, '(617) 555-3267': 1, '(514) 555-9022': 1}}

## Table: `Territories`
- ID: 477127da-f666-450e-a8a6-3365c00444f4
- Primary Keys: TerritoryID.
- Shape: 53 row(s), 3 column(s).

### Column: `TerritoryID`
- ID: ce2317ea-f7cb-4beb-954d-bfb8e8c97581
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 53
- Null count: 0
- Categorical statistics: {'value_counts': {'01581': 1, '01730': 1, '01833': 1, '02116': 1, '02139': 1, '02184': 1, '02903': 1, '03049': 1, '03801': 1, '06897': 1}}

### Column: `TerritoryDescription`
- ID: c7d01927-3b2b-4b95-94d6-8fedb9d1bc0d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 53
- Null count: 0
- Categorical statistics: {'value_counts': {'New York': 2, 'Wilton': 1, 'Westboro': 1, 'Troy': 1, 'Tampa': 1, 'Southfield': 1, 'Seattle': 1, 'Scottsdale': 1, 'Savannah': 1, 'Santa Monica': 1}}

### Column: `RegionID`
- ID: 38c16615-13eb-4548-899f-77e5bc6c7fd9
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 53
- Null count: 0
- Numerical statistics: {'mean': 2.150943396226415, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 4}

## List of foreign keys constraints
- `CustomerCustomerDemo`.`CustomerTypeID` -> `CustomerDemographics`.`CustomerTypeID`
- `CustomerCustomerDemo`.`CustomerID` -> `Customers`.`CustomerID`
- `Employees`.`ReportsTo` -> `Employees`.`EmployeeID`
- `EmployeeTerritories`.`TerritoryID` -> `Territories`.`TerritoryID`
- `EmployeeTerritories`.`EmployeeID` -> `Employees`.`EmployeeID`
- `Order Details`.`ProductID` -> `Products`.`ProductID`
- `Order Details`.`OrderID` -> `Orders`.`OrderID`
- `Orders`.`ShipVia` -> `Shippers`.`ShipperID`
- `Orders`.`CustomerID` -> `Customers`.`CustomerID`
- `Orders`.`EmployeeID` -> `Employees`.`EmployeeID`
- `Products`.`SupplierID` -> `Suppliers`.`SupplierID`
- `Products`.`CategoryID` -> `Categories`.`CategoryID`
- `Territories`.`RegionID` -> `Regions`.`RegionID`
## Table: `Categories`
- ID: 8ab5a624-0596-497e-a0ee-3996d95dbe63
- Primary Keys: CategoryID.
- Shape: 8 row(s), 4 column(s).

### Column: `Picture`
- ID: 25ad7169-e449-40a6-95c9-8e09975036fa
- Data type: BLOB
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0

### Column: `CategoryID`
- ID: 04c20046-2808-4021-bbf1-99876e0eea6e
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: True
- Non null count: 8
- Null count: 0
- Numerical statistics: {'mean': 4.5, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 8}

### Column: `CategoryName`
- ID: 815cd167-41f4-45d9-a467-0ed9dd8a8ec8
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0
- Categorical statistics: {'value_counts': {'Seafood': 1, 'Produce': 1, 'Meat/Poultry': 1, 'Grains/Cereals': 1, 'Dairy Products': 1, 'Confections': 1, 'Condiments': 1, 'Beverages': 1}}

### Column: `Description`
- ID: 21fcbf83-627d-4ff0-957f-5e3b3dddcb25
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 0
- Categorical statistics: {'value_counts': {'Sweet and savory sauces, relishes, spreads, and seasonings': 1, 'Soft drinks, coffees, teas, beers, and ales': 1, 'Seaweed and fish': 1, 'Prepared meats': 1, 'Dried fruit and bean curd': 1, 'Desserts, candies, and sweet breads': 1, 'Cheeses': 1, 'Breads, crackers, pasta, and cereal': 1}}

## Table: `CustomerCustomerDemo`
- ID: e1ea6b2c-3a25-4257-8eb7-ffa81b16b55f
- Primary Keys: CustomerID.
- Shape: 0 row(s), 2 column(s).

### Column: `CustomerID`
- ID: 707ed661-a134-48a9-bfd1-0966c06c962e
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

### Column: `CustomerTypeID`
- ID: f1668f51-ff26-46c1-b9b7-48813b3dbc37
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

## Table: `CustomerDemographics`
- ID: 169809a7-e312-4bac-9a68-d05105d14d7c
- Primary Keys: CustomerTypeID.
- Shape: 0 row(s), 2 column(s).

### Column: `CustomerTypeID`
- ID: 966a9cdc-7516-4b46-83ec-e33349896da8
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

### Column: `CustomerDesc`
- ID: 87dde91e-ae61-4dd8-810a-1bff7e5204ac
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 0
- Null count: 0
- Categorical statistics: {'value_counts': {}}

## Table: `Customers`
- ID: 09594675-9477-4331-8850-c2922cb0554f
- Primary Keys: CustomerID.
- Shape: 93 row(s), 11 column(s).

### Column: `CustomerID`
- ID: 6d8f6099-28b1-4e2e-98cf-227918948955
- Data type: TEXT
- Is Primary Key: True
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'ALFKI': 1, 'ANATR': 1, 'ANTON': 1, 'AROUT': 1, 'BERGS': 1, 'BLAUS': 1, 'BLONP': 1, 'BOLID': 1, 'BONAP': 1, 'BOTTM': 1}}

### Column: `CompanyName`
- ID: 3a4ea0d0-23c3-4115-9ebf-f64346f24464
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'IT': 2, 'Wolski  Zajazd': 1, 'Wilman Kala': 1, 'White Clover Markets': 1, 'Wellington Importadora': 1, 'Wartian Herkku': 1, 'Vins et alcools Chevalier': 1, 'Victuailles en stock': 1, 'Vaffeljernet': 1, "Trail's Head Gourmet Provisioners": 1}}

### Column: `ContactName`
- ID: c45ec1d3-e249-4e11-85ca-b8e611092d57
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'Zbyszek Piestrzeniewicz': 1, 'Yvonne Moncada': 1, 'Yoshi Tannamuri': 1, 'Yoshi Latimer': 1, 'Yang Wang': 1, 'Victoria Ashworth': 1, 'Valon Hoti': 1, 'Val2': 1, 'Thomas Hardy': 1, 'Sven Ottlieb': 1}}

### Column: `ContactTitle`
- ID: 97f93fdb-53ef-4e2b-9abf-21d1947ac492
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 93
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 17, 'Owner': 17, 'Marketing Manager': 12, 'Sales Manager': 11, 'Accounting Manager': 10, 'Sales Associate': 7, 'Marketing Assistant': 6, 'Sales Agent': 5, 'Order Administrator': 2, 'IT': 2}}

### Column: `Address`
- ID: c1440edd-6e14-42be-a4a0-09a83a55b0d7
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'Åkergatan 24': 1, 'ul. Filtrowa 68': 1, 'Walserweg 21': 1, 'Vinbæltet 34': 1, 'Via Monte Bianco 34': 1, 'Via Ludovico il Moro 22': 1, 'Torikatu 38': 1, 'Taucherstraße 10': 1, 'Strada Provinciale 124': 1, 'South House 300 Queensbridge': 1}}

### Column: `City`
- ID: 70e73112-d0a4-4ca5-8ae3-d3ca35a6c82d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'London': 6, 'México D.F.': 5, 'Sao Paulo': 4, 'Rio de Janeiro': 3, 'Madrid': 3, 'Buenos Aires': 3, 'Portland': 2, 'Paris': 2, 'Nantes': 2, 'Lisboa': 2}}

### Column: `Region`
- ID: 36cace1c-6d19-4d9f-9d7a-2808a05bbd8a
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'Western Europe': 28, 'South America': 16, 'North America': 16, 'Southern Europe': 10, 'British Isles': 8, 'Central America': 5, 'Northern Europe': 4, 'Scandinavia': 3, 'Eastern Europe': 1}}

### Column: `PostalCode`
- ID: cf00c753-955a-425e-b6b8-be2a75e7eb4c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 90
- Null count: 3
- Categorical statistics: {'value_counts': {'1010': 3, '44000': 2, '05033': 2, 'WX3 6FW': 1, 'WX1 6LT': 1, 'WA1 1DP': 1, 'V3F 2K1': 1, 'T2F 8M4': 1, 'SW7 1RZ': 1, 'S-958 22': 1}}

### Column: `Country`
- ID: 1143644d-9aeb-414b-b267-92749b3eae60
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'USA': 13, 'Germany': 11, 'France': 11, 'Brazil': 9, 'UK': 7, 'Spain': 5, 'Mexico': 5, 'Venezuela': 4, 'Italy': 3, 'Canada': 3}}

### Column: `Phone`
- ID: 78ddf161-80e0-48ed-8acb-e47fb6970d5a
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 91
- Null count: 2
- Categorical statistics: {'value_counts': {'981-443655': 1, '91.24.45.40': 1, '90-224 8858': 1, '88.60.15.31': 1, '86 21 32 43': 1, '78.32.54.86': 1, '7675-3425': 1, '6562-9722': 1, '61.77.61.10': 1, '40.67.88.88': 1}}

### Column: `Fax`
- ID: 29c30aa2-23c7-41fb-a473-e0577b5015a8
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 69
- Null count: 24
- Categorical statistics: {'value_counts': {'981-443655': 1, '91.24.45.41': 1, '90-224 8858': 1, '88.60.15.32': 1, '86 22 33 44': 1, '78.32.54.87': 1, '7675-3426': 1, '6562-9723': 1, '61.77.61.11': 1, '40.67.89.89': 1}}

## Table: `Employees`
- ID: d6090517-bb47-413b-a951-db0d8bf65c46
- Primary Keys: EmployeeID.
- Shape: 9 row(s), 18 column(s).

### Column: `EmployeeID`
- ID: 055d5005-5498-42f0-8815-569ba1622e3f
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: True
- Non null count: 9
- Null count: 0
- Numerical statistics: {'mean': 5.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `LastName`
- ID: 8ed5ab15-bfd6-4571-84ba-57ceae6f6632
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Suyama': 1, 'Peacock': 1, 'Leverling': 1, 'King': 1, 'Fuller': 1, 'Dodsworth': 1, 'Davolio': 1, 'Callahan': 1, 'Buchanan': 1}}

### Column: `FirstName`
- ID: 2f779241-dc95-4367-9d0f-e6612facaeac
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Steven': 1, 'Robert': 1, 'Nancy': 1, 'Michael': 1, 'Margaret': 1, 'Laura': 1, 'Janet': 1, 'Anne': 1, 'Andrew': 1}}

### Column: `Title`
- ID: 346d6b29-09c0-4a95-8086-bb800c6890f1
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 6, 'Vice President, Sales': 1, 'Sales Manager': 1, 'Inside Sales Coordinator': 1}}

### Column: `TitleOfCourtesy`
- ID: 902ebc10-0411-487e-85ac-70c48ea85620
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Ms.': 4, 'Mr.': 3, 'Mrs.': 1, 'Dr.': 1}}

### Column: `BirthDate`
- ID: f2d0e7f9-e881-4179-8705-96b3a2770d5e
- Data type: DATE
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `HireDate`
- ID: a378b57c-c080-4f1e-99be-04c7f1ac2719
- Data type: DATE
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `Address`
- ID: a60c5adb-1097-472d-8092-2f7c64ec410f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Edgeham Hollow\nWinchester Way': 1, 'Coventry House\nMiner Rd.': 1, '908 W. Capital Way': 1, '722 Moss Bay Blvd.': 1, '7 Houndstooth Rd.': 1, '507 - 20th Ave. E.Apt. 2A': 1, '4726 - 11th Ave. N.E.': 1, '4110 Old Redmond Rd.': 1, '14 Garrett Hill': 1}}

### Column: `City`
- ID: 18296191-f80c-433e-bdaa-d4cabec24a98
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'London': 4, 'Seattle': 2, 'Tacoma': 1, 'Redmond': 1, 'Kirkland': 1}}

### Column: `Region`
- ID: 9f56dac0-54d6-411f-bd13-d95c902d20d0
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'North America': 5, 'British Isles': 4}}

### Column: `PostalCode`
- ID: cbc88037-a5f0-4cd3-84e7-8d740c5fe968
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'WG2 7LT': 1, 'SW1 8JR': 1, 'RG1 9SP': 1, 'EC2 7JR': 1, '98401': 1, '98122': 1, '98105': 1, '98052': 1, '98033': 1}}

### Column: `Country`
- ID: 7a782190-5167-48c9-80a6-d959c46ed009
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 5, 'UK': 4}}

### Column: `HomePhone`
- ID: ef1cb775-2612-4b47-b650-b301ff943173
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'(71) 555-7773': 1, '(71) 555-5598': 1, '(71) 555-4848': 1, '(71) 555-4444': 1, '(206) 555-9857': 1, '(206) 555-9482': 1, '(206) 555-8122': 1, '(206) 555-3412': 1, '(206) 555-1189': 1}}

### Column: `Extension`
- ID: 311451a6-beca-4428-89de-eb45a8ce7f4c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'5467': 1, '5176': 1, '465': 1, '452': 1, '428': 1, '3457': 1, '3453': 1, '3355': 1, '2344': 1}}

### Column: `Photo`
- ID: 14ee59f6-36ef-49b6-9b1e-2e21df6141dc
- Data type: BLOB
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0

### Column: `Notes`
- ID: 1fd877cb-a607-45ec-8878-9194429c2f71
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses "Successful Telemarketing" and "International Sales Management."  He is fluent in French.': 1, 'Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan in 1992, the year he joined the company.  After completing a course entitled "Selling in Europe," he was transferred to the London office in March 1993.': 1, 'Michael is a graduate of Sussex University (MA, economics, 1983) and the University of California at Los Angeles (MBA, marketing, 1986).  He has also taken the courses "Multi-Cultural Selling" and "Time Management for the Sales Professional."  He is fluent in Japanese and can read and write French, Portuguese, and Spanish.': 1, 'Margaret holds a BA in English literature from Concordia College (1958) and an MA from the American Institute of Culinary Arts (1966).  She was assigned to the London office temporarily from July through November 1992.': 1, 'Laura received a BA in psychology from the University of Washington.  She has also completed a course in business French.  She reads and writes French.': 1, 'Janet has a BS degree in chemistry from Boston College (1984).  She has also completed a certificate program in food retailing management.  Janet was hired as a sales associate in 1991 and promoted to sales representative in February 1992.': 1, 'Education includes a BA in psychology from Colorado State University in 1970.  She also completed "The Art of the Cold Call."  Nancy is a member of Toastmasters International.': 1, 'Anne has a BA degree in English from St. Lawrence College.  She is fluent in French and German.': 1, 'Andrew received his BTS commercial in 1974 and a Ph.D. in international marketing from the University of Dallas in 1981.  He is fluent in French and Italian and reads German.  He joined the company as a sales representative, was promoted to sales manager in January 1992 and to vice president of sales in March 1993.  Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association.': 1}}

### Column: `ReportsTo`
- ID: 946d404b-1671-412a-bb08-941798554007
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 8
- Null count: 1
- Numerical statistics: {'mean': 3.125, 'std': None, 'min': 2, 'q2': None, 'median': None, 'q3': None, 'max': 5}

### Column: `PhotoPath`
- ID: d35c52e4-832c-4b2a-bb05-d6a9d45a4491
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 9
- Null count: 0
- Categorical statistics: {'value_counts': {'http://accweb/emmployees/davolio.bmp': 5, 'http://accweb/emmployees/peacock.bmp': 1, 'http://accweb/emmployees/leverling.bmp': 1, 'http://accweb/emmployees/fuller.bmp': 1, 'http://accweb/emmployees/buchanan.bmp': 1}}

## Table: `EmployeeTerritories`
- ID: cfe51f37-7ec6-423e-a5ff-69b06753125e
- Primary Keys: EmployeeID.
- Shape: 49 row(s), 2 column(s).

### Column: `EmployeeID`
- ID: ee1b41be-2d01-4dd0-896d-53cf3aa68d81
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 49
- Null count: 0
- Numerical statistics: {'mean': 5.510204081632653, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `TerritoryID`
- ID: 1f5ac5f7-6883-4b4d-8f54-0f32afc717fb
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 49
- Null count: 0
- Categorical statistics: {'value_counts': {'98104': 1, '98052': 1, '98004': 1, '95060': 1, '95054': 1, '95008': 1, '94105': 1, '94025': 1, '90405': 1, '85251': 1}}

## Table: `Order Details`
- ID: a03335e3-414c-4559-8764-66d67e903525
- Primary Keys: OrderID.
- Shape: 609283 row(s), 5 column(s).

### Column: `OrderID`
- ID: f3f851d4-e43f-4413-86f5-942fac652d2b
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 18785.56068526448, 'std': None, 'min': 10248, 'q2': None, 'median': None, 'q3': None, 'max': 26529}

### Column: `ProductID`
- ID: cdee512d-6316-4af3-91ad-cc4a7e1f3b4e
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 38.99956342126729, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 77}

### Column: `UnitPrice`
- ID: 06eda878-ecfa-4610-841b-01161017cd02
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0

### Column: `Quantity`
- ID: 8d8c0dbb-3ee3-4778-9d43-0710927ec8f2
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 25.503094621054583, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 130}

### Column: `Discount`
- ID: 3c216408-0e7c-4329-833a-7ca0ba9aa9d5
- Data type: REAL
- Is Primary Key: False
- Is nullable: False
- Non null count: 609283
- Null count: 0
- Numerical statistics: {'mean': 0.00019865973611605774, 'std': None, 'min': 0.0, 'q2': None, 'median': None, 'q3': None, 'max': 0.25}

## Table: `Orders`
- ID: 20414a87-96a2-4314-887c-a247daf4b160
- Primary Keys: OrderID.
- Shape: 16282 row(s), 14 column(s).

### Column: `Freight`
- ID: 9b0a23b2-230a-413f-97bc-4bb6dabc430f
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `ShipName`
- ID: bd3f6cab-a437-40a8-b54d-6b3254c2c0f7
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Ernst Handel': 217, 'Wolski Zajazd': 213, 'Ana Trujillo Emparedados y helados': 209, 'Queen Cozinha': 207, 'Folk och fä HB': 205, 'Save-a-lot Markets': 204, 'Consolidated Holdings': 203, 'HILARION-Abastos': 202, 'Wartian Herkku': 201, 'Seven Seas Imports': 199}}

### Column: `ShipAddress`
- ID: 0093ef8a-e38a-46b2-ba33-f9b25249b96c
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Obere Str. 57': 376, 'Kirchgasse 6': 217, 'ul. Filtrowa 68': 213, 'Avda. de la Constitución 2222': 209, 'Alameda dos Canàrios, 891': 207, 'Åkergatan 24': 205, '187 Suffolk Ln.': 204, 'Berkeley Gardens 12 \xa0Brewery': 203, 'Carrera 22 con Ave. Carlos Soublette #8-35': 202, 'Torikatu 38': 201}}

### Column: `ShipCity`
- ID: ea44ff9f-8cb2-4631-94c2-cd7aedb0079d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'London': 921, 'México D.F.': 899, 'Sao Paulo': 773, 'Rio de Janeiro': 545, 'Buenos Aires': 535, 'Berlin': 376, 'Nantes': 360, 'Lisboa': 357, 'Madrid': 345, 'Portland': 340}}

### Column: `ShipRegion`
- ID: aea35d32-a7dd-470d-8ebc-78dbd5c44acb
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'Western Europe': 5056, 'South America': 2925, 'North America': 2875, 'Southern Europe': 1586, 'British Isles': 1452, 'Central America': 899, 'Northern Europe': 743, 'Scandinavia': 533, 'Eastern Europe': 213}}

### Column: `ShipPostalCode`
- ID: d0e7b9c0-5a5a-473e-af6c-7fed22ad93c5
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16110
- Null count: 172
- Categorical statistics: {'value_counts': {'1010': 535, '12209': 376, '5022': 360, '44000': 360, '5033': 351, '8010': 217, '01-012': 213, '5021': 209, '05487-020': 207, 'S-844 67': 205}}

### Column: `ShipCountry`
- ID: 0e8fa030-45e0-48e7-b743-92c7330bbc22
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 2328, 'Germany': 2193, 'France': 1778, 'Brazil': 1683, 'UK': 1280, 'Mexico': 899, 'Venezuela': 707, 'Spain': 691, 'Canada': 547, 'Italy': 538}}

### Column: `OrderID`
- ID: a43b85f8-7162-41a3-bfcd-77757ddeae5d
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 18388.5, 'std': None, 'min': 10248, 'q2': None, 'median': None, 'q3': None, 'max': 26529}

### Column: `CustomerID`
- ID: 1931e5b9-18a9-4079-9051-738029f36c76
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Categorical statistics: {'value_counts': {'BSBEV': 210, 'RICAR': 203, 'LILAS': 203, 'GOURL': 202, 'PRINI': 200, 'HUNGC': 198, 'TORTU': 197, 'FOLIG': 195, 'ANATR': 195, 'RANCH': 194}}

### Column: `EmployeeID`
- ID: ccfa910e-a6f8-49e6-954d-2138e3ef6d7c
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 4.96886131924825, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 9}

### Column: `OrderDate`
- ID: e12d3dce-f78d-47f0-bfe3-8aa4afd1e740
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `RequiredDate`
- ID: bbd20bd0-b23d-4d76-9606-a2198dd09f16
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0

### Column: `ShippedDate`
- ID: c303d001-34ce-406e-a8fc-0d6857e3359f
- Data type: DATETIME
- Is Primary Key: False
- Is nullable: True
- Non null count: 16261
- Null count: 21

### Column: `ShipVia`
- ID: 601fca0f-9c27-4833-86d0-48f8383437a0
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 16282
- Null count: 0
- Numerical statistics: {'mean': 2.007738607050731, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 3}

## Table: `Products`
- ID: 23bdb40f-b7eb-4455-a550-e1e11b52589f
- Primary Keys: ProductID.
- Shape: 77 row(s), 10 column(s).

### Column: `ProductID`
- ID: dc55e671-0d2b-4845-b39a-31f976781892
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 39.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 77}

### Column: `ProductName`
- ID: f8a0dd49-a522-4b39-ba4a-52b3e56450a9
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaanse koeken': 1, 'Wimmers gute Semmelknödel': 1, 'Vegie-spread': 1, 'Valkoinen suklaa': 1, "Uncle Bob's Organic Dried Pears": 1, 'Tunnbröd': 1, 'Tourtière': 1, 'Tofu': 1, 'Thüringer Rostbratwurst': 1, 'Teatime Chocolate Biscuits': 1}}

### Column: `SupplierID`
- ID: 97c6985b-f361-47b7-a511-65abeff7f857
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 13.64935064935065, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 29}

### Column: `CategoryID`
- ID: 18752bcb-a929-43e5-bbde-5664733015c1
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 4.116883116883117, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 8}

### Column: `QuantityPerUnit`
- ID: cebb8a59-bbd0-40dd-9b85-7a043fcd90b2
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'24 - 12 oz bottles': 4, '5 kg pkg.': 2, '24 - 250 g pkgs.': 2, '24 - 200 g pkgs.': 2, '10 - 500 g pkgs.': 2, '750 cc per bottle': 1, '500 ml': 1, '500 g': 1, '50 bags x 30 sausgs.': 1, '50 - 300 g pkgs.': 1}}

### Column: `UnitPrice`
- ID: 47e0c1d8-d3cd-461b-b6f5-65ccf3505074
- Data type: NUMERIC
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0

### Column: `UnitsInStock`
- ID: 31fe2949-5401-468d-aed0-64d4f8fa122b
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 40.506493506493506, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 125}

### Column: `UnitsOnOrder`
- ID: 0e2b795d-6964-4a42-84b6-1f9269754954
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 10.12987012987013, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 100}

### Column: `ReorderLevel`
- ID: 957913b8-5a3a-4b44-ae68-2e7cab4fe22c
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: True
- Non null count: 77
- Null count: 0
- Numerical statistics: {'mean': 12.467532467532468, 'std': None, 'min': 0, 'q2': None, 'median': None, 'q3': None, 'max': 30}

### Column: `Discontinued`
- ID: 31bd44de-6eb3-4a66-bdcb-22453e3aad72
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 77
- Null count: 0
- Categorical statistics: {'value_counts': {'0': 69, '1': 8}}

## Table: `Regions`
- ID: ce5f3566-966b-4b0e-ac06-dfc1ec9cd53d
- Primary Keys: RegionID.
- Shape: 4 row(s), 2 column(s).

### Column: `RegionID`
- ID: 88373f02-73a7-4248-b2b0-2f478320a323
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 4
- Null count: 0
- Numerical statistics: {'mean': 2.5, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 4}

### Column: `RegionDescription`
- ID: 30cccc13-1be0-4621-8bc7-71453fe69a74
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 4
- Null count: 0
- Categorical statistics: {'value_counts': {'Western': 1, 'Southern': 1, 'Northern': 1, 'Eastern': 1}}

## Table: `Shippers`
- ID: 41a418ee-92f2-4b42-bad3-2ff144ac851f
- Primary Keys: ShipperID.
- Shape: 3 row(s), 3 column(s).

### Column: `ShipperID`
- ID: d3593656-7414-4dcc-b6a9-0daff3500dce
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 3
- Null count: 0
- Numerical statistics: {'mean': 2.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 3}

### Column: `CompanyName`
- ID: 7c8bbc27-7e1e-4b4d-9017-afdb7818b1b0
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 3
- Null count: 0
- Categorical statistics: {'value_counts': {'United Package': 1, 'Speedy Express': 1, 'Federal Shipping': 1}}

### Column: `Phone`
- ID: 1d16e744-0f04-4445-a120-964eaa60622f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 3
- Null count: 0
- Categorical statistics: {'value_counts': {'(503) 555-9931': 1, '(503) 555-9831': 1, '(503) 555-3199': 1}}

## Table: `Suppliers`
- ID: ebe5b00a-4cf0-4cad-9349-7cec2e75679a
- Primary Keys: SupplierID.
- Shape: 29 row(s), 12 column(s).

### Column: `Fax`
- ID: 2d372503-fad3-4441-bc60-d47932d1640d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 13
- Null count: 16
- Categorical statistics: {'value_counts': {'43844115': 1, '38.76.98.58': 1, '031-987 65 91': 1, '(617) 555-3389': 1, '(514) 555-2921': 1, '(313) 555-3349': 1, '(12345) 1210': 1, '(1) 03.83.00.62': 1, '(089) 6547667': 1, '(0544) 60603': 1}}

### Column: `HomePage`
- ID: 846ed4b6-ca1e-4275-b6a3-79858d93b621
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 5
- Null count: 24
- Categorical statistics: {'value_counts': {'Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#': 1, "Mayumi's (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/mayumi.htm#": 1, "G'day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#": 1, '#FORMAGGI.HTM#': 1, '#CAJUN.HTM#': 1}}

### Column: `SupplierID`
- ID: ac47be75-0bc8-456e-aa31-bc5bc5acc429
- Data type: INTEGER
- Is Primary Key: True
- Is nullable: False
- Non null count: 29
- Null count: 0
- Numerical statistics: {'mean': 15.0, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 29}

### Column: `CompanyName`
- ID: efa6d523-dc8e-49c9-ae4b-0b94b8aebabf
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaanse Snoepfabriek': 1, 'Tokyo Traders': 1, 'Svensk Sjöföda AB': 1, 'Specialty Biscuits, Ltd.': 1, 'Refrescos Americanas LTDA': 1, 'Plutzer Lebensmittelgroßmärkte AG': 1, 'Pavlova, Ltd.': 1, 'Pasta Buttini s.r.l.': 1, 'PB Knäckebröd AB': 1, 'Norske Meierier': 1}}

### Column: `ContactName`
- ID: a700e6ba-be69-4da9-9c57-20847197e4fd
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Yoshi Nagase': 1, 'Wendy Mackenzie': 1, 'Sven Petersen': 1, 'Shelley Burke': 1, 'Robb Merchant': 1, 'Regina Murphy': 1, 'Petra Winkler': 1, 'Peter Wilson': 1, 'Niels Petersen': 1, 'Michael Björn': 1}}

### Column: `ContactTitle`
- ID: 192ad429-6c1d-4c36-8073-beef923b6da3
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Sales Representative': 6, 'Marketing Manager': 5, 'Sales Manager': 4, 'Order Administrator': 2, 'Accounting Manager': 2, 'Wholesale Account Agent': 1, 'Sales Agent': 1, 'Regional Account Rep.': 1, 'Purchasing Manager': 1, 'Product Manager': 1}}

### Column: `Address`
- ID: 93900ee3-6796-4da6-9cf2-7533bcfafc7f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Viale Dante, 75': 1, 'Via dei Gelsomini, 153': 1, 'Verkoop\nRijnweg 22': 1, 'Valtakatu 12': 1, 'Tiergartenstraße 5': 1, 'P.O. Box 78934': 1, 'Order Processing Dept.\n2100 Paul Revere Blvd.': 1, 'Lyngbysild\nFiskebakken 10': 1, 'Kaloadagatan 13': 1, 'Hatlevegen 5': 1}}

### Column: `City`
- ID: 29fb86b7-13f6-4a23-ab24-26d68881624f
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'Zaandam': 1, 'Tokyo': 1, 'São Paulo': 1, 'Sydney': 1, 'Stockholm': 1, 'Ste-Hyacinthe': 1, 'Singapore': 1, 'Sandvika': 1, 'Salerno': 1, 'Ravenna': 1}}

### Column: `Region`
- ID: 583eef62-19d6-4587-aab5-b2e8a1166284
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 28
- Null count: 1
- Categorical statistics: {'value_counts': {'Western Europe': 6, 'North America': 6, 'Southern Europe': 3, 'Northern Europe': 3, 'Scandinavia': 2, 'Eastern Asia': 2, 'British Isles': 2, 'Victoria': 1, 'South-East Asia': 1, 'South America': 1}}

### Column: `PostalCode`
- ID: 217676d6-1ac5-48f3-b79c-6f00792a9baa
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'S-345 67': 1, 'S-123 45': 1, 'M14 GSD': 1, 'J2S 7S8': 1, 'H1J 1C3': 1, 'EC1 4SD': 1, '9999 ZZ': 1, '97101': 1, '84100': 1, '75004': 1}}

### Column: `Country`
- ID: f361d250-a477-4e01-9871-874803a14b68
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'USA': 4, 'Germany': 3, 'France': 3, 'UK': 2, 'Japan': 2, 'Italy': 2, 'Canada': 2, 'Australia': 2, 'Sweden ': 1, 'Sweden': 1}}

### Column: `Phone`
- ID: c225f85d-1383-4875-a2c3-8719f153b630
- Data type: TEXT
- Is Primary Key: False
- Is nullable: True
- Non null count: 29
- Null count: 0
- Categorical statistics: {'value_counts': {'85.57.00.07': 1, '555-8787': 1, '43844108': 1, '38.76.98.06': 1, '08-123 45 67': 1, '031-987 65 43': 1, '(98) 598 76 54': 1, '(953) 10956': 1, '(617) 555-3267': 1, '(514) 555-9022': 1}}

## Table: `Territories`
- ID: 477127da-f666-450e-a8a6-3365c00444f4
- Primary Keys: TerritoryID.
- Shape: 53 row(s), 3 column(s).

### Column: `TerritoryID`
- ID: ce2317ea-f7cb-4beb-954d-bfb8e8c97581
- Data type: TEXT
- Is Primary Key: True
- Is nullable: False
- Non null count: 53
- Null count: 0
- Categorical statistics: {'value_counts': {'01581': 1, '01730': 1, '01833': 1, '02116': 1, '02139': 1, '02184': 1, '02903': 1, '03049': 1, '03801': 1, '06897': 1}}

### Column: `TerritoryDescription`
- ID: c7d01927-3b2b-4b95-94d6-8fedb9d1bc0d
- Data type: TEXT
- Is Primary Key: False
- Is nullable: False
- Non null count: 53
- Null count: 0
- Categorical statistics: {'value_counts': {'New York': 2, 'Wilton': 1, 'Westboro': 1, 'Troy': 1, 'Tampa': 1, 'Southfield': 1, 'Seattle': 1, 'Scottsdale': 1, 'Savannah': 1, 'Santa Monica': 1}}

### Column: `RegionID`
- ID: 38c16615-13eb-4548-899f-77e5bc6c7fd9
- Data type: INTEGER
- Is Primary Key: False
- Is nullable: False
- Non null count: 53
- Null count: 0
- Numerical statistics: {'mean': 2.150943396226415, 'std': None, 'min': 1, 'q2': None, 'median': None, 'q3': None, 'max': 4}

## List of foreign keys constraints
- `CustomerCustomerDemo`.`CustomerTypeID` -> `CustomerDemographics`.`CustomerTypeID`
- `CustomerCustomerDemo`.`CustomerID` -> `Customers`.`CustomerID`
- `Employees`.`ReportsTo` -> `Employees`.`EmployeeID`
- `EmployeeTerritories`.`TerritoryID` -> `Territories`.`TerritoryID`
- `EmployeeTerritories`.`EmployeeID` -> `Employees`.`EmployeeID`
- `Order Details`.`ProductID` -> `Products`.`ProductID`
- `Order Details`.`OrderID` -> `Orders`.`OrderID`
- `Orders`.`ShipVia` -> `Shippers`.`ShipperID`
- `Orders`.`CustomerID` -> `Customers`.`CustomerID`
- `Orders`.`EmployeeID` -> `Employees`.`EmployeeID`
- `Products`.`SupplierID` -> `Suppliers`.`SupplierID`
- `Products`.`CategoryID` -> `Categories`.`CategoryID`
- `Territories`.`RegionID` -> `Regions`.`RegionID`
