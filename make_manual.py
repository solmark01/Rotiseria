from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor

c = canvas.Canvas('Manual_Usuario_El_Buen_Gusto.pdf', pagesize=A6)
w,h = A6
m = 5*mm

# Page 1
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-45*mm,w,45*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',16)
c.drawCentredString(w/2,h-18*mm,'EL BUEN GUSTO')
c.setFont('Helvetica-Bold',10)
c.drawCentredString(w/2,h-26*mm,'MANUAL DE USUARIO')
c.setFont('Helvetica',7)
c.drawCentredString(w/2,h-34*mm,'Rotisería • Viandas • Pedidos')
c.setFillColor(HexColor('#1e1a16'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-55*mm,'ÍNDICE')
c.setStrokeColor(HexColor('#c0713a'))
c.line(m,h-57*mm,w-m,h-57*mm)
c.setFont('Helvetica',7)
y=h-63*mm
items=[('1. Introducción','3'),('2. Navegación','3'),('3. Módulo Órdenes','4'),('4. Módulo Clientes','5'),('5. Módulo Platos','6'),('6. Módulo Informe','7'),('7. Puntos y Premios','7'),('8. Módulo Equipo','8'),('9. Configuración y Datos','8'),('10. Copias de Seguridad','9'),('11. Trucos y Consejos','9')]
for t,p in items:
    c.drawString(m,y,t)
    c.drawRightString(w-m,y,p)
    y-=3.5*mm

# Page 2
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'1. INTRODUCCIÓN')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica',7)
for line in ['El Buen Gusto es una app para gestionar','pedidos de viandas y rotisería desde el celular.','','Permite llevar órdenes, clientes, cuenta corriente,','platos, informes, puntos y más.','','Los datos se guardan en el celular.','Se puede instalar como app web.']:
    c.drawString(m,y,line)
    y-=3.2*mm
y-=1*mm
c.setFont('Helvetica-Bold',8)
c.drawString(m,y,'2. NAVEGACIÓN')
y-=4*mm
c.line(m,y,w-m,y)
y-=3.5*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Barra inferior:')
y-=3*mm
c.setFont('Helvetica',6.5)
c.drawString(m,y,'Ordenes | Clientes | Platos | Informe | Config')
y-=4*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Crear nuevo:')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Doble clic en pestaña (Ordenes/Clientes/Platos)')
y-=3*mm
c.drawString(m,y,'• O doble clic en el área de esa sección')

# Page 3
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'3. MÓDULO ÓRDENES')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Vista principal')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Filtros: Todos / Pendientes / Listos / Cancelados')
y-=3*mm
c.drawString(m,y,'• Botón "Orden del día para el chef"')
y-=3*mm
c.drawString(m,y,'• Tarjetas con cliente, platos, entrega, total')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Crear nueva orden')
y-=3*mm
c.setFont('Helvetica',7)
for s in ['1. Doble clic para abrir formulario','2. Seleccionar o crear cliente','3. Agregar uno o más platos','4. Entrega: Mensajero / Retira','5. Descuento % o $ (opcional)','6. Notas para el chef (opcional)','7. Crear Orden']:
    c.drawString(m,y,s)
    y-=2.8*mm
y-=2*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Acciones por orden')
y-=3*mm
c.setFont('Helvetica',7)
for s in ['• Listo / Volver a pendiente / Cancelar','• Pago | PDF | Imagen','• Comprobante | WA Cliente/Chef','• Eliminar']:
    c.drawString(m,y,s)
    y-=2.8*mm

# Page 4
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'4. MÓDULO CLIENTES')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Funciones')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Buscar por nombre/teléfono/dirección')
y-=3*mm
c.drawString(m,y,'• Filtrar por etiquetas y Deudores')
y-=3*mm
c.drawString(m,y,'• Doble clic para agregar cliente')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Acciones')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Cuenta Corriente (Debe/Haber/Saldo)')
y-=3*mm
c.drawString(m,y,'• Registrar pago (Efectivo/Transferencia)')
y-=3*mm
c.drawString(m,y,'• Pts - Notificar con imagen')
y-=3*mm
c.drawString(m,y,'• Editar / Eliminar')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Cuenta Corriente')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Rojo=Debe | Verde=A favor | Gris=Al día')

