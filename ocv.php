<?php

  $con = mysqli_connect('localhost', 'root', '', 'rh3');

  $count = $_GET['count'];
  $time = $_SERVER['REQUEST_TIME'];

  $sql = "INSERT INTO ocv values ('$count', '$time')";

  mysqli_query($con, $sql);

?>
