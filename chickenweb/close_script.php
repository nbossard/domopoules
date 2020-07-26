<?php
echo "Closing chicken door...";
$command = escapeshellcmd('/opt/chickendoor/close_door.py');
$execres = shell_exec($command);
echo "<pre>$execres</pre>";
?>
