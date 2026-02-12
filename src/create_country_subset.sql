CREATE TABLE energy_countries AS
SELECT * 
FROM energy_raw
WHERE ISO_code IS NOT NULL
    AND ISO_code != ''