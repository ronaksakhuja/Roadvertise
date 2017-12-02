<?php
$con = mysqli_connect('localhost', 'root', '', 'rh3');

$fp = fopen('file.csv', 'w');
fwrite($fp,"DAY_NUM,DAY,SLOT1,SLOT2,SLOT3,SLOT4,SLOT5,SLOT6\n");
$query="SELECT * FROM ocv";
$result=$con->query($query);
$count=0;
$day_num=0;
$day=0;
// $end=1;
while($row=mysqli_fetch_assoc($result)){
    if($count==0){
        // echo $day_num.",".$day.",";     
            fwrite($fp,$day_num.",".$day.",");
            // echo "in";
        // $end=0;
    }



    if($count!=0){
        fwrite($fp, ",");
        // echo ",";
    }
    $count++;
    fwrite($fp,$row['count']);
    // echo $row['count'];

    if($count==6){
        $day_num++;
        $day++;
        $day=$day%7;
        fwrite($fp,"\n");
        // echo nl2br("\n");
        $count=0;
    }
}
?>