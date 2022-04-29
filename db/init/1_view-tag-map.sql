CREATE VIEW TagMap AS SELECT a.tag AS tag1,
    b.tag AS tag2,
    news.ressort,
    count(*) AS count
FROM tags a
    CROSS JOIN tags b
    JOIN news ON news.id = a."newsId"
WHERE a."newsId" = b."newsId" AND a.tag <> b.tag AND news.date > '2021-04-01 00:00:00'::timestamp without time zone AND news."crawlType" = 'insert'::text
GROUP BY a.tag, b.tag, news.ressort
ORDER BY (count(*)) DESC;