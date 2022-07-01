DROP VIEW IF EXISTS public.tag_map;

CREATE VIEW public.tag_map AS SELECT a.tag AS tag1,
    b.tag AS tag2,
    tagesschau.ressort,
    count(*) AS count
FROM clean_tags a
    CROSS JOIN clean_tags b
    JOIN tagesschau ON tagesschau.id = a."tagesschauId"
WHERE a."tagesschauId" = b."tagesschauId" AND a.tag <> b.tag AND tagesschau."crawlerCrawlType" = 'insert'
GROUP BY a.tag, b.tag, tagesschau."ressort"
ORDER BY (count(*)) DESC;
