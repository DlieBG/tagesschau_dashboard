DROP VIEW IF EXISTS public.copyright_ressort;

CREATE VIEW public.copyright_ressort AS 

select 
    c.*,
    t.ressort
from clean_copyright as c
left join tagesschau as t
	on t.id = c."tagesschauId"
where 
	t.ressort is not null and
	t.ressort != 'investigativ' and
	t."crawlerCrawlType" = 'insert'
	
union 

select 
    c.*,
	case 
		when c."imageCopyright" = 'dpa' then 'inland'
		when c."imageCopyright" = 'picture alliance' then 'ausland'
		when c."imageCopyright" = 'IMAGO' then 'inland'
		when c."imageCopyright" = 'Associated Press' then 'ausland'
		when c."imageCopyright" = 'Reuters' then 'ausland'
		when c."imageCopyright" = 'Agence France-Presse' then 'ausland'
		when c."imageCopyright" = 'Freie Journalisten' then 'ausland'
		when c."imageCopyright" = 'Getty Images' then 'sport'
		when c."imageCopyright" = 'ARD' then 'inland'
	else 'other'
	end as ressort
from clean_copyright as c
left join tagesschau as t
	on t.id = c."tagesschauId"
where 
	t.ressort is null and
	t."crawlerCrawlType" = 'insert';
