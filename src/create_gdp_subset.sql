DROP TABLE IF EXISTS gdp_countries;

CREATE TABLE gdp_countries AS
SELECT *
FROM gdp_raw
GROUP BY code, year;
