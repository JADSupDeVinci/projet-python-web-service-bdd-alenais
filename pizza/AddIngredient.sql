DELIMITER //

CREATE PROCEDURE AddIngredient(
    IN label VARCHAR(100),
    IN label_commercial VARCHAR(100),
    IN id_typeingredient INT
)
BEGIN
    INSERT INTO ingredient (label, label_commercial, id_typeingredient)
    VALUES (label, label_commercial, id_typeingredient);
    SELECT LAST_INSERT_ID() AS id;
END //

DELIMITER ;