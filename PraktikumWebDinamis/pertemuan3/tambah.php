<?php 

	require "../Pertemuan2/function.php";
	
	if (isset($_POST["submit"])) {
		if (tambah($_POST)>0) {
			echo "
				<script>
					alert('Data Berhasil Di Ditambahkan');
					document.location.href='../Pertemuan2/index.php';
				</script>";
		}else{
			echo "<script>
					alert('Data Gagal Di Ditambahkan');
					document.location.href='../Pertemuan2/index.php';
				</script>";
		}
	}
	
 ?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Tambah Data Mahasiswa</title>
</head>
<body>
	<h1>Tambah Data Mahasiswa</h1>

	<form action="" method="post"  enctype="multipart/form-data">
		<li>
			<label for="nama" > Nama</label>
			<input type="text" name="nama" id="nama">
		</li>
		<li>
			<label for="nim" >NIM</label>
			<input type="text" name="nim" id="nim">
		</li>
		<li>
			<label for="jurusan" >Jurusan</label>
			<input type="text" name="jurusan" id="jurusan">
		</li>
		<li>
			<label for="email" >Email</label>
			<input type="text" name="email" id="email">
		</li>
		<li>
			<label for="photo" >Photo</label>
			<input type="file" name="photo" id="photo">
		</li>
		<li>
			<button type="submit" name="submit">Tambah Data</button>
		</li>
	</form>
	<a href="../Pertemuan2/index.php">Back</a>
</body>
</html>