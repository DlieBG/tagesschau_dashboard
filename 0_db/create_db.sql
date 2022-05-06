-- Table: public.tagesschau

-- DROP TABLE IF EXISTS public.tagesschau;

CREATE TABLE IF NOT EXISTS public.tagesschau
(
    "id" serial NOT NULL,
    "sophoraId" text COLLATE pg_catalog."default" NOT NULL,
    "externalId" text COLLATE pg_catalog."default" NOT NULL,
    "title" text COLLATE pg_catalog."default" NOT NULL,
    "teaserImageTitle" text COLLATE pg_catalog."default",
    "teaserImageCopyright" text COLLATE pg_catalog."default",
    "teaserImageAlttext" text COLLATE pg_catalog."default",
    "teaserImageType" text COLLATE pg_catalog."default",
    "date" timestamp NOT NULL,
    "trackingSid" text COLLATE pg_catalog."default",
    "trackingSrc" text COLLATE pg_catalog."default",
    "trackingCtp" text COLLATE pg_catalog."default",
    "trackingPdt" text COLLATE pg_catalog."default",
    "trackingOtp" text COLLATE pg_catalog."default",
    "trackingCid" text COLLATE pg_catalog."default",
    "trackingPti" text COLLATE pg_catalog."default",
    "trackingType" text COLLATE pg_catalog."default",
    "updateCheckUrl" text COLLATE pg_catalog."default" NOT NULL,
    "regionId" bigint NOT NULL,
    "imageTitle" text COLLATE pg_catalog."default",
    "imageCopyright" text COLLATE pg_catalog."default",
    "imageAlttext" text COLLATE pg_catalog."default",
    "imageType" text COLLATE pg_catalog."default",
    "details" text COLLATE pg_catalog."default" NOT NULL,
    "detailsweb" text COLLATE pg_catalog."default" NOT NULL,
    "shareUrl" text COLLATE pg_catalog."default" NOT NULL,
    "topline" text COLLATE pg_catalog."default" NOT NULL,
    "firstSentence" text COLLATE pg_catalog."default" NOT NULL,
    "ressort" text COLLATE pg_catalog."default" NOT NULL,
    "type" text COLLATE pg_catalog."default" NOT NULL,
    "breakingNews" boolean NOT NULL,
    "crawlerInsertTime" timestamp NOT NULL,
    "crawlerCrawlTime" timestamp NOT NULL,
    "crawlerCrawlType" text COLLATE pg_catalog."default" NOT NULL,
    "crawlerContentUpdate" boolean NOT NULL,
    "crawlerFrontepageIndex" bigint NOT NULL,
    "crawlerFrontpageStatus" text COLLATE pg_catalog."default" NOT NULL,
    "crawlerAllIndex" bigint NOT NULL,
    "crawlerAllStatus" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tagesschau_pkey PRIMARY KEY (id),
    CONSTRAINT tagesschau_id_key UNIQUE (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tagesschau
    OWNER to postgres;


-- Table: public.content

-- DROP TABLE IF EXISTS public.content;

CREATE TABLE IF NOT EXISTS public.content
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "type" text COLLATE pg_catalog."default" NOT NULL,
    "value" text COLLATE pg_catalog."default" NOT NULL,
    "boxTitle" text COLLATE pg_catalog."default" NOT NULL,
    "boxSubtitle" text COLLATE pg_catalog."default" NOT NULL,
    "boxText" text COLLATE pg_catalog."default" NOT NULL,
    "boxLink" text COLLATE pg_catalog."default" NOT NULL,
    "boxSource" text COLLATE pg_catalog."default" NOT NULL,
    "videoSophoraId" text COLLATE pg_catalog."default" NOT NULL,
    "videoExternalId" text COLLATE pg_catalog."default" NOT NULL,
    "videoTitle" text COLLATE pg_catalog."default" NOT NULL,
    "videoDate" timestamp NOT NULL,
    "videoUpdateCheckUrl" text COLLATE pg_catalog."default" NOT NULL,
    "videoCopyright" text COLLATE pg_catalog."default" NOT NULL,
    "videoType" text COLLATE pg_catalog."default" NOT NULL,
    "videoAlttext" text COLLATE pg_catalog."default" NOT NULL,
    "quotationText" text COLLATE pg_catalog."default" NOT NULL,
    "webviewInline" text COLLATE pg_catalog."default" NOT NULL,
    "htmlEmbedService" text COLLATE pg_catalog."default" NOT NULL,
    "htmlEmbedUrl" text COLLATE pg_catalog."default" NOT NULL,
    "audioDate" timestamp NOT NULL,
    "audioTeaserImageTitle" text COLLATE pg_catalog."default" NOT NULL,
    "audioTeaserImageCopyright" text COLLATE pg_catalog."default" NOT NULL,
    "audioTeaserImageAlttext" text COLLATE pg_catalog."default" NOT NULL,
    "audioTeaserImageType" text COLLATE pg_catalog."default" NOT NULL,
    "audioTitle" text COLLATE pg_catalog."default" NOT NULL,
    "audioText" text COLLATE pg_catalog."default" NOT NULL,
    "socialTitle" text COLLATE pg_catalog."default" NOT NULL,
    "socialAccount" text COLLATE pg_catalog."default" NOT NULL,
    "socialUsername" text COLLATE pg_catalog."default" NOT NULL,
    "socialAvatar" text COLLATE pg_catalog."default" NOT NULL,
    "socialUrl" text COLLATE pg_catalog."default" NOT NULL,
    "socialShorttext" text COLLATE pg_catalog."default" NOT NULL,
    "socialDate" timestamp NOT NULL,
    "index" bigint NOT NULL,
    CONSTRAINT content_pkey PRIMARY KEY (id),
    CONSTRAINT "content_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.content
    OWNER to postgres;


-- Table: public.geotags

-- DROP TABLE IF EXISTS public.geotags;

CREATE TABLE IF NOT EXISTS public.geotags
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "tag" text COLLATE pg_catalog."default" NOT NULL,
    "index" bigint NOT NULL,
    CONSTRAINT geotags_pkey PRIMARY KEY (id),
    CONSTRAINT "geotags_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.geotags
    OWNER to postgres;


-- Table: public.tags

-- DROP TABLE IF EXISTS public.tags;

CREATE TABLE IF NOT EXISTS public.tags
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "tag" text COLLATE pg_catalog."default" NOT NULL,
    "index" bigint NOT NULL,
    CONSTRAINT tags_pkey PRIMARY KEY (id),
    CONSTRAINT "tags_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tags
    OWNER to postgres;


-- Table: public.source

-- DROP TABLE IF EXISTS public.source;

CREATE TABLE IF NOT EXISTS public.source
(
    "id" text COLLATE pg_catalog."default" NOT NULL,
    "name" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT source_pkey PRIMARY KEY (id),
    CONSTRAINT source_id_key UNIQUE (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.source
    OWNER to postgres;


-- Table: public.news

-- DROP TABLE IF EXISTS public.news;

CREATE TABLE IF NOT EXISTS public.news
(
    "id" serial NOT NULL,
    "sourceId" text COLLATE pg_catalog."default" NOT NULL,
    "author" text COLLATE pg_catalog."default",
    "title" text COLLATE pg_catalog."default" NOT NULL,
    "description" text COLLATE pg_catalog."default" NOT NULL,
    "url" text COLLATE pg_catalog."default" NOT NULL,
    "urlToImage" text COLLATE pg_catalog."default",
    "publishedAt" timestamp NOT NULL,
    "content" text COLLATE pg_catalog."default",
    CONSTRAINT news_pkey PRIMARY KEY (id),
    CONSTRAINT "news_sourceId_fkey" FOREIGN KEY ("sourceId")
        REFERENCES public.source (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.news
    OWNER to postgres;


CREATE INDEX ON content("tagesschauId");
CREATE INDEX ON geotags("tagesschauId");
CREATE INDEX ON tags("tagesschauId");
CREATE INDEX ON news("sourceId");
