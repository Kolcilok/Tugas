<?php 
	require "koneksi.php";

	function query($query){
		global $koneksi_db;
		$result= mysqli_query($koneksi_db,$query);
		$rows = [];
		while($row = mysqli_fetch_assoc($result)){
			$rows[] = $row;
		};
		return $rows;
	}



	function upload(){
		$namaFile = $_FILES['photo']['name'];
		$ukuranFile = $_FILES['photo']['size'];
		$error = $_FILES['photo']['error'];
		$tmpName = $_FILES['photo']['tmp_name'];

		// Wajib Upload Foto
		if($error === 4) {
			echo "
				<script> 
					alert('Pilih photo terlebih dahulu !');
				</script>";

			return false;
		}


		// type file photo
		$ekstensiPhotoDiijinkan = ['jpg','jpeg','png'];
		$ekstensiPhoto = explode('.',$namaFile);
		$ekstensiPhoto = strtolower(end($ekstensiPhoto));

		if(!in_array($ekstensiPhoto, $ekstensiPhotoDiijinkan)) {
			echo "<script> 
				alert('Type File Tidak Di dukung');
				</script>";
			return false;
		}

		if($ukuranFile > 1000000) {
			echo "<script> 
				alert('Ukuran Photo melebihi  ketentuan (<1Mb) !');
				</script>";
			return false;
		}

		$namaFileBaru = uniqid();
		$namaFileBaru = '.';
		$namaFileBaru= $ekstensiPhoto;

		move_uploaded_file($tmpName,'../img/'.$namaFileBaru);
		return $namaFileBaru;


	
	}

	function tambah($data){
		global $koneksi_db; 
		$nama = htmlspecialchars($data['nama']); 
		$nim = htmlspecialchars($data['nim']) ;
		$jrs = htmlspecialchars($data['jurusan']) ;
		$email = htmlspecialchars($data['email']); 
		$photo = upload();
			
		if (!$photo ) {
			return 0;
		}

		$query = "INSERT INTO tb_mhs5a VALUES('', '$nama', '$nim', '$jrs', '$email', '$photo')";

	mysqli_query($koneksi_db,$query);

	return mysqli_affected_rows($koneksi_db);

	}

	function hapus($id){
		global $koneksi_db;
		mysqli_query($koneksi_db,"DELETE FROM tb_mhs5a WHERE id=$id");
		return mysqli_affected_rows($koneksi_db);
	}

	function ubah($data){
		global $koneksi_db; 

		$id = $data['id'];
		$nama = htmlspecialchars($data['nama']); 
		$nim = htmlspecialchars($data['nim']) ;
		$jrs = htmlspecialchars($data['jurusan']) ;
		$email = htmlspecialchars($data['email']); 
		$photoLama = htmlspecialchars($data['photoLama']);

		if ($_FILES['photo']['error']===4) {
			$photo = $photoLama;
		}else{
			$photo = upload();
		}

		$query = "UPDATE tb_mhs5a SET 
			nama='$nama',
			nim='$nim',
			jurusan='$jrs',
			email='$email',
			photo='$photo'
			 WHERE id = $id
			 "; 

	mysqli_query($koneksi_db,$query);

	return mysqli_affected_rows($koneksi_db);

	}

	

	function cari($kata_kunci){
		$query = "SELECT * FROM tb_mhs5a WHERE 
		nama LIKE '%$kata_kunci%' OR
		nim LIKE '%$kata_kunci%' OR
		jurusan LIKE '%$kata_kunci%' OR
		email LIKE '%$kata_kunci%'
		 ";
		return query($query);
	}


	function registrasi($data){
		global $koneksi_db;

		$username =strtolower(stripcslashes($data["username"]));
		$password = mysqli_real_escape_string($koneksi_db,$data["password"]);
		$password2 = mysqli_real_escape_string($koneksi_db,$data['password2']);

		$result = mysqli_query($koneksi_db,"SELECT  username FROM tb_user WHERE username = '$username'");

		if (mysqli_fetch_assoc($result)) {
			echo "<script> 
				alert('username Sudah Terdaftar ! ');
				</script>";
				return false;
		}

		if ($password !== $password2) {
			echo "<script> 
				alert('konfirmasi password tidak sama silakan isi kembali');
				</script>";
				return false;
		}

		$password = password_hash($password, PASSWORD_DEFAULT);

		mysqli_query($koneksi_db,"INSERT INTO tb_user VALUES ('', '$username', '$password')");
		
		return mysqli_affected_rows($koneksi_db);

	}

	
 ?>
