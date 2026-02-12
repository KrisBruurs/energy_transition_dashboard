DROP TABLE IF EXISTS co2_countries;

CREATE TABLE co2_countries AS
SELECT *
FROM co2_raw
WHERE ISO_code IS NOT NULL
    OR ISO_code != '';