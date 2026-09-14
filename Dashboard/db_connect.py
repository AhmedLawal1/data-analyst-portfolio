#Connect to the SQL Server database and retrieve sales data into a pandas DataFrame

import pandas as pd
import pyodbc

def get_sales_data():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=;" #Sever name
        "DATABASE=;"   #Database name
        "UID=;"      #User ID
        "PWD=;"      #Password
        "TrustServerCertificate=yes;" #Trust Server Certificate
    )

#SQL Query (with Joins and Filters) to retrieve sales data from the database

    query = """
        SELECT
        s.DESPDATE_ITM AS [DATE],
        c.REPRESENT AS SALESREP,
        s.CUSTOMER_ITM AS CUSTOMER,
        s.PRODGROUP_ITM AS PRODGROUP,
        s.PARTNO_SORD AS PRODUCT,
        s.SORDQTY AS QTY,

        s.SORDQTY * (s.SELLPRICE / s.CURRATE_ITM) AS ORDERVAL,

        s.SORDQTY * pc.MATCOST_LOT AS ORDERCOST,

        (s.SORDQTY * (s.SELLPRICE / s.CURRATE_ITM)) - (s.SORDQTY * pc.MATCOST_LOT) AS MARGIN

    FROM dbo.MBG140 s

    INNER JOIN dbo.MBG110 c
        ON s.ACCOUNT15_ITM = c.ACCOUNT15_CUS
        AND s.CUSTOMER_ITM = c.CUSTOMER

    OUTER APPLY
    (
        SELECT TOP 1
            m.LOTDTE,
            m.MATCOST_LOT
        FROM dbo.MBC300 m
        WHERE s.ACCOUNT15_ITM = m.ACCOUNT15_LOT
        AND s.PARTNO_SORD = m.PARTNO_LOT
        AND CAST(m.LOTDTE AS date) <= CAST(s.DESPDATE_ITM AS date)
        ORDER BY 
            CAST(m.LOTDTE AS date) DESC,
            m.LOTDTE DESC
    ) pc

    WHERE s.DESPDATE_ITM IS NOT NULL
    AND s.DESPDATE_ITM >= '2021-01-01' -- Leave start date the same, as it is when accurate data collection began --
    AND s.DESPDATE_ITM <  '2026-09-01' -- Change the end date to the begining of the new month --
    """

    df = pd.read_sql(query, conn) # Read the SQL query results into a pandas DataFrame

    conn.close()

    return df
