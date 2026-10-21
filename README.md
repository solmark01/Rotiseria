# El Buen Gusto — PWA

Sistema de gestión de viandas con licencias Solmark.

## Archivos

| Archivo | Descripción |
|---|---|
| `index.html` | App principal |
| `manifest.json` | Configuración PWA |
| `sw.js` | Service Worker (modo offline) |
| `clave.js` | Clave pública ECDSA (generada por Solmark) |
| `icon-192.png` | Ícono PWA |
| `icon-512.png` | Ícono PWA grande |

## Pasos para publicar en GitHub Pages

1. Crear un repositorio en GitHub (ej: `el-buen-gusto`)
2. Subir todos estos archivos al repositorio
3. Ir a Settings → Pages → Source: **main branch / root**
4. La app queda en: `https://TU_USUARIO.github.io/el-buen-gusto/`

## Conectar con Solmark

1. Abrir Solmark → módulo **Aplicaciones** → **+ Nueva aplicación**
2. Nombre: `El Buen Gusto` (o el nombre del cliente)
3. Link: URL de GitHub Pages del cliente
4. Guardar

Para generar la primera clave de un cliente:
1. Solmark → **Claves** → **Descargar clave.js**
2. Reemplazar el `clave.js` del repositorio con el descargado
3. Hacer commit y push — tarda ~1 minuto en actualizar

Para activar la licencia de un cliente:
1. Solmark → cliente → **Generar clave**
2. Poner fecha de vencimiento
3. Copiar la clave generada y enviársela al cliente
4. El cliente la pega en la app → **Datos** → campo de clave

## Cada cliente tiene su propio repositorio

Cada instancia de la app es un repo de GitHub independiente con el
`clave.js` de ese cliente. El `clave.js` se genera UNA SOLA VEZ
con las mismas claves ECDSA y sirve para TODOS los clientes.

## Estructura de licencias

- **7 días** de prueba gratis desde la primera apertura
- Al vencer: pantalla de bloqueo con código de cliente
- El cliente pide clave → vos la generás en Solmark → él la pega
- Las claves se firman con ECDSA P-256 (no se pueden falsificar)
