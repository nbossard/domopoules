<?php
echo "Opening chicken door...";
$command = escapeshellcmd('/opt/chickendoor/open_door_force_short.py');
//$command = escapeshellcmd('ls -la /opt/chickendoor');
$execres = shell_exec($command);
echo "<pre>$execres</pre>";
?>
