<?PHP
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");   
$hostname_localhost ="ardbud.mysql.pythonanywhere-services.com";
$database_localhost ="ardbud$asecontfg";
$username_localhost ="ardbud";
$password_localhost ="tfgasecon18";
$json=array();
	if(isset($_GET["usuario_id"]) && isset($_GET["noticia_id"])){
		$usuario_id=$_GET['usuario_id'];
		$noticia_id=$_GET['noticia_id'];
		
		$conexion=mysqli_connect($hostname_localhost,$username_localhost,$password_localhost,$database_localhost);
		
		$insert="INSERT INTO noticias_usuarios(usuario_id, noticia_id) VALUES ({$usuario_id},{$noticia_id})";
		$resultado_insert=mysqli_query($conexion,$insert);
		
		if($resultado_insert){
			$consulta="SELECT * FROM noticias_usuarios WHERE usuario_id = '{$usuario_id}'";
			$resultado=mysqli_query($conexion,$consulta);
			
			if($registro=mysqli_fetch_array($resultado)){
				$json['noticia'][]=$registro;
			}
			mysqli_close($conexion);
			echo json_encode($json);
		}
		else{
			$resulta["usuario_id"]='null';
			$resulta["noticia_id"]='null';
			$json['noticia'][]=$resulta;
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