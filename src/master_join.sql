DROP TABLE IF EXISTS master;

CREATE TABLE master AS
SELECT
    e.country,
    e.ISO_code,
    e.year,
    e.primary_energy_consumption,
    e.energy_per_capita,
    e.electricity_demand,
    e.renewables_share_energy,
    e.fossil_share_energy,
    e.solar_share_elec,
    e.wind_share_elec,
    c.co2,
    c.co2_per_capita,
    g."GDP per capita" AS gdp_per_capita

FROM energy_countries AS e
INNER JOIN co2_countries AS c
    ON e.year = c.year
    AND e.iso_code = c.iso_code
LEFT JOIN gdp_countries AS g
    ON e.year = g.year
    AND e.iso_code = g.code;
