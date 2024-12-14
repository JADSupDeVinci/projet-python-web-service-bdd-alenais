     DELIMITER //

CREATE PROCEDURE AddTypeIngredient(
    IN label VARCHAR(100)
)
BEGIN
    INSERT INTO typeingredient (label)
    VALUES (label);
END //

DELIMITER ;