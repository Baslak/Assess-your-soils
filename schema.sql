CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name TEXT,
	company TEXT,
    email TEXT,
	password_hash TEXT
);

INSERT INTO users (full_name, company, email) VALUES ('Lucy Kendall', 'VinProof', 'lucy@example.com');

CREATE TABLE spray_program (
    id SERIAL PRIMARY KEY,
    Vine_Stage TEXT,
	E_L INTEGER,
    Product TEXT,
	PD_Target TEXT,
    Notes TEXT,
    Rate_per_Ha INTEGER,
    Rate_per_100L INTEGER,
    CF INTEGER,
    Water_Rate INTEGER,
    Approx_Timing TEXT
);

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Wooly Bud', 4, 'Biopest Oil', 'PM, Mites', 'Do not spray sulfur within 14 days', 2, 1, 1, 200, 'September');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Shoots 10cm', 12, 'Sulphur', 'PM, Mites', 1.2, 0.6, 1, 200, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Shoots 10cm', 12, 'Copper', 'DM', 0.5, 0.25, 1, 200, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Shoots 10cm', 12, 'Kelp', 'Nutriton', 3, 1.5, 1, 200, 'October');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10 days', 15, 'Sulphur', 'PM, Mites', 1.5, 0.5, 1, 300, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10 days', 15, 'Copper', 'DM', 0.75, .25, 1, 300, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10 days', 15, 'Kelp', 'Nutrition', 3, 1, 1, 300, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10 days', 15, 'EcoCarb Plus', 'DM', 'DM risk', 2, 0.4, 1, 500, 'October');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10 days', 15, 'Horti oil', 'DM', 'DM risk', 1.25, 0.25, 1, 500, 'October');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Pre-flowering', 19, 'Sulphur', 'PM, Mites', 2.5, 0.5, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Pre-flowering', 19, 'Copper', 'DM', 1.25, .25, 1, 500, 'Novmeber');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Pre-flowering', 19, 'Kelp', 'Nutrition', 4, 0.8, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Pre-flowering', 19, 'Nutrient', 'Organic Trace Elements', 0.5, 0.1, 1, 500, 'November');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Sulphur', 'PM, Mites', 3.75, 0.5, 1.5, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Copper', 'DM', 1.875, .25, 1.5, 500, 'Novmeber');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Kelp', 'Nutrition', 4, 0.8, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Nutrient', 'Organic Trace Elements', 0.5, 0.1, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Ecoprotector', 'Botrytis', 10, 2, 1, 500, 'November');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Sulphur', 'PM, Mites', 3.75, 0.5, 1.5, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Copper', 'DM', 1.875, .25, 1.5, 500, 'Novmeber');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Kelp', 'Nutrition', 4, 0.8, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Nutrient', 'Organic Trace Elements', 0.5, 0.1, 1, 500, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Flowering', 25, 'Ecoprotector', 'Botrytis', 10, 2, 1, 500, 'November');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 29, 'Sulphur', 'PM', 4.5, 0.5, 1.5, 600, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 29, 'Copper', 'DM', 2.25, 0.25, 1.5, 600, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 29, 'Kelp', 'Nutrtion', 6, 1, 1, 600, 'November');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 29, 'Ecoprotector', 'adjuvant', 1.5, 0.25, 1, 600, 'November');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Approx_Timing) VALUES ('Post-Flowering', 29, 'Antagonist', 'Botrytis', 'if dirty flowering use Serenade Opti or Botector', 'December');
INSERT INTO spray_program (Vine_Stage, E_L, Product, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 29, 'EcoCarb Plus', 'if DM risk', 2, 0.4, 1, 500, 'December');
INSERT INTO spray_program (Vine_Stage, E_L, Product, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Post-Flowering', 32, 'Horti Oil', 'if DM risk', 1.25, 0.25, 1, 500, 'December');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10-14 days', 30, 'Sulphur', 'PM', 4.5, 0.5, 1.5, 600, 'December');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10-14 days', 30, 'Copper', 'DM', 2.25, 0.25, 1.5, 600, 'December');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Bunch Closure', 32, 'Sulphur', 'PM', 4.5, 0.5, 1.5, 600, 'December');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('Bunch Closure', 32, 'Copper', 'DM', 2.25, 0.25, 1.5, 600, 'December');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Approx_Timing) VALUES ('Bunch Closure', 32, 'Antagonist', 'Botrytis', 'if dirty flowering use Serenade Opti or Botector', 'December');

INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Notes, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10-14 days', 32, 'Sulphur', 'PM', 'until WHP', 3.6, 0.4, 1.5, 600, 'January');
INSERT INTO spray_program (Vine_Stage, E_L, Product, PD_Target, Rate_per_Ha, Rate_per_100L, CF, Water_Rate, Approx_Timing) VALUES ('+10-14 days', 32, 'Copper', 'DM', 2.25, 0.25, 1.5, 600, 'January');

CREATE TABLE vineyard (
    id SERIAL PRIMARY KEY,
    owner_email TEXT,
    vineyard_site TEXT,
	vineyard_size INTEGER,
    varieties TEXT,
	elevation INTEGER,
    orientation TEXT,
    E_L_Stage INTEGER
);

INSERT INTO vineyard (owner_email, vineyard_site, vineyard_size, varieties, elevation, orientation, E_L_Stage) VALUES ('lucy@example.com', 'Maffra', 3, 'Chardonnay, Pinot Noir', 400, 'North-West', 0);