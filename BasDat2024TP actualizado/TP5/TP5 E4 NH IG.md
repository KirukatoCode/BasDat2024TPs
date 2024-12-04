# _Ejercicio 4 del Trabajo Practico 5, por Hubert Noelia Belén y Guardese Iván_

# DISEÑO DE LA BASE DE DATOS PARA TALLERES DE AUTOS:

## Dependencias Funcionales (DFs)

- **`codigoSucursal -> domicilioSucursal, telefonoSucursal`**
  El `codigoSucursal` identifica de manera única el domicilio y teléfono de una sucursal.

- **`codigoSucursal, codigoFosa -> largoFosa, anchoFosa`**
  Una combinación de `codigoSucursal` y `codigoFosa` determina las dimensiones de cada fosa.

- **`codigoSucursal, codigoFosa, patenteAuto -> marcaAuto, modeloAuto, dniCliente`**
  Cada registro en este contexto indica el auto reparado en una fosa específica de una sucursal y a qué cliente pertenece.

- **`patenteAuto -> marcaAuto, modeloAuto, dniCliente`**
  La patente identifica de manera única cada auto, incluyendo su marca, modelo y cliente propietario.

- **`dniCliente -> nombreCliente, celularCliente`**
  El `dniCliente` identifica de manera única al cliente, permitiendo obtener su nombre y celular.

- **`dniMecanico -> nombreMecanico, emailMecanico`**
  Cada mecánico está identificado por su `dniMecanico`, que permite obtener su nombre y correo electrónico.

----------------------------------------------------------------------------------------------------

## Claves Candidatas:
La combinación de `codigoSucursal`, `codigoFosa`, `patenteAuto` permite identificar de manera única un registro en el contexto de la base de datos, ya que incluye:

- **`codigoSucursal`**: Determina la sucursal.
- **`codigoFosa`**: Identifica la fosa dentro de la sucursal.
- **`patenteAuto`**: Identifica de manera única un auto.

Por lo tanto, esta combinación es la clave candidata.

----------------------------------------------------------------------------------------------------

## Clave Primaria:
**Clave primaria elegida:**
`codigoSucursal, codigoFosa, patenteAuto`

**Justificación:**
Esta clave refleja la jerarquía y las relaciones entre sucursales, fosas y autos, siendo la más representativa y adecuada para identificar registros sin ambigüedad.

----------------------------------------------------------------------------------------------------

## Normalización:
### 1FN: Primera Forma Normal:
El esquema inicial ya cumple con la 1FN porque todos los atributos tienen valores atómicos y no hay listas o repeticiones dentro de un mismo campo.

----------------------------------------------------------------------------------------------------

### 2FN: Segunda Forma Normal:
Para alcanzar la 2FN, eliminamos dependencias parciales descomponiendo los datos en tablas más pequeñas, agrupando los atributos en función de las dependencias funcionales completas.

- **`Sucursal`**: `{codigoSucursal, domicilioSucursal, telefonoSucursal}`
- **`Fosa`**: `{codigoSucursal, codigoFosa, largoFosa, anchoFosa}`
- **`AutoCliente`**: `{codigoSucursal, codigoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente}`
- **`Cliente`**: `{dniCliente, nombreCliente, celularCliente}`
- **`Mecanico`**: `{dniMecanico, nombreMecanico, emailMecanico}`
- **`Arreglo`**: `{codigoSucursal, codigoFosa, patenteAuto, dniMecanico}`

----------------------------------------------------------------------------------------------------

### 3FN: Tercera Forma Normal:
Para alcanzar la 3FN, eliminamos dependencias transitivas reorganizando las tablas. En este punto, cada atributo no clave depende directamente de la clave primaria.

#### **Tabla Sucursal**
- `codigoSucursal` (Clave primaria)
- `domicilioSucursal`
- `telefonoSucursal`

#### **Tabla Fosa**
- `codigoSucursal` (Clave foránea a Sucursal)
- `codigoFosa` (Clave primaria compuesta junto con `codigoSucursal`)
- `largoFosa`
- `anchoFosa`

#### **Tabla Auto**
- `patenteAuto` (Clave primaria)
- `marcaAuto`
- `modeloAuto`
- `dniCliente` (Clave foránea a Cliente)

#### **Tabla Cliente**
- `dniCliente` (Clave primaria)
- `nombreCliente`
- `celularCliente`

#### **Tabla Mecanico**
- `dniMecanico` (Clave primaria)
- `nombreMecanico`
- `emailMecanico`

#### **Tabla Reparacion**
- `codigoSucursal` (Clave foránea a Sucursal)
- `codigoFosa` (Clave foránea a Fosa)
- `patenteAuto` (Clave foránea a Auto)
- `dniMecanico` (Clave foránea a Mecanico)
- Clave primaria compuesta: (`codigoSucursal`, `codigoFosa`, `patenteAuto`, `dniMecanico`)