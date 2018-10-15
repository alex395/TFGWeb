<?PHP
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");   
$hostname_localhost ="ardbud.mysql.pythonanywhere-services.com";
$database_localhost ="ardbud$asecontfg";
$username_localhost ="ardbud";
$password_localhost ="tfgasecon18";
$json=array();
	if(isset($_GET["usuario_id"]) && isset($_GET["peticion_id"]) && isset($_GET["titulo"]) && isset($_GET["archivo"]) && isset($_GET["fecha"])){
		$usuario_id=$_GET['usuario_id'];
		$peticion_id=$_GET['peticion_id'];
		$titulo=$_GET['titulo'];
		$archivo=$_GET['archivo'];
		$fecha=$_GET['fecha'];
		
		$conexion=mysqli_connect($hostname_localhost,$username_localhost,$password_localhost,$database_localhost);
		
		$insert="INSERT INTO web_envio(titulo, archivo, fecha, usuario_id, peticion_id) VALUES ('{$titulo}','{$archivo}',CAST(N'${fecha}' AS DateTime),{$usuario_id},{$peticion_id})";
		$resultado_insert=mysqli_query($conexion,$insert);
		
		if($resultado_insert){
			$consulta="SELECT * FROM web_envio WHERE titulo = '{$titulo}'";
			$resultado=mysqli_query($conexion,$consulta);
			
			if($registro=mysqli_fetch_array($resultado)){
				$json['envio'][]=$registro;
			}
			mysqli_close($conexion);
			echo json_encode($json);
		}
		else{
			$resulta["titulo"]='null';
			$resulta["descripcion"]='null';
			$resulta["fecha"]='null';
			$json['envio'][]=$resulta;
			echo json_encode($json);
		}
		
	}
	else{
			$resulta["titulo"]='fallo';
			$resulta["descripcion"]='fallo';
			$resulta["fecha"]='fallo';
			$json['envio'][]=$resulta;
			echo json_encode($json);
		}
?>