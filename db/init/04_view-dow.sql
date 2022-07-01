DROP VIEW IF EXISTS public.dow_tagesschau;

CREATE VIEW public.dow_tagesschau AS 

with dows as (
	select 
		extract(isodow from date) as dow,
		"crawlerCrawlType"
	from tagesschau
)
select 
	dows.dow,
	dows."crawlerCrawlType",
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
		where dows."crawlerCrawlType" = sub."crawlerCrawlType"
	)::float as percent
from dows
group by dows.dow, weekday, dows."crawlerCrawlType"
order by dows.dow;


DROP VIEW IF EXISTS public.dow_news;

CREATE VIEW public.dow_news AS 

with dows as (
	select extract(isodow from "publishedAt") as dow
	from news
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
		from news
	):: float as percent
from dows
group by dows.dow, weekday
order by dows.dow;
