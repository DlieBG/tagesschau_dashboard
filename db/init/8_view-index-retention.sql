DROP VIEW IF EXISTS public.index_retention;

CREATE MATERIALIZED VIEW public.index_retention AS 

select
	m.index,
	max(m.retention) as max_retention,
	min(m.retention) as min_retention,
	avg(m.retention) as avg_retention,
	extract('epoch' from avg(m.retention)) / 60 as avg_retention_minutes,
	max(m."max_new_index") as "max_new_index",
	min(nullif(m."min_new_index", -1)) as "min_new_index",
	avg(m."avg_new_index")::int as "avg_new_index"
from (
	select 
		t."externalId" as "externalId",
		t."crawlerFrontpageIndex" as index,
		sum(sub."crawlerCrawlTime" - t."crawlerCrawlTime") as retention,
		max(sub."crawlerFrontpageIndex") as "max_new_index",
		min(nullif(sub."crawlerFrontpageIndex", -1)) as "min_new_index",
		avg(sub."crawlerFrontpageIndex")::int as "avg_new_index"
	from (
		select *
		from tagesschau
		--where
			--"crawlerFrontpageIndex" != -1
	) as t
	inner join lateral (
		select *
		from tagesschau as j
		where 
			t."crawlerFrontpageIndex" != j."crawlerFrontpageIndex" and
			t."externalId" = j."externalId" and
			t."crawlerCrawlTime" < j."crawlerCrawlTime"
		order by j."crawlerCrawlTime" asc
		limit 1
	) as sub on true
	group by t."externalId", index
) as m
group by m.index
order by m.index;
