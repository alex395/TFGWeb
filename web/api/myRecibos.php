<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");   
$hostname_localhost ="ardbud.mysql.pythonanywhere-services.com";
$database_localhost ="ardbud$asecontfg";
$username_localhost ="ardbud";
$password_localhost ="tfgasecon18";
$json=array();
				
	if(isset($_GET["usuario_id"])){
		$usuario_id=$_GET["usuario_id"];
		
		$conexion = mysqli_connect($hostname_localhost,$username_localhost,$password_localhost,$database_localhost);
		$consulta="select * from web_recibo where usuario_id= '{$usuario_id}'";

		$resultado=mysqli_query($conexion,$consulta);
		
		while($registro=mysqli_fetch_array($resultado)){
			$json['recibo'][]=$registro;
			//echo $registro['id'].' - '.$registro['nombre'].'<br/>';
		}
		mysqli_close($conexion);
		echo json_encode($json);
	}
	else{
		$resultar["success"]=0;
		$resultar["message"]='Ws no Retorna';
		$resultar["nombre"] = 'null';
		$json['recibo'][]=$resultar;
		echo json_encode($json);
	}
?>