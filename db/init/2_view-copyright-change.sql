DROP VIEW IF EXISTS public.copyright;

CREATE VIEW public.copyright AS 

select 
	t."id",
	t."regionId",
	"teaserImageCopyright",
	(
		select c."imageCopyright"
		from tagesschau as sub 
		left join clean_copyright as c
			on c."tagesschauId" = t."id"
		where 
			sub."externalId" = t."externalId" and
			sub."crawlerCrawlTime" < t."crawlerCrawlTime"
		order by "crawlerCrawlTime" desc
		limit 1
	) as "previousImageCopyright"
from tagesschau as t
left join clean_copyright as c
	on c."tagesschauId" = t."id"
where 
	t."teaserImageCopyright" is not null and
	t."crawlerCrawlType" = 'update' and
	(
		select c."imageCopyright"
		from tagesschau as sub 
		left join clean_copyright as c
			on c."tagesschauId" = t."id"
		where 
			sub."externalId" = t."externalId" and
			sub."crawlerCrawlTime" < t."crawlerCrawlTime"
		order by "crawlerCrawlTime" desc
		limit 1
	) != c."imageCopyright";
