   DELIMITER //

CREATE PROCEDURE UpdateIngredient(
    IN label_com VARCHAR(255),
    IN ingredient_id INT
)
BEGIN
    UPDATE ingredient
    SET label_commercial = label_com
    WHERE id = ingredient_id;
END //

DELIMITER ;