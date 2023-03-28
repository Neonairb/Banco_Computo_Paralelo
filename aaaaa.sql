CREATE OR REPLACE TRIGGER INSERT_GLOBAL_PRESTAMO
AFTER INSERT OR UPDATE OR DELETE
ON PRESTAMO2
FOR EACH ROW
BEGIN
  IF INSERTING THEN
    INSERT INTO PRESTAMO_C1
      VALUES (:NEW.noprestamo, :NEW.idsucursal, :NEW.cantidad);
	INSERT INTO PRESTAMO_C2
      VALUES (:NEW.noprestamo, :NEW.idsucursal, :NEW.cantidad);
  ELSIF UPDATING THEN
    UPDATE PRESTAMO_C1
      SET noprestamo = :NEW.noprestamo,
          idsucursal = :NEW.idsucursal,
          cantidad = :NEW.cantidad
      WHERE noprestamo = :OLD.noprestamo;
    UPDATE PRESTAMO_C2
      SET noprestamo = :NEW.noprestamo,
          idsucursal = :NEW.idsucursal,
          cantidad = :NEW.cantidad
      WHERE noprestamo = :OLD.noprestamo;
  ELSIF DELETING THEN
    DELETE FROM PRESTAMO_C1
      WHERE noprestamo = :OLD.noprestamo;
    DELETE FROM PRESTAMO_C2
      WHERE noprestamo = :OLD.noprestamo;
  END IF;
END;
