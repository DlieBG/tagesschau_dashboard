DROP TABLE IF EXISTS public.content;
DROP TABLE IF EXISTS public.geotags;
DROP TABLE IF EXISTS public.tags;
DROP TABLE IF EXISTS public.clean_tags;
DROP TABLE IF EXISTS public.clean_regions;
DROP TABLE IF EXISTS public.tagesschau;

DROP TABLE IF EXISTS public.news;
DROP TABLE IF EXISTS public.source;


-- Table: public.tagesschau

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
    "ressort" text COLLATE pg_catalog."default",
    "type" text COLLATE pg_catalog."default" NOT NULL,
    "breakingNews" boolean NOT NULL,
    "crawlerInsertTime" timestamp NOT NULL,
    "crawlerCrawlTime" timestamp NOT NULL,
    "crawlerCrawlType" text COLLATE pg_catalog."default" NOT NULL,
    "crawlerContentUpdate" boolean,
    "crawlerFrontpageIndex" bigint NOT NULL,
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

CREATE TABLE IF NOT EXISTS public.content
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "type" text COLLATE pg_catalog."default" NOT NULL,
    "value" text COLLATE pg_catalog."default",
    "boxTitle" text COLLATE pg_catalog."default",
    "boxSubtitle" text COLLATE pg_catalog."default",
    "boxText" text COLLATE pg_catalog."default",
    "boxLink" text COLLATE pg_catalog."default",
    "boxSource" text COLLATE pg_catalog."default",
    "videoSophoraId" text COLLATE pg_catalog."default",
    "videoExternalId" text COLLATE pg_catalog."default",
    "videoTitle" text COLLATE pg_catalog."default",
    "videoDate" timestamp,
    "videoUpdateCheckUrl" text COLLATE pg_catalog."default",
    "videoCopyright" text COLLATE pg_catalog."default",
    "videoType" text COLLATE pg_catalog."default",
    "videoAlttext" text COLLATE pg_catalog."default",
    "quotationText" text COLLATE pg_catalog."default",
    "webviewInline" text COLLATE pg_catalog."default",
    "htmlEmbedService" text COLLATE pg_catalog."default",
    "htmlEmbedUrl" text COLLATE pg_catalog."default",
    "audioDate" timestamp,
    "audioTeaserImageTitle" text COLLATE pg_catalog."default",
    "audioTeaserImageCopyright" text COLLATE pg_catalog."default",
    "audioTeaserImageAlttext" text COLLATE pg_catalog."default",
    "audioTeaserImageType" text COLLATE pg_catalog."default",
    "audioTitle" text COLLATE pg_catalog."default",
    "audioText" text COLLATE pg_catalog."default",
    "socialTitle" text COLLATE pg_catalog."default",
    "socialAccount" text COLLATE pg_catalog."default",
    "socialUsername" text COLLATE pg_catalog."default",
    "socialAvatar" text COLLATE pg_catalog."default",
    "socialUrl" text COLLATE pg_catalog."default",
    "socialShorttext" text COLLATE pg_catalog."default",
    "socialDate" timestamp,
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

-- Table: public.tags


CREATE TABLE IF NOT EXISTS public.clean_tags
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "tag" text COLLATE pg_catalog."default" NOT NULL,
    "index" bigint NOT NULL,
    CONSTRAINT clean_tags_pkey PRIMARY KEY (id),
    CONSTRAINT "clean_tags_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clean_tags
    OWNER to postgres;


-- Table: public.clean_regions

CREATE TABLE IF NOT EXISTS public.clean_regions
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "regionId" bigint NOT NULL,
    "regionName" text COLLATE pg_catalog."default" NOT NULL,
    "regionIsoCode" text COLLATE pg_catalog."default" NOT NULL,
    "date" timestamp NOT NULL,
    "regionResidents" integer NOT NULL,
    "broadcasterName" text COLLATE pg_catalog."default" NOT NULL,
    "broadcasterNameShorthand" text COLLATE pg_catalog."default" NOT NULL,
    "broadcasterRevenue" integer NOT NULL,
    "broadcasterEmployees" integer NOT NULL,
    "broadcasterResidents" integer NOT NULL,
    CONSTRAINT clean_regions_pkey PRIMARY KEY (id),
    CONSTRAINT "clean_regions_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clean_regions
    OWNER to postgres;


-- Table: public.clean_copyright

CREATE TABLE IF NOT EXISTS public.clean_copyright
(
    "id" serial NOT NULL,
    "tagesschauId" integer NOT NULL,
    "imageCopyright" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT clean_copyright_pkey PRIMARY KEY (id),
    CONSTRAINT "clean_copyright_tagesschauId_fkey" FOREIGN KEY ("tagesschauId")
        REFERENCES public.tagesschau (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clean_copyright
    OWNER to postgres;


-- Table: public.source

CREATE TABLE IF NOT EXISTS public.source
(
    "id" text COLLATE pg_catalog."default" NOT NULL,
    "name" text COLLATE pg_catalog."default" NOT NULL,
    "description" text COLLATE pg_catalog."default" NOT NULL,
    "url" text COLLATE pg_catalog."default" NOT NULL,
    "category" text COLLATE pg_catalog."default" NOT NULL,
    "language" text COLLATE pg_catalog."default" NOT NULL,
    "country" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT source_pkey PRIMARY KEY (id),
    CONSTRAINT source_id_key UNIQUE (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.source
    OWNER to postgres;


-- Table: public.news

CREATE TABLE IF NOT EXISTS public.news
(
    "id" serial NOT NULL,
    "sourceId" text COLLATE pg_catalog."default" NOT NULL,
    "author" text COLLATE pg_catalog."default",
    "title" text COLLATE pg_catalog."default",
    "description" text COLLATE pg_catalog."default",
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


CREATE INDEX ON tagesschau("externalId");
CREATE INDEX ON content("tagesschauId");
CREATE INDEX ON geotags("tagesschauId");
CREATE INDEX ON tags("tagesschauId");
CREATE INDEX ON clean_tags("tagesschauId");
CREATE INDEX ON clean_regions("tagesschauId");
CREATE INDEX ON clean_copyright("tagesschauId");
CREATE INDEX ON news("sourceId");
