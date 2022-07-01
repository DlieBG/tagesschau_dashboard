DROP VIEW IF EXISTS public.hod_tagesschau;

CREATE VIEW public.hod_tagesschau AS 

with hods as (
	select 
		extract(hour from date) as hod,
		"crawlerCrawlType"
	from tagesschau
)
select 
	hods.hod,
	hods."crawlerCrawlType",
	count(*),
	count(*) / (
		select count(*)
		from tagesschau as sub
		where hods."crawlerCrawlType" = sub."crawlerCrawlType"
	)::float as percent
from hods
group by hods.hod, hods."crawlerCrawlType"
order by hods.hod;


DROP VIEW IF EXISTS public.hod_news;

CREATE VIEW public.hod_news AS 

with hods as (
	select extract(hour from "publishedAt") as hod
	from news
)
select 
	hods.hod,
	count(*),
	count(*) / (
		select count(*)
		from news
	):: float as percent
from hods
group by hods.hod
order by hods.hod;
