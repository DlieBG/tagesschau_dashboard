DROP VIEW IF EXISTS public.content_ctp;

CREATE VIEW public.content_ctp AS 

select 
	c.*,
	t."trackingCtp"
from content as c
inner join tagesschau as t
on
	c."tagesschauId" = t.id;
