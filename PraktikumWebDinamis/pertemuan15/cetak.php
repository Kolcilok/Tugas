<?php 
require_once __DIR__. '/vendor/autoload.php';

require '../Pertemuan2/function.php';
$mahasiswa= query("SELECT * FROM tb_mhs5a");

$mpdf = new \Mpdf\Mpdf();

$html = '<!DOCTYPE html>
<html>
<head>
	<title>Daftar Mahasiswa</title>
</head>
<body>
	<h1>Daftar Mahasiswa</h1>

	<table border="1" cellpadding="10" cellspacing="0">
		<tr>
			<th>ID</th>
			<th>Nama</th>
			<th>NIM</th>
			<th>Email</th>
			<th>Jurusan</th>
			<th>Photo</th>
			<th>Aksi</th>
		</tr>';
		$i = 1;
		foreach ($mahasiswa as $mhs){
		$html .='<tr>
				<td>'.$i++.'</td>
				<td>'. $mhs['nama'].'</td>
				<td>'. $mhs['nim'].'</td>
				<td>'. $mhs['email'].'</td>
				<td>'. $mhs['jurusan'].'</td>
				<td><img src="../img/'. $mhs ['photo'].'" width="50" alt=""></td>
				<td>
			</tr>';
		};
$html .=	'</table>
</body>
</html>';
		

$mpdf->WriteHTML($html);
$mpdf->Output();
 ?>


