DROP VIEW IF EXISTS public.tag_date;

CREATE VIEW public.tag_date AS 

select 
	tags.*,
	t."crawlerCrawlTime",
	1 as factor
from clean_tags as tags
left join tagesschau as t
	on tags."tagesschauId" = t.id
where t."crawlerCrawlType" = 'insert'

union

select 
	tags.*,
	t."crawlerCrawlTime",
	.25 as factor
from clean_tags as tags
left join tagesschau as t
	on tags."tagesschauId" = t.id
where t."crawlerCrawlType" = 'update';
