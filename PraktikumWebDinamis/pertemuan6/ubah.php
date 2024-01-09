<?php 
	require "../Pertemuan2/function.php";
	
	$id = $_GET["id"];

	


	$mhs = query("SELECT * FROM `tb_mhs5a` WHERE id= $id")[0];

	if (isset($_POST['submit'])) {
		if (ubah($_POST) > 0 ) {
 	echo "
 		 <script>
 		 	alert('Data Berhasil Di Ubah');
 		 	document.location.href = '../Pertemuan2/index.php';
 		 </script>
 	";

 	}else{
 	echo "
 		 <script>
 		 	alert('Data Gagal Di Ubah');
 		 	document.location.href = '../Pertemuan2/index.php';
 		 </script>
 		";
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

	<form action="" method="post" enctype="multipart/form-data">
		<input type="hidden" name="id" value="<?php echo $mhs['id'] ?>">
		<input type="hidden" name="photoLama" value="../img/<?php echo $mhs['photo'] ?>">
		<li>
			<label for="nama"> Nama</label>
			<input type="text" name="nama" id="nama"
				required 
				value="<?php echo $mhs["nama"];  ?>" 
			>
		</li>
		<li>
			<label for="nim" >NIM</label>
			<input type="text" name="nim" id="nim"
			required
				value="<?php echo $mhs["nim"];  ?>"
			>
		</li>
		<li>
			<label for="jurusan" >Jurusan</label>
			<input type="text" name="jurusan" id="jurusan"
			required
				value="<?php echo $mhs["jurusan"];  ?>"
			>
		</li>
		<li>
			<label for="email" >Email</label>
			<input type="text" name="email" id="email"
			required
				value="<?php echo $mhs["email"];  ?>"
			>
		</li>
		<li>
			<label for="photo" >Photo</label>
			<img src="../img/<?php echo $mhs["photo"]; ?>" width="40px"> <br>
			<input type="file" name="photo" id="photo"
			required
				value="<?php echo $mhs["photo"];  ?>"
			>
		</li>
		<li>
			<button type="submit" name="submit">Tambah Data</button>
		</li>
	</form>
	<a href="../Pertemuan2/index.php">Back</a>
</body>
</html>