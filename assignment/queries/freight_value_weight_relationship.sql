SELECT 
    p.product_weight_g,
    oi.freight_value
FROM 
    olist_order_items oi
JOIN 
    olist_products p
ON 
    oi.product_id = p.product_id
WHERE 
    p.product_weight_g IS NOT NULL 
    AND oi.freight_value IS NOT NULL;
