select*from methen_table;

-- Alter table name to correct name of the table
ALTER TABLE methen_table
RENAME TO methane_table;

select*from methane_table;

-- modify notes column datatype
alter table methane_table
ALTER column notes type integer USING (NULLIF(notes, '')::integer); 

-- Analyze the methane emissions data
select region, country, avg(emissions) as average_emissions
from methane_table
group by region, country
Having country in ('India','China');


-- What are the top10 country with most emissions
select country, sum(emissions) as total_emissions
from methane_table
group by country
order by total_emissions DESC
limit 10;

-- what are the types of emissions source in the dataset and which is highest?
select type, count(*)
from methane_table
group by type
order by count(*) DESC;

-- what are the top segment of emissions
select segment, sum(emissions) as total_emisssions, avg(emissions) as ave_emissions
from methane_table
group by segment
order by 2 desc, 3 desc
limit 10;

-- find out the reasons of emissions by each region
select distinct reason, region
from methane_table
order by region desc;




