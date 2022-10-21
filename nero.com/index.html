<?php
    session_start();
    
    if( !isset($_SESSION["login"]) )
    {
        header("Location: login.php");
        exit;
    }
    
    require 'function.php';
    $makanan = query("SELECT * FROM makanan");

    // Tombol cari diklik
    if( isset($_POST["cari"]) )
    {
        $makanan = cari($_POST["keyword"]);
    }
    
?>

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>
    Home
  </title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="https://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/business-casual.min.css" rel="stylesheet">
  <style>
table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 15px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: black;
  color: white;
}
</style>

</head>

<body>

  <h1 class="site-heading text-center text-white d-none d-lg-block">
    <span class="site-heading-lower">
      PizzaMan
    </span>
    <span class="site-heading-upper text-primary mb-3">
      Calories Counting Website
    </span>
  </h1>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark py-lg-4" id="mainNav">
    <div class="container">
      <a class="navbar-brand text-uppercase text-expanded font-weight-bold d-lg-none" href="#">
        Start Bootstrap
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item active px-lg-4">
            <a class="nav-link text-uppercase text-expanded" href="index.php">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item px-lg-4">
            <a class="nav-link text-uppercase text-expanded" href="calculator.php">Calculator</a>
          </li>
          <li class="nav-item px-lg-4">
            <a class="nav-link text-uppercase text-expanded" href="collaboration.php">Collaboration</a>
          </li>
          <li class="nav-item px-lg-4">
              <a class="nav-link text-uppercase text-expanded" href="company.php">Company</a>
            </li>
          <li class="nav-item px-lg-4">
            <a class="nav-link text-uppercase text-expanded" href="profil.php">Profile</a>
          </li>
          <li class="nav-item px-lg-4">
            <a class="nav-link text-uppercase text-expanded" href="logout.php">Log Out</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

    <section class="page-section cta">
    <div class="container">
      <div class="row">
        <div style="font-size:30px" class="col-xl-9 mx-auto">
        Daftar Makanan 
        <br>
          <div class="cta-inner text-center rounded">
          <a href="tambah.php">Tambah Makanan</a>
          <form action="" method="post">
        <input type="text" name="keyword" size="30" autofocus placeholder="cari makanan" autocomplete="off">
        <button type="submit" name="cari">Cari</button>
    </form>
    <br>
    <!-- Food Table -->
    <table style="font-size:20px" id="t01" border="1" cellpading="20" cellspacing="0">
        <tr>
            <th>No.</th>
            <th>Aksi</th>
            <th>Nama</th>
            <th>Kalori (100gr)</th>
        </tr>

        <!-- Mengambil Data dari Database -->
        <?php $i = 1; ?>
        <?php foreach( $makanan as $row ): ?>
        <tr>
            <td ><?php echo $i; ?></td>
            <td>
              <a href="ubah.php">ubah</a> | 
              <a href="hapus.php?id=<?= $row["id"]; ?>">hapus</a>
            </td>
            <td><?php echo $row["nama"]; ?></td>
            <td><?php echo $row["kalori"]; ?></td>
        </tr>
        <?php $i++; ?>
        <?php endforeach; ?>
    </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer text-faded text-center py-5">
    <div class="container">
      <p class="m-0 small">Copyright &copy; Your Website 2020</p>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

</body>

</html>