-- Table: public.news

DROP TABLE IF EXISTS public.news;

CREATE TABLE IF NOT EXISTS public.news
(
    id serial NOT NULL,
    "sophoraId" text COLLATE pg_catalog."default" NOT NULL,
    "externalId" text COLLATE pg_catalog."default" NOT NULL,
    title text COLLATE pg_catalog."default" NOT NULL,
    "teaserImageTitle" text COLLATE pg_catalog."default",
    "teaserImageCopyright" text COLLATE pg_catalog."default",
    "teaserImageAlttext" text COLLATE pg_catalog."default",
    "teaserImageType" text COLLATE pg_catalog."default",
    date timestamp NOT NULL,
    "updateCheckUrl" text COLLATE pg_catalog."default" NOT NULL,
    "regionId" bigint NOT NULL,
    details text COLLATE pg_catalog."default" NOT NULL,
    "detailsweb" text COLLATE pg_catalog."default" NOT NULL,
    topline text COLLATE pg_catalog."default" NOT NULL,
    "firstSentence" text COLLATE pg_catalog."default" NOT NULL,
    ressort text COLLATE pg_catalog."default" NOT NULL,
    type text COLLATE pg_catalog."default" NOT NULL,
    "breakingNews" boolean NOT NULL,
    index bigint NOT NULL,
    "insertTime" timestamp NOT NULL,
    "crawlTime" timestamp NOT NULL,
    "crawlType" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT news_pkey PRIMARY KEY (id),
    CONSTRAINT news_id_key UNIQUE (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.news
    OWNER to tagesschau;


-- Table: public.content

DROP TABLE IF EXISTS public.content;

CREATE TABLE IF NOT EXISTS public.content
(
    id serial NOT NULL,
    "newsId" integer NOT NULL,
    value text COLLATE pg_catalog."default" NOT NULL,
    type text COLLATE pg_catalog."default" NOT NULL,
    index bigint NOT NULL,
    CONSTRAINT content_pkey PRIMARY KEY (id),
    CONSTRAINT "content_newsId_fkey" FOREIGN KEY ("newsId")
        REFERENCES public.news (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.content
    OWNER to tagesschau;


-- Table: public.geotags

DROP TABLE IF EXISTS public.geotags;

CREATE TABLE IF NOT EXISTS public.geotags
(
    id serial NOT NULL,
    "newsId" integer NOT NULL,
    tag text COLLATE pg_catalog."default" NOT NULL,
    index bigint NOT NULL,
    CONSTRAINT geotags_pkey PRIMARY KEY (id),
    CONSTRAINT "geotags_newsId_fkey" FOREIGN KEY ("newsId")
        REFERENCES public.news (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.geotags
    OWNER to tagesschau;


-- Table: public.tags

DROP TABLE IF EXISTS public.tags;

CREATE TABLE IF NOT EXISTS public.tags
(
    id serial NOT NULL,
    "newsId" integer NOT NULL,
    tag text COLLATE pg_catalog."default" NOT NULL,
    index bigint NOT NULL,
    CONSTRAINT tags_pkey PRIMARY KEY (id),
    CONSTRAINT "tags_newsId_fkey" FOREIGN KEY ("newsId")
        REFERENCES public.news (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tags
    OWNER to tagesschau;


CREATE index ON content("newsId");
CREATE index ON geotags("newsId");
CREATE index ON tags("newsId");
