from .checks import (
    check_not_null,
    check_unique,
    check_accepted_values,
    check_non_negative,
    check_range
)


# ORDERS
ORDERS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "order_id"),
    lambda df: check_not_null(df, "customer_id"),

    # UNIQUENESS
    lambda df: check_unique(df, ["order_id"]),

    # VALIDITY
    lambda df: check_accepted_values(
        df,
        "order_status",
        [
            "delivered",
            "shipped",
            "canceled",
            "unavailable",
            "invoiced",
            "processing",
            "created",
            "approved"
        ]
    ),
]


# CUSTOMERS
CUSTOMERS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "customer_id"),
    lambda df: check_not_null(df, "customer_unique_id"),
    lambda df: check_not_null(df, "customer_state"),

    # UNIQUENESS
    lambda df: check_unique(df, ["customer_id"]),
]


# GEOLOCATION
GEOLOCATION_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "geolocation_zip_code_prefix"),
    lambda df: check_not_null(df, "geolocation_lat"),
    lambda df: check_not_null(df, "geolocation_lng"),

    # VALIDITY
    lambda df: check_range(df, "geolocation_lat", -90, 90),
    lambda df: check_range(df, "geolocation_lng", -180, 180),
]


# ORDER ITEMS
ORDER_ITEMS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "order_id"),
    lambda df: check_not_null(df, "product_id"),
    lambda df: check_not_null(df, "seller_id"),

    # UNIQUENESS
    lambda df: check_unique(
        df,
        ["order_id", "order_item_id"]
    ),

    # VALIDITY
    lambda df: check_non_negative(df, "price"),
    lambda df: check_non_negative(df, "freight_value"),
]


# PAYMENTS
ORDER_PAYMENTS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "order_id"),
    lambda df: check_not_null(df, "payment_type"),
    lambda df: check_not_null(df, "payment_value"),

    # VALIDITY
    lambda df: check_non_negative(df, "payment_value"),
]


# REVIEWS
ORDER_REVIEWS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "review_id"),
    lambda df: check_not_null(df, "order_id"),
    lambda df: check_not_null(df, "review_score"),

    # UNIQUENESS
    lambda df: check_unique(df,["review_id", "order_id"]),

    # VALIDITY
    lambda df: check_range(df, "review_score", 1, 5)
]


# PRODUCTS
PRODUCTS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "product_id"),

    # UNIQUENESS
    lambda df: check_unique(df, ["product_id"]),

    # VALIDITY
    lambda df: check_non_negative(df, "product_weight_g"),
    lambda df: check_non_negative(df, "product_length_cm"),
    lambda df: check_non_negative(df, "product_height_cm"),
    lambda df: check_non_negative(df, "product_width_cm"),
]


# SELLERS
SELLERS_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "seller_id"),
    lambda df: check_not_null(df, "seller_state"),

    # UNIQUENESS
    lambda df: check_unique(df, ["seller_id"]),
]


# PRODUCT CATEGORY TRANSLATION
PRODUCT_CATEGORY_TRANSLATION_CHECKS = [
    # COMPLETENESS
    lambda df: check_not_null(df, "product_category_name"),
    lambda df: check_not_null(df, "product_category_name_english"),

    # UNIQUENESS
    lambda df: check_unique(df, ["product_category_name"]),
]


# DATASET MAPPING
TABLE_CHECKS = {
    "olist_orders_dataset": ORDERS_CHECKS,
    "olist_customers_dataset": CUSTOMERS_CHECKS,
    "olist_geolocation_dataset": GEOLOCATION_CHECKS,
    "olist_order_items_dataset": ORDER_ITEMS_CHECKS,
    "olist_order_payments_dataset": ORDER_PAYMENTS_CHECKS,
    "olist_order_reviews_dataset": ORDER_REVIEWS_CHECKS,
    "olist_products_dataset": PRODUCTS_CHECKS,
    "olist_sellers_dataset": SELLERS_CHECKS,
    "product_category_name_translation": PRODUCT_CATEGORY_TRANSLATION_CHECKS,
}