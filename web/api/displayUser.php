<?PHP
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");   
$hostname_localhost ="ardbud.mysql.pythonanywhere-services.com";
$database_localhost ="ardbud$asecontfg";
$username_localhost ="ardbud";
$password_localhost ="tfgasecon18";
$json=array();
	if(isset($_GET["id"])){
		$id=$_GET["id"];
				
		$conexion = mysqli_connect($hostname_localhost,$username_localhost,$password_localhost,$database_localhost);
		$consulta="select * from web_usuario where id= '{$id}'";
		$resultado=mysqli_query($conexion,$consulta);
			
		if($registro=mysqli_fetch_array($resultado)){
			$json['usuario'][]=$registro;
		//	echo $registro['id'].' - '.$registro['nombre'].' - '.$registro['profesion'].'<br/>';
		}else{
			$resultar["email"]='null';
			$resultar["nombre"]='null';
			$resultar["password"]='null';
			$json['usuario'][]=$resultar;
		}
		
		mysqli_close($conexion);
		echo json_encode($json);
	}
	else{
		$resultar["success"]=0;
		$resultar["message"]='Ws no Retorna';
		$resultar["nombre"] = 'null';
		$json['usuario'][]=$resultar;
		echo json_encode($json);
	}
?>