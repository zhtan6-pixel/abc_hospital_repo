CREATE TABLE [abc].[patients] (
    [patient_id]             BIGINT        NOT NULL,
    [first_name]             VARCHAR (100) NOT NULL,
    [last_name]              VARCHAR (100) NOT NULL,
    [date_of_birth]          DATE          NULL,
    [gender]                 VARCHAR (10)  NULL,
    [city]                   VARCHAR (100) NULL,
    [state]                  VARCHAR (50)  NULL,
    [registered_hospital_id] INT           NULL,
    [insurance_provider_id]  INT           NULL,
    [created_at]             DATETIME2 (0) NOT NULL,
    [updated_at]             DATETIME2 (0) NOT NULL
);


GO