# Page 5
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'5. MÓDULO PLATOS')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Buscar platos')
y-=3*mm
c.drawString(m,y,'• Doble clic para agregar')
y-=3*mm
c.drawString(m,y,'• Muestra costo, precio, margen y ganancia')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Datos')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Nombre, Costo ($), Precio venta ($),')
y-=3*mm
c.drawString(m,y,'Descripción (opcional)')
y-=8*mm
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'6. MÓDULO INFORME')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Períodos: Hoy / Semana / Mes')
y-=3*mm
c.drawString(m,y,'• Venta, Costo, Utilidad, Viandas, Órdenes')
y-=3*mm
c.drawString(m,y,'• Top 5 Platos/Clientes por período y año')
y-=3*mm
c.drawString(m,y,'• Exportar PDF')

# Page 6
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'7. PUNTOS Y PREMIOS')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Funcionamiento')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Se suman al crear orden')
y-=3*mm
c.drawString(m,y,'• Configurable puntos por $1')
y-=3*mm
c.drawString(m,y,'• Ranking con medallas')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Premios y canjes')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Crear premios con puntos necesarios')
y-=3*mm
c.drawString(m,y,'• Canjear desde cliente/ranking')
y-=3*mm
c.drawString(m,y,'• Descuenta puntos al canjear')
y-=3*mm
c.drawString(m,y,'• Historial de canjes')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Notificar puntos')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Genera imagen para WhatsApp')

# Page 7
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'8. MÓDULO EQUIPO')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Agregar Chefs/Vendedores con tel')
y-=3*mm
c.drawString(m,y,'• WhatsApp directo')
y-=3*mm
c.drawString(m,y,'• Útil para enviar orden del día')
y-=8*mm
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'9. CONFIGURACIÓN Y DATOS')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Secciones')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Licencia • Backup • Puntos • Equipo')
y-=3*mm
c.drawString(m,y,'Apariencia • Contactos')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Apariencia')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Cambiar emoji y nombre del restaurante')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Contactos')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'• Importar .VCF desde Google Contacts')
y-=3*mm
c.drawString(m,y,'• Importar archivo VCF del celular')

# Page 8
c.showPage()
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'10. COPIAS DE SEGURIDAD')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Crear backup')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Config > Datos > Descargar copia completa')
y-=3*mm
c.drawString(m,y,'Guarda todo: clientes, platos, órdenes,')
y-=3*mm
c.drawString(m,y,'pagos, puntos, premios, configuración')
y-=5*mm
c.setFont('Helvetica-Bold',7)
c.drawString(m,y,'Restaurar')
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Elegir .JSON desde Descargas')
y-=3*mm
c.setFillColor(HexColor('#c0453a'))
c.setFont('Helvetica-Bold',6.5)
c.drawString(m,y,'¡Importante! Reemplaza TODOS los datos')
c.setFillColor(HexColor('#1e1a16'))
y-=3*mm
c.setFont('Helvetica',7)
c.drawString(m,y,'Hacer backup antes de restaurar')
y-=8*mm
c.setFillColor(HexColor('#c0713a'))
c.rect(0,h-12*mm,w,12*mm,fill=1)
c.setFillColor(HexColor('#ffffff'))
c.setFont('Helvetica-Bold',9)
c.drawString(m,h-8*mm,'11. TRUCOS Y CONSEJOS')
c.setFillColor(HexColor('#1e1a16'))
y=h-18*mm
c.setFont('Helvetica',6.8)
tips=['• Doble clic = crear rápido','• Orden del día para el chef','• PDF/imagen de comprobante','• Controlar deuda en Cuenta Corriente','• Usar puntos para fidelizar','• Importar contactos .VCF','• Hacer backup semanal','• Instalar app en inicio','• Marcar Pendiente/Listo/Cancelado']
for t in tips:
    c.drawString(m,y,t)
    y-=3*mm
y-=3*mm
c.setFont('Helvetica',6)
c.setFillColor(HexColor('#8a7e72'))
c.drawCentredString(w/2,y,'El Buen Gusto • Manual optimizado para celular')

c.save()
print('ok')
