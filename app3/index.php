<?php
$host = '172.31.18.91'; // Mi IP Privada
$user = 'admin_practica';
$pass = 'Sandia4you';
$db   = 'db_app3';

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("❌ Error de conexión: " . $conn->connect_error);
}
echo "✅ ¡Conexión exitosa a la Base de Datos en la Instancia 4 desde un contenedor Docker!";
?>
