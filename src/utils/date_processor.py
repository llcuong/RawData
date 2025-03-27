from src.loader.database import gd_vnedc_database


def get_this_week_info():
    sql = f"""
        SELECT *
        FROM [MES_OLAP].[dbo].[week_date]
        WHERE CAST(GETDATE() AS DATE) BETWEEN start_date AND end_date """
    result = gd_vnedc_database().select_sql_dict(sql)
    if result:
        return result[0]
    else:
        return []

def get_last_week_info():
    sql = f"""
        SELECT TOP 1 *
        FROM [MES_OLAP].[dbo].[week_date]
        WHERE 
            (year < (
                SELECT year 
                FROM [MES_OLAP].[dbo].[week_date]
                WHERE CAST(GETDATE() AS DATE) BETWEEN start_date AND end_date
            ))
            OR (
                year = (
                    SELECT year 
                    FROM [MES_OLAP].[dbo].[week_date]
                    WHERE CAST(GETDATE() AS DATE) BETWEEN start_date AND end_date
                )
                AND week_no < (
                    SELECT week_no 
                    FROM [MES_OLAP].[dbo].[week_date]
                    WHERE CAST(GETDATE() AS DATE) BETWEEN start_date AND end_date
                )
            )
        ORDER BY year DESC, week_no DESC"""
    result = gd_vnedc_database().select_sql_dict(sql)
    if result:
        return result[0]
    else:
        return []

