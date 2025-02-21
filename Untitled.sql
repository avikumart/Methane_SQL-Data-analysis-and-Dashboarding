select*from methane_table;

-- create a view from methane_table
create view algeria_emissions as
select*from methane_table
where country = 'algeria';

-- emissions of India
create view india_emissions as
select*from methane_table
where country = 'India';

select*from india_emissions;

select*from methane_table
where baseyear = '2022';

-- groupby query
select region, avg(emissions) as avg_emissions 
from methane_table
group by region;

-- find the avg, min and max emisssions from eu and ap only. 
select region, avg(emissions) as avg_emissions, min(emissions) as min_emission, max(emissions) as max_emission
from methane_table
where region in ('Asia Pacific','Europe')
group by region;

select region, count(*) as count_of_rows
from methane_table
group by region
order by count_of_rows asc
limit 5
offset 4;

-- find the count of rows of africa and europe
select region, count(*) as count_of_rows
from methane_table
group by region
having region in ('Europe','Africa');

select region, count(*) as count_of_rows
from methane_table
where region in ('Europe','Africa')
group by region;

-- Find the average emissions by each country that is located in africa
select country, avg(emissions)
from methane_table
where region = 'Africa'
group by country;

-- find the average emissions froF each segment from india
select segment, avg(emissions)
from methane_table
where country = 'India'
group by segment;

