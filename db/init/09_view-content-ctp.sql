DROP VIEW IF EXISTS public.content_ctp;

CREATE VIEW public.content_ctp AS 

select 
	c.*,
	t."trackingCtp",
	case
		when c.type = 'box' then 'Box'
		when c.type = 'headline' then 'Überschrift'
		when c.type = 'htmlEmbed' then 'HTML'
		when c.type = 'image_gallery' then 'Fotos'
		when c.type = 'text' then 'Text'
	else ''
	end as clean_type
from content as c
inner join tagesschau as t
on
	c."tagesschauId" = t.id;
