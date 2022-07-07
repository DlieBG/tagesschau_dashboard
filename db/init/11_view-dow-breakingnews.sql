DROP VIEW IF EXISTS public.dow_breakingnews;

CREATE VIEW public.dow_breakingnews AS 

with dows as (
	select 
		extract(isodow from date) as dow
	from tagesschau
	where "breakingNews" = true and "crawlerCrawlType" = 'insert'
)
select 
	dows.dow,
	case
		when dows.dow = 1 then 'Montag'
		when dows.dow = 2 then 'Dienstag'
		when dows.dow = 3 then 'Mittwoch'
		when dows.dow = 4 then 'Donnerstag'
		when dows.dow = 5 then 'Freitag'
		when dows.dow = 6 then 'Samstag'
		when dows.dow = 7 then 'Sonntag'
	else ''
	end as weekday,
	count(*),
	count(*) / (
		select count(*)
		from tagesschau as sub
		where "breakingNews" = true and "crawlerCrawlType" = 'insert'
	)::float as percent
from dows
group by dows.dow, weekday
order by dows.dow;
