DROP VIEW IF EXISTS public.regions;

CREATE VIEW public.regions AS 

select 
	r."regionId", 
	r."regionName", 
	r."regionIsoCode",
	r."regionResidents", 
	r."broadcasterName", 
	r."broadcasterNameShorthand", 
	r."broadcasterRevenue", 
	r."broadcasterEmployees", 
	r."broadcasterResidents",
	count(*),
	count(*) / r."broadcasterResidents"::float as article_per_resident,
	count(*) / r."broadcasterEmployees"::float as article_per_employee,
	r."broadcasterRevenue" / count(*)::float as euro_per_article,
	r."broadcasterResidents" / r."broadcasterEmployees"::float as resident_per_employee
from clean_regions as r
left join tagesschau as t
	on t.id = r."tagesschauId"
where 
	t."crawlerCrawlType" = 'insert' and
	r."regionId" > 0
group by
	r."regionId", 
	r."regionName", 
	r."regionIsoCode",
	r."regionResidents", 
	r."broadcasterName", 
	r."broadcasterNameShorthand", 
	r."broadcasterRevenue", 
	r."broadcasterEmployees", 
	r."broadcasterResidents"
order by r."regionId";
