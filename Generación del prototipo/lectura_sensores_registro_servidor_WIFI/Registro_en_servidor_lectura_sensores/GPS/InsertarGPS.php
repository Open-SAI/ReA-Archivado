<!DOCTYPE html>
<html>
<head>
<title>Registro BD</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="Refresh" content="1;url=http://10.42.0.82">	 
</head>
<?php
//include("conexion.php");
$host = "localhost";
$user = "root";
$pw	=  "DiosPerdoname@";  
$db	= "Registro";

$Lat =  $_GET["Latitud"];
$Lon =  $_GET["Longitud"];
$Tem = $_GET["Temperatura"];
$VelT = $_GET["Velocidad"];

echo "Datos de Geolocalizaci&oacuten <br>";
echo  "Latitud: $Lat <br>";
echo  "Longitud: $Lon <br>";
echo  "Temperatura: $Tem <br>";
echo  "Velocidad: $VelT <br>";


if(isset ($Lat) && !empty($Lat) && 
	isset ($Lon) && !empty($Lon) &&
	isset ($Tem) && !empty($Tem) &&
	isset ($VelT) && !empty($VelT) )
	
	{
		$con = mysql_connect($host, $user, $pw) or die ("Problemas al conectar");
		mysql_select_db($db, $con) or die ("Problemas al conectar la DB");
		mysql_query("INSERT INTO GEODATA (Latitud, Longitud, Temperatura, Velocidad) VALUES ('$Lat','$Lon', '$Tem', '$VelT')", $con);
		echo "datos insertados";
	}
	else {
		echo "Problemas al insertar datos";
	}
?>