<?php
    $command = escapeshellcmd('python3 /pop.py');
    $output = shell_exec($command);
    echo $output;
?>