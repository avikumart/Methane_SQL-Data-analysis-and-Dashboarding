CREATE TABLE methen_table (
region varchar(255),
country varchar(255),
emissions float,
type varchar(255),
segment varchar(255),
reason varchar(255),
baseYear varchar(255),
notes varchar(255)
);

select*from methen_table;

select region, country, emissions
from methen_table
where emissions > (select AVG(emissions) from methen_table);

select region, country, avg(emissions) AS avg_emissions
from methen_table
GROUP BY region, country
ORDER BY avg_emissions desc;


