CREATE TABLE [abc].[doctors] (
    [doctor_id]    BIGINT        NOT NULL,
    [first_name]   VARCHAR (100) NOT NULL,
    [last_name]    VARCHAR (100) NOT NULL,
    [specialty]    VARCHAR (100) NULL,
    [hospital_id]  INT           NULL,
    [phone_number] VARCHAR (20)  NULL,
    [created_at]   DATETIME2 (0) NOT NULL,
    [updated_at]   DATETIME2 (0) NOT NULL
);


GO