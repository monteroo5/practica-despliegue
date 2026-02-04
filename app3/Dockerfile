FROM php:8.1-apache
# Instalar extensiones necesarias para MySQL
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
# Copiar el archivo index.php al servidor web
COPY index.php /var/www/html/
EXPOSE 80
