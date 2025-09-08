ALTER TABLE restaurants RENAME TO restaurant_info;

ALTER TABLE menus RENAME TO menu_items;

ALTER TABLE restaurant_info
RENAME COLUMN location TO address;

ALTER TABLE menu_items
ADD COLUMN available BOOLEAN DEFAULT TRUE

DROP TABLE menu_items