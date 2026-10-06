CREATE TABLE [ctrl].[audit_log_copy] (
    [adf_run_id]        VARCHAR (MAX)    NULL,
    [table_id]          INT              NULL,
    [stage]             VARCHAR (MAX)    NULL,
    [status]            VARCHAR (MAX)    NULL,
    [records_written]   INT              NULL,
    [start_time]        DATETIME2 (6)    NULL,
    [end_time]          DATETIME2 (6)    NULL,
    [created_timestamp] DATETIME2 (6)    NULL,
    [audit_id]          UNIQUEIDENTIFIER NULL
);


GO