<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");   
$hostname_localhost ="ardbud.mysql.pythonanywhere-services.com";
$database_localhost ="ardbud$asecontfg";
$username_localhost ="ardbud";
$password_localhost ="tfgasecon18";
$json=array();
		
		if(isset($_GET["user_id"])){
		$user_id=$_GET["user_id"];
		
		$conexion = mysqli_connect($hostname_localhost,$username_localhost,$password_localhost,$database_localhost);
		mysqli_set_charset($conexion, "utf8");
		$consulta="SELECT web_noticia.id FROM web_noticia INNER JOIN noticias_usuarios ON web_noticia.id=noticias_usuarios.noticia_id where noticias_usuarios.usuario_id='${user_id}'";

		$resultado=mysqli_query($conexion,$consulta);
		
		while($registro=mysqli_fetch_array($resultado)){
			$json['noticia'][]=$registro;
			//echo $registro['id'].' - '.$registro['nombre'].'<br/>';
		}
		mysqli_close($conexion);
		echo json_encode($json);
	}
	else{
		$resultar["success"]=0;
		$resultar["message"]='Ws no Retorna';
		$resultar["nombre"] = 'null';
		$json['noticia'][]=$resultar;
		echo json_encode($json);
	}
?>