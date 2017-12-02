<?php

  $con = mysqli_connect('localhost', 'root', '', 'rh3');
$query="UPDATE TABLE max_bid SET max_bid='$max_bid' AND winner='$winner' WHERE time='$time'";

?>
