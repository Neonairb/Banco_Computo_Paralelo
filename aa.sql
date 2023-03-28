CREATE OR REPLACE PROCEDURE INSERT_SUCURSAL (
    idsucursal IN VARCHAR,
    nombresucursal IN VARCHAR,
    ciudadsucursal IN VARCHAR,
    activos IN NUMBER,
    region IN NUMBER
)
IS
BEGIN
IF region = 1 THEN
INSERT INTO sucursal1_sin
VALUES (idsucursal, nombresucursal, ciudadsucursal, activos, region);
COMMIT;
ELSE
INSERT INTO sucursal2_sin
VALUES (idsucursal, nombresucursal, ciudadsucursal, activos, region);
COMMIT;
END IF;
END;