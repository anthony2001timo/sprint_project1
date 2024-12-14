
WITH order_amount_per_day AS (
    SELECT
        DATE(order_purchase_timestamp) AS order_date,
        COUNT(*) AS order_count
    FROM
        olist_orders
    GROUP BY
        DATE(order_purchase_timestamp)
)


SELECT
    oad.order_date,
    oad.order_count,
    ph.date AS holiday_date
FROM
    order_amount_per_day oad
LEFT JOIN
    public_holidays ph
ON
    DATE(oad.order_date) = DATE(ph.date)
ORDER BY
    oad.order_date;
