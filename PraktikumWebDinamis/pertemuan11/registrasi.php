<?php 
	require '../Pertemuan2/function.php';

	if (isset($_POST['register'])) {
		if (registrasi($_POST)>0) {
			echo "<script> 
				alert('Userr Baru Berhasil Di Ditambahkan');
				</script>";
		}else{
			echo mysqli_error($koneksi_db);
		}
	}


 ?>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Halaman Registrasi</title>

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
	<h1 style="text-align: center;">Halaman Registrasi</h1>
	<marquee>hahah</marquee>
	<center>
		<div class="id">
		<form action="" method="post" >
		<li>
			<label for="username" > Username</label>
			<input type="text" name="username" id="username">
		</li>
		<li>
			<label for="password" >Password</label>
			<input type="password" name="password" id="password">
		</li>
		<li>
			<label for="password2" >Konfirmasi Password</label>
			<input type="password" name="password2" id="password2">
		</li>
		<li>
			<button type="submit" name="register">Login</button>
		</li>
	</form>
	</div>
	</center>
</body>
</html>