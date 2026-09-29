CREATE TABLE [ctrl].[audit_log] (
    [audit_id]          BIGINT        NULL,
    [adf_run_id]        VARCHAR (100) NOT NULL,
    [table_id]          INT           NOT NULL,
    [stage]             VARCHAR (20)  NOT NULL,
    [status]            VARCHAR (20)  NOT NULL,
    [records_written]   INT           NULL,
    [start_time]        DATETIME2 (0) NULL,
    [end_time]          DATETIME2 (0) NULL,
    [created_timestamp] DATETIME2 (0) NOT NULL
);


GO