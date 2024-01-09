<?php 
 require '../Pertemuan2/function.php';


 $id = $_GET['id'];

 if (hapus($id) > 0 ) { 
 	echo "
 		 <script>
 		 	alert('Data Berhasil Dihapus');
 		 	document.location.href = '../Pertemuan2/index.php';
 		 </script>
 	";

 }else{ 
 	echo "
 		 <script>
 		 	alert('Data Gagal Dihapus');
 		 	document.location.href = '../Pertemuan2/index.php';
 		 </script>
 	";
 }
 ?>

