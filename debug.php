<?php

  $con = mysqli_connect('localhost', 'root', '', 'rh3');
  $sql = "SELECT * FROM ocv";

  $data = mysqli_fetch_all(mysqli_query($con, $sql), true);
  echo json_encode($data);

?>
