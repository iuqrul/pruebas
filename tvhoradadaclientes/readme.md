Área de clientes de TvHoradada
==============

Entorno de desarrollo
--------------
tvh.o2w.es
usuario: 52528342-E
clave: daigual


Archivos relaccionados con Angular JS
--------------
clientes/static/js -> Archivos javascript
clientes/static/views -> Archivos de vistas html



Cómo ejecutar la apliación de cliente
--------------

Es posible ejecutar la parte de cliente de la aplicación en offline sin necesidad de configurar ningún servidor web para ver el resultado. Todo gracias a "The Cors"

* Para ello tenemos que ir al directorio clientes/static
* Una vez ahí podemos abrir el archivo index.html con el firefox
* O bien con el Chrome, pero tenemos que pasarle unos parámetros para que nos permita usar cors en archivos locales.


  google-chrome --args -allow-file-access-from-files index.html
  o
  chromium --args -allow-file-access-from-files index.html



Presentación
------------
http://tvh.o2w.es/docs/frontend.html
En pdf: http://tvh.o2w.es/docs/frontend.pdf
