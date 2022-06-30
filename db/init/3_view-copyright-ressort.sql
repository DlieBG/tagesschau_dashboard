DROP VIEW IF EXISTS public.copyright_ressort;

CREATE VIEW public.copyright_ressort AS 

select 
    c.*,
    t.ressort
from clean_copyright as c
left join tagesschau as t
	on t.id = c."tagesschauId";
