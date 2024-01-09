<?php 
	session_start();
	if(isset($_SESSION["login"])){
		header("Location: ../Pertemuan2/index.php");
		exit;
	}

	require '../Pertemuan2/function.php';
	if (isset($_POST["login"])) {
		$username = $_POST["username"];
		$password = $_POST["password"];

		$result = mysqli_query($koneksi_db,"SELECT * FROM tb_user WHERE username ='$username'");

		if (mysqli_num_rows($result) === 1) {
			$row = mysqli_fetch_assoc($result);
			if (password_verify($password,$row["password"])) {
				$_SESSION["login"] = true;
				header("Location : index.php");
				exit;
			}
		}
		 $error = true;
	}

 
 ?>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Halaman Login</title>

	<style>

		.id{
			background-color: cyan;
			padding: 20px;
			width: 200px;
		}
		form{

		}
		label{
			display: block;
		}

		li{
			list-style: none;
		}
	</style>
</head>
<body>
	<h1 style="text-align: center;">Halaman Login</h1>
	<?php if (isset($error)) :?>
		<p style="color: red; font-style: italic;"> Username / Password Salah</p>

	<?php endif;  ?>
	<marquee>hahah</marquee>
	<center>
		<div class="id">
		<form action="" method="post" >
		<li>
			<label for="username" > Username</label>
			<input type="text" name="username" id="username" required>
		</li>
		<li>
			<label for="password" >Password</label>
			<input type="password" name="password" id="password">
		</li>
		<li>
			<button type="submit" name="login">Login</button>
		</li>
	</form>
	</div>
	</center>
</body>
</html>