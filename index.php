<?php

    $conn = pg_connect("WOOPS");
    if($conn){
        // echo $conn;
        echo 'connected';
    }else{
        // echo $conn;
        echo 'not connected';
    }
   
?>
<html>
  <h1>-- html confirmation of that php stuff</h1>
</html>
