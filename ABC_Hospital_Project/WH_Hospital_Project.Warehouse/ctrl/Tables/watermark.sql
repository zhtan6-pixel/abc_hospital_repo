CREATE TABLE [ctrl].[watermark] (
    [table_id]               INT           NOT NULL,
    [watermark_value]        VARCHAR (200) NULL,
    [last_updated_timestamp] DATETIME2 (0) NOT NULL
);


GO