DROP VIEW IF EXISTS public.wordtype_per_ressort;

CREATE VIEW public.wordtype_per_ressort AS 

select  t."ressort", c."wordType", AVG(c.count) as avg
from content_analysis as c
join tagesschau as t
on c."tagesschauId" = t.id
group by t."ressort", c."wordType"
order by ressort, avg desc