<?php 
	session_start();

	if(!isset($_SESSION["login"])){
		header("Location: ../pertemuan12/login.php");
		exit();
	}
	require "function.php";

	$jumlahDataPerhalaman = 1;
	$jumlahData = count(query("SELECT * FROM tb_mhs5a"));
	$jumlahHalaman = ceil($jumlahData/$jumlahDataPerhalaman);
	$halamanActive = (isset($_GET['halaman']))?$_GET['halaman']:1;
	$awalData = ($jumlahDataPerhalaman*$halamanActive)-$jumlahDataPerhalaman;

	$mahasiswa= query("SELECT * FROM tb_mhs5a LIMIT $awalData , $jumlahDataPerhalaman");
	// $mahasiswa= query("SELECT * FROM tb_mhs5a ORDER BY id DESC");
	if (isset($_POST['cari'])) {
		$mahasiswa = cari($_POST['kata_kunci']);
	}
 ?>
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Halaman Depan</title>
</head>
<body>


	<h1>Daftar Mahasiswa</h1>
	<a href="../pertemuan12/logout.php">Keluar</a>|<a href="../pertemuan15/cetak.php" target="_blank">Cetak</a>
	<form action="" method="post" style="padding:20px;">
		
		<input type="text" name="kata kunci" size="30" autofocus placeholder="Massukan Kata Pencarian" autocomplete="on">
		<button type="submit" name="cari">Cari</button>
	</form>
		<?php if($halamanActive > 1 ) :  ?>
				<a href="?halaman=<?=$halamanActive -1; ?>">&laquo;</a>
		<?php endif; ?>

		<?php for ($i=1; $i <= $jumlahHalaman ; $i++) : ?>
			<?php if ($i == $halamanActive) : ?>
				<a href="?halaman=<?= $i ;?>" style="font-weight: bold; color: red;">
					<?= $i; ?>
				</a>
			<?php else:  ?>
				<a href="?halaman=<?= $i ;?>">
					<?= $i; ?>
				</a>
			<?php endif; ?>
		<?php endfor; ?>
		<?php if($halamanActive < $jumlahHalaman ) :  ?>
			<a href="?halaman=<?=$halamanActive + 1; ?>">&raquo;</a>
		<?php endif; ?>

	<a href="../pertemuan3/tambah.php">Tambah Data Mahasiswa</a>
	
	<table border="1" cellpadding="5" cellspacing="0">
		<tr>
			<th>ID</th>
			<th>Nama</th>
			<th>NIM</th>
			<th>Email</th>
			<th>Jurusan</th>
			<th>Photo</th>
			<th>Aksi</th>
		</tr>
		<tr>
			<?php $i=1; ?>
			<?php 
			foreach ($mahasiswa as $row):
			?>
			<tr>
				<td><?php echo $i ?></td>
				<td><?php echo $row['nama']; ?></td>
				<td><?php echo $row['nim']; ?></td>
				<td><?php echo $row['email']; ?></td>
				<td><?php echo $row['jurusan']; ?></td>
				<td><img src="../img/<?php echo $row ['photo'] ?>" width="50" alt=""></td>
				<td>
					<a href="../pertemuan6/ubah.php?id=<?php echo $row['id']; ?>">EDIT</a>
					<a href="../pertemuan6/hapus.php?id=<?php echo $row['id']; ?>"
						onClick=" return confirm('Yakin data akan dihapus');"
						>HAPUS</a>
				</td>
			</tr>
			<?php $i++; ?>
			<?php 
		endforeach;
		?>
		</tr>
	</table>

	
</body>
</html